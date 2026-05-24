---
name: run-tests
description: Run focused pytest checks for an exercise and summarize failures with file/function context.
---

# Run Tests

When asked to verify work, run the smallest relevant pytest target first:

```bash
python3 -m pytest <exercise_folder>/ -v
```

If failures occur, summarize:

- failing test name
- expected vs actual
- likely engineering or implementation cause
- exact next edit
