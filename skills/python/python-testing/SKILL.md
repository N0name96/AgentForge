---
name: python-testing
description: Design and implement useful automated tests for Python applications.
---

# Python Testing

Understand the existing testing stack before creating tests.

Detect whether the project uses:
- pytest
- unittest
- hypothesis
- integration tests
- fixtures
- mocks
- factories

Follow existing conventions.

## Test priorities

Tests should focus on behavior rather than implementation details.

Prefer testing:
- normal behavior
- boundary conditions
- errors
- regressions
- important business rules

Avoid excessive mocking.

Mock external boundaries when appropriate, not internal implementation details.

## Quality

Tests should be:
- deterministic
- independent
- readable
- focused
- fast when possible