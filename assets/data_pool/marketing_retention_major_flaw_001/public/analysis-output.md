# First-Pass Analysis Output

Analyst note: this was a quick logistic regression, not a final causal model.

Outcome: `renewed_30d`

Predictors included: `campaign_flag`, `prior_3mo_spend`, `days_since_last_login`, `support_tickets_30d`, `segment`

Summary:

| Term | Estimate | Std. error | p-value |
| --- | ---: | ---: | ---: |
| campaign_flag | 0.31 | 0.12 | 0.010 |
| prior_3mo_spend | 0.004 | 0.001 | 0.003 |
| days_since_last_login | -0.018 | 0.006 | 0.004 |
| support_tickets_30d | -0.22 | 0.08 | 0.006 |

Extra note: lifecycle targeting rules were updated during the same quarter.
