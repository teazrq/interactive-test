# Data Dictionary

Context: warehouse throughput monitoring.

Row unit: shift line.

Columns:

- `shift_id`: anonymized shift id.
- `line`: packing line.
- `avg_staffing`: average staff count during the shift.
- `machine_downtime_min`: downtime minutes recorded during the shift.
- `incoming_orders`: orders released to the line before shift start.
- `pick_delay_min`: average upstream pick delay.
- `throughput_units`: packed units during the shift.
- `defect_rate`: share of packed units flagged by quality checks.

Notes:

- Operations wants to know whether graph discovery can suggest bottlenecks.
- Timestamps are shift-level, not minute-level.
- The team has prior knowledge that incoming orders and staffing are set before throughput is observed.
