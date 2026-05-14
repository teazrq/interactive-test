# interactive-test

[![Version](https://img.shields.io/badge/version-0.2.1-blue.svg)]()

`interactive-test` simulates realistic human users for testing another interactive assistant or skill. It is currently tuned for `causal-consultant`, including effect estimation, reporting, and causal-discovery sidecar or discovery-report scenarios.

The simulator must stay in character. It should never tell or hint to the target assistant that it is testing, scoring, logging, benchmarking, following hidden YAML, or recording backend observations. Controller-facing scenario reveals, logs, scores, and checkpoint summaries are never forwarded to the target assistant.

Scenario generation now uses six major parameters:

- `mode`
- `personality`
- `knowledge_level`
- `domain`
- `intent`
- `data_condition`

Intent carries task content, including `causal_discovery_sidecar` and `causal_discovery_report`. Data condition carries both availability and flaw severity. Stress behavior, pressure moves, multi-turn issue tracking, scorecards, and critical failures live in `assets/interactive_test_config.yaml`.

During a run, keep two artifacts separate:

- `runs/YYYY-MM-DD_HH-mm-ss-user-simulation.md` for settings, transcript, backend observations, and final evaluation;
- `reports/YYYY-MM-DD_HH-mm-ss-assistant-deliverables.md` for report-like outputs from the target assistant.

Do not save runner outputs inside this skill folder. Use a separate test workspace, usually with `runs/` and `reports/` directories. Use `TEST_CONTROLLER:` commands only for controller-side actions such as revealing the hidden scenario, saving a checkpoint, scoring the run, or ending the test.
