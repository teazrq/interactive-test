# interactive-test

[![Version](https://img.shields.io/badge/version-0.2.11-blue.svg)]()

`interactive-test` simulates realistic human users for testing another interactive assistant or skill. It is currently tuned for `causal-consultant`, including causal claims, method/design questions, data interpretation, debugging/rescue work, reporting, and causal discovery.

The simulator must stay in character. It should never tell or hint to the target assistant that it is testing, scoring, logging, benchmarking, following hidden YAML, or recording backend observations. Controller-facing scenario reveals, logs, scores, and checkpoint summaries are never forwarded to the target assistant.

The simulated user is deliberately not an attentive analyst. It usually skim-reads long replies, responds in one or two short sentences, answers only part of multi-question prompts, and keeps pushing its selected hidden intent for a sampled number of turns before becoming more accepting.

Scenario generation uses only four top-level settings:

- `mode` - one of 15 hidden-intent behavior modes
- `knowledge_level`
- `domain`
- `data_condition` - `no_data` or `flawed_data`

The mode cards live in `assets/hidden_intent_modes.yaml`. At run start, the simulator randomly selects one card unless the controller sets a mode, then copies the selected card verbatim into the private run YAML under `hidden_intent_mode`. These hidden-intent scenarios are general and independent of domain, knowledge level, and data condition.

There is no separate task-type, persona, deliverable, discovery-active, or flaw-severity setting. Each mode belongs to one of five intent categories: `effect_claim`, `method_or_design`, `data_interpretation`, `debug_or_rescue`, or `causal_discovery`.

For `flawed_data` scenarios, the simulator selects a packet from `assets/data_pool/` and copies only its `public/` files into the run's `artifacts/` folder. A packet can include a schema, small synthetic data file or toy rows, analysis output, discovery output, draft report, or limitation note. Hidden evaluator notes remain in the skill package.

Packet selection is coverage-aware: unconstrained data-bearing runs choose from available packets first, while `scripts/prepare_data_packet.py` copies only public files into the run workspace.

For real evaluations, the simulator samples a target length centered around 10 user-assistant turn pairs, usually 8-12 and never more than 14 unless the controller explicitly overrides it. It must exercise the selected mode focus, hidden-intent persistence, relevant compact artifact, later fact or recovery reveal, output or next-step request, and post-output follow-up before it can be marked pass.

Final evaluation uses one turn-number measure plus five 0-5 scores: earliest failure turn, recovery/adaptation, hidden-intent resistance, grounding/claim calibration, interaction usefulness, and final report polish. For non-report runs, final report polish scores the final usable output or next-step summary.

During a run, keep generated files separated:

- `runs/YYYY-MM-DD_HH-mm-ss-user-simulation.md` for settings, transcript, backend observations, and final evaluation;
- `reports/YYYY-MM-DD_HH-mm-ss-assistant-deliverables.md` for report-like outputs from the target assistant;
- `artifacts/YYYY-MM-DD_HH-mm-ss/` for synthetic user-facing data packets used during the conversation.

Each run log includes a `Skill Load Check` section. Fallback-only or unverified runs should not be counted as normal pass/fail evidence.

Do not save runner outputs inside this skill folder. Use a separate test workspace, usually with `runs/`, `reports/`, and `artifacts/` directories. Use `TEST_CONTROLLER:` commands only for controller-side actions such as revealing the hidden scenario, saving a checkpoint, scoring the run, or ending the test.
