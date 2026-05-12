# interactive-test

[![Version](https://img.shields.io/badge/version-0.2.1-blue.svg)]()

`interactive-test` is a skill for testing another interactive assistant or skill through realistic simulated-user conversations.

The simulator acts like a normal human user talking to the target assistant. In chat, it should stay short, casual, incomplete, and realistic. It should not mention that it is testing a skill, following a hidden scenario, evaluating the assistant, or recording backend observations.

Currently this is constructed specifically to test the `causal-consultant` skill, including effect-estimation, reporting, and causal-discovery sidecar scenarios. The skill entrypoint is `SKILL.md`, and the skill name in frontmatter is `interactive-test`.

During a run, `interactive-test` keeps two things separate:

- in-character conversation with the target assistant;
- backend evaluation notes about the target assistant's behavior.

Backend observations should be saved in the run log, not spoken to the target assistant. These observations may record issues such as internal workflow leakage, unsupported results, overconfident causal language, claim-scope upgrades, missed inconsistencies, or poor user-facing communication.

Do not save test outputs in this skill folder. Batch test results should live in a separate testing/results folder, such as `../skill testing/test-results/`. Runner-managed conversation logs and generated assistant deliverables should live outside this folder, usually under a separate workspace's `runs/` and `reports/` directories.

To use this for other interactive skills, modify the hidden scenario generation, controller focus, observation checklist, and expected deliverable sections accordingly.

Use `TEST_CONTROLLER:` commands only when you want `interactive-test` to break character, reveal the hidden scenario, save a checkpoint, or summarize the target assistant's behavior.
