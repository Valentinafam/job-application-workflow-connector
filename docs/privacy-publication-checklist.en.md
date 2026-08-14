# Privacy and Publication Checklist

Before publishing:

- Remove real resumes, cover letters, screenshots, and generated application materials.
- Remove candidate names, emails, phone numbers, addresses, immigration details, and postal codes.
- Remove real job application logs, confirmation text, recruiter messages, and interview notes.
- Remove local paths such as `/Users/...`.
- Remove browser sessions, cookies, local storage, cache, and exported passwords.
- Replace private job board data with empty templates or short synthetic examples.
- Preserve upstream license notices for any MIT-licensed material you reuse.
- Do not redistribute source files from repositories without an explicit license unless you have written permission.

Run:

```bash
python3 scripts/check_no_private_data.py .
```

This script is a helper, not a guarantee. Review the repository manually before making it public.

