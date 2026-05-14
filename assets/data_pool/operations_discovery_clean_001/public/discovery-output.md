# Causal Discovery Output

Analyst note: this was a first-pass PC-style run on shift-level data. It is exploratory.

Candidate directed edges:

| Edge | Stability |
| --- | ---: |
| `incoming_orders -> throughput_units` | 0.86 |
| `avg_staffing -> throughput_units` | 0.79 |
| `machine_downtime_min -> throughput_units` | 0.74 |
| `pick_delay_min -> throughput_units` | 0.66 |
| `machine_downtime_min -> defect_rate` | 0.58 |

Undirected or unstable links:

- `pick_delay_min -- machine_downtime_min`
- `avg_staffing -- defect_rate`

Background constraints supplied:

- `incoming_orders` and `avg_staffing` are pre-shift.
- `throughput_units` and `defect_rate` are end-of-shift outcomes.
- No minute-level ordering is available within a shift.
