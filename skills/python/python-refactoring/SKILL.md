---
name: python-refactoring
description: Improve the structure, readability, maintainability, and design of Python code while preserving externally observable behavior.
---

# Python Refactoring

Use this skill when improving existing code without intentionally changing its externally observable behavior.

Refactoring is not feature development.

Its primary objective is to improve internal design while preserving functionality.

# Before Refactoring

Understand:

1. What problem is the refactor intended to solve?
2. What behavior must remain unchanged?
3. What tests currently protect that behavior?
4. Which callers depend on the code?
5. What public interfaces exist?
6. What project conventions apply?

Do not refactor code merely because you personally prefer another style.

There should be a meaningful improvement.

Examples:

- duplicated logic
- excessive coupling
- unclear responsibilities
- difficult testing
- overly complex functions
- misleading naming
- unnecessary inheritance
- poor module boundaries
- repeated conditionals
- tangled dependencies

# Preserve Behavior

Unless explicitly requested otherwise, preserve:

- public APIs
- return values
- exceptions
- side effects
- persistence behavior
- ordering guarantees
- externally visible data formats

Do not silently mix behavioral changes with structural refactoring.

If behavioral changes are necessary, make them explicit.

# Refactoring Strategy

Prefer small, controlled transformations.

A useful workflow is:

1. Understand current behavior.
2. Ensure sufficient test coverage.
3. Make one coherent structural improvement.
4. Run relevant tests.
5. Continue incrementally.
6. Review the complete diff.

Avoid massive rewrites when smaller transformations can achieve the same goal.

# Common Refactorings

Consider, where appropriate:

- extract function
- extract class
- inline unnecessary abstraction
- rename misleading symbols
- remove duplication
- simplify conditionals
- separate responsibilities
- reduce parameter count
- introduce meaningful value objects
- move behavior to the appropriate module
- remove dead code
- replace inappropriate inheritance with composition
- clarify dependency boundaries

Use these as tools, not objectives.

# Functions

Large functions are not automatically bad.

Refactor when a function:

- performs multiple unrelated responsibilities
- contains repeated logic
- has deeply nested control flow
- is difficult to understand or test
- mixes abstraction levels excessively

Extract functions around meaningful concepts.

Do not create tiny functions with meaningless names merely to reduce line length.

# Classes

Watch for classes that:

- have too many responsibilities
- depend on too many unrelated components
- expose too much internal state
- exist only as containers for unrelated helpers
- use inheritance where composition is more appropriate

Conversely, do not split cohesive classes simply to satisfy arbitrary size rules.

# Duplication

Not all similar code is true duplication.

Remove duplication when multiple code paths represent the same concept and are likely to evolve together.

Do not create premature generic abstractions for code that only happens to look similar.

Prefer a small amount of duplication over the wrong abstraction.

# Complexity

Reduce unnecessary complexity.

Look for:

- nested conditionals
- deeply nested loops
- boolean flags controlling unrelated behaviors
- hidden side effects
- duplicated branching logic
- unnecessary indirection

Prefer clear control flow.

# Dependencies

Refactoring should not casually introduce new dependencies.

If a design improvement requires a dependency change, justify it independently.

# Tests During Refactoring

Tests are the safety net.

Before significant refactoring:

- identify relevant tests
- add characterization tests if important behavior lacks coverage

During refactoring:

- run focused tests frequently

After refactoring:

- run the relevant test suite
- inspect the final diff

# Scope

Do not expand a focused refactor into a project-wide redesign.

Avoid opportunistically changing unrelated code.

If nearby code deserves improvement but is outside scope, mention it separately.

# Completion

A successful refactor should leave the code:

- easier to understand
- easier to modify
- easier to test
- less duplicated or coupled where relevant
- behaviorally equivalent unless otherwise requested

Explain what structural problem was improved and how behavior was verified.
