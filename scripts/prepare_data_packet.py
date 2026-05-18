#!/usr/bin/env python3
"""Select and copy a public data packet for an interactive-test run.

The source data pool may contain hidden evaluator notes and evaluator labels.
This script copies only files under the selected packet's public/ directory into
the run artifact folder. It prints controller-side JSON metadata, including the
hidden notes path, so the run log can record the selected packet without
exposing hidden files or labels to the target assistant.
"""

from __future__ import annotations

import argparse
import json
import random
import shutil
from pathlib import Path


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def score_packet(packet: dict, domain: str | None, intent_category: str | None, data_condition: str | None) -> int:
    score = 0
    if domain and packet.get("domain") == domain:
        score += 4
    if intent_category and intent_category in packet.get("intent_categories", []):
        score += 4
    if data_condition and packet.get("data_condition") == data_condition:
        score += 5
    return score


def packet_matches_constraints(packet: dict, args: argparse.Namespace) -> bool:
    if args.domain and packet.get("domain") != args.domain:
        return False
    if args.intent_category and args.intent_category not in packet.get("intent_categories", []):
        return False
    if args.data_condition and packet.get("data_condition") != args.data_condition:
        return False
    return True


def select_packet(index: dict, args: argparse.Namespace) -> dict:
    packets = index.get("packets", [])
    if not packets:
        raise SystemExit("No packets listed in data pool index.")

    if args.packet_id:
        matches = [packet for packet in packets if packet.get("packet_id") == args.packet_id]
        if not matches:
            raise SystemExit(f"Packet id not found: {args.packet_id}")
        return matches[0]

    eligible = [packet for packet in packets if packet_matches_constraints(packet, args)]

    if eligible:
        seed = args.seed or f"{args.run_id}:{args.domain}:{args.intent_category}:{args.data_condition}"
        return random.Random(seed).choice(eligible)

    if not args.allow_near_match:
        raise SystemExit(
            "No data packet matches the provided constraints. Re-run with --allow-near-match or choose a packet id."
        )

    ranked = sorted(
        packets,
        key=lambda packet: score_packet(packet, args.domain, args.intent_category, args.data_condition),
        reverse=True,
    )
    best_score = score_packet(ranked[0], args.domain, args.intent_category, args.data_condition)
    if best_score <= 0:
        raise SystemExit("No usable near-match data packet found.")

    best = [
        packet
        for packet in ranked
        if score_packet(packet, args.domain, args.intent_category, args.data_condition) == best_score
    ]
    seed = args.seed or f"{args.run_id}:near:{args.domain}:{args.intent_category}:{args.data_condition}"
    return random.Random(seed).choice(best)


def copy_public_files(packet_dir: Path, destination: Path) -> list[dict]:
    public_dir = packet_dir / "public"
    if not public_dir.is_dir():
        raise SystemExit(f"Selected packet has no public directory: {packet_dir}")

    destination.mkdir(parents=True, exist_ok=True)
    copied = []
    for source in sorted(path for path in public_dir.rglob("*") if path.is_file()):
        relative = source.relative_to(public_dir)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        copied.append(
            {
                "source": str(source),
                "path": str(target),
                "relative_path": str(relative).replace("\\", "/"),
            }
        )
    return copied


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare an interactive-test data packet.")
    parser.add_argument("--pool-index", required=True, help="Path to assets/data_pool/index.json.")
    parser.add_argument("--run-id", required=True, help="Run id used for artifact destination metadata.")
    parser.add_argument("--domain", help="Optional domain constraint.")
    parser.add_argument("--intent-category", help="Optional hidden intent category constraint.")
    parser.add_argument("--data-condition", help="Optional data-condition constraint.")
    parser.add_argument("--destination", required=True, help="Run artifact folder to receive public files.")
    parser.add_argument("--packet-id", help="Optional exact packet id.")
    parser.add_argument("--seed", help="Optional deterministic selection seed.")
    parser.add_argument("--allow-near-match", action="store_true", help="Allow closest packet if no exact match exists.")
    args = parser.parse_args()

    index_path = Path(args.pool_index).resolve()
    pool_root = index_path.parent
    index = load_json(index_path)
    packet = select_packet(index, args)
    packet_dir = (pool_root / packet["path"]).resolve()
    destination = Path(args.destination).resolve()

    copied_files = copy_public_files(packet_dir, destination)
    manifest = load_json(packet_dir / "packet.json")
    hidden_notes_path = packet_dir / "hidden" / "evaluator-notes.json"

    selection = {
        "run_id": args.run_id,
        "selection_source": "data_pool",
        "pool_index": str(index_path),
        "packet_id": packet["packet_id"],
        "packet_path": str(packet_dir),
        "domain": manifest.get("domain"),
        "intent_categories": manifest.get("intent_categories", []),
        "data_condition": manifest.get("data_condition"),
        "artifact_types": manifest.get("artifact_types", []),
        "entrypoint": str(destination / manifest.get("user_facing_entrypoint", "")),
        "destination": str(destination),
        "copied_public_files": copied_files,
        "hidden_evaluator_notes_path": str(hidden_notes_path) if hidden_notes_path.exists() else None,
    }

    print(json.dumps(selection, indent=2))


if __name__ == "__main__":
    main()
