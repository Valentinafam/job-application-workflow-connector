# Workflow Connection

This connector links lead discovery to application execution without storing private candidate data in the public repository.

## Flow

1. Onboarding
   - Create a private candidate profile.
   - Define application rules.
   - Add resume variants and routing rules.
   - Confirm reusable answer-bank wording.

2. Lead Finding
   - Run the lead-finding skill on a schedule, usually daily or every two days.
   - Save discovered jobs to `dashboard/job_pool.csv`.
   - Extract high-frequency job description and requirement keywords.
   - Classify each job by role family, fit, priority, and blocker status.

3. Resume and Cover Letter Routing
   - Volume mode uses a prebuilt resume variant by role family.
   - Precision mode tailors resume and cover letter for the specific posting.
   - Every application should have a cover letter unless the platform has no upload or text field.

4. Application Execution
   - Apply only to jobs that pass the user's rules.
   - Stop for CAPTCHA, login, 2FA, unclear legal facts, sensitive answers, or failed upload verification.
   - Record every attempt in `dashboard/application_log.csv`.

5. Dashboard Review
   - Show daily totals, job pool, application status, blockers, and follow-up actions.
   - Convert repeated blockers into `dashboard/automation_rules.csv`.

## Mode Policy

Volume mode:

- Use existing resume variants.
- Submit simple, low-risk applications after the user has authorized that behavior.
- Do not tailor materials unless a rule promotes the job to Precision.

Precision mode:

- Tailor resume and cover letter.
- Ask user to approve final materials and submission.
- Use this for high-fit jobs, government jobs, complex forms, or strategic employers.

## State Machine

```text
Found -> Screened -> Pending
Found -> Screened -> Skipped
Pending -> Applying -> Submitted
Pending -> Applying -> Blocked
Pending -> Needs user -> Applying
```

Only count `Submitted` after explicit confirmation evidence appears.

