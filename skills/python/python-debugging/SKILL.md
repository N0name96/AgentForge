---
name: python-debugging
description: Diagnose and fix Python bugs using evidence-driven debugging.
---

# Python Debugging

Use this skill when investigating defects, unexpected behavior,
exceptions or failing tests.

## Workflow

1. Read the error carefully.
2. Identify the entry point where the failure occurs.
3. Trace the relevant execution path.
4. Inspect related tests.
5. Reproduce the failure when possible.
6. Form a concrete hypothesis.
7. Validate the hypothesis before modifying code.
8. Apply the smallest safe fix.
9. Add or update a regression test.
10. Run relevant tests.
11. Review the diff.

## Rules

Do not:
- change unrelated code
- suppress exceptions without understanding them
- remove failing tests to make the suite pass
- add broad try/except blocks to hide errors

Prefer understanding the root cause over treating symptoms.