# Data Dictionary

Context: retention campaign analysis for an online subscription product.

Row unit: customer-month.

Outcome: `renewed_30d`, whether the customer renewed within 30 days after the campaign window.

Columns:

- `customer_id`: anonymized customer id.
- `month`: calendar month for the row.
- `campaign_flag`: 1 if the customer received the winback campaign message during the month.
- `days_since_last_login`: days between last login and the campaign send or monthly snapshot.
- `prior_3mo_spend`: customer spending in the three months before the monthly snapshot.
- `support_tickets_30d`: support tickets in the 30 days around the campaign month.
- `discount_offer`: 1 if the message included a discount.
- `renewed_30d`: 1 if the customer renewed within 30 days.
- `segment`: lifecycle segment assigned by marketing.

Notes from the analyst:

- The campaign was targeted to customers the lifecycle team thought were at risk.
- Some campaign rows appear after a customer had already contacted support about cancellation.
- The team wants a short executive readout by Friday.
