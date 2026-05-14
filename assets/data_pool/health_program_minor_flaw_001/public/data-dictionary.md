# Data Dictionary

Context: hospital readmission coaching program.

Row unit: discharged patient.

Columns:

- `patient_id`: anonymized patient id.
- `discharge_date`: hospital discharge date.
- `coaching_offer`: 1 if the patient was offered post-discharge coaching.
- `accepted_coaching`: 1 if the patient accepted and received at least one call.
- `age`: age at discharge.
- `prior_admissions`: admissions in the prior year.
- `risk_score`: discharge risk score from the care-management system.
- `readmitted_30d`: 1 if readmitted within 30 days.

Notes:

- Coaching was offered based on staff availability and risk score.
- A few `risk_score` values are missing because one clinic joined the system later.
