# interactive-test

[![Version](https://img.shields.io/badge/version-0.2.3-blue.svg)]()

`interactive-test` simulates realistic human users for testing another interactive assistant or skill. It is currently tuned for `causal-consultant`, including effect estimation, reporting, and causal-discovery sidecar or discovery-report scenarios.

The simulator must stay in character. It should never tell or hint to the target assistant that it is testing, scoring, logging, benchmarking, following hidden YAML, or recording backend observations. Controller-facing scenario reveals, logs, scores, and checkpoint summaries are never forwarded to the target assistant.

Scenario generation now uses six major parameters:

- `mode`
- `personality`
- `knowledge_level`
- `domain`
- `intent`
- `data_condition`

Intent carries task content, including `causal_discovery_sidecar` and `causal_discovery_report`. Data condition carries both availability and flaw severity. Run-length rules, stress behavior, pressure moves, multi-turn issue tracking, scorecards, and critical failures live in `assets/interactive_test_config.yaml`.

For real evaluations, the simulator should run longer conversations by default. A scored evaluation needs at least 20 user-assistant turn pairs and should usually include 20-30. It must exercise pressure, a compact artifact, a later flaw or contradiction, report chasing, a deliverable request, and post-deliverable follow-up before it can be marked pass. Very short runs are smoke checks only and should be marked invalid if used as pass/fail evidence.

Agent B should keep trying to get a usable report-like output. If a strong causal report is not supported, it should naturally ask what can be written instead, such as an exploratory report, descriptive summary, diagnostic memo, limitations-forward report, or stakeholder-safe slide narrative. After the assistant produces or narrows that output, Agent B should continue with follow-up questions to improve or understand it.

During a run, keep two artifacts separate:

- `runs/YYYY-MM-DD_HH-mm-ss-user-simulation.md` for settings, transcript, backend observations, and final evaluation;
- `reports/YYYY-MM-DD_HH-mm-ss-assistant-deliverables.md` for report-like outputs from the target assistant.

Do not save runner outputs inside this skill folder. Use a separate test workspace, usually with `runs/` and `reports/` directories. Use `TEST_CONTROLLER:` commands only for controller-side actions such as revealing the hidden scenario, saving a checkpoint, scoring the run, or ending the test.
