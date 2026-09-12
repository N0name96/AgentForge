---
name: python-coding
description: Implement production-quality Python features and behavior while respecting the existing architecture and project conventions.
---

# Python Coding

Use this skill when implementing or modifying application behavior.

# Before Implementation

Understand:

1. What behavior is requested?
2. Where should that behavior live?
3. What existing implementation is most similar?
4. What interfaces or contracts are affected?
5. What tests already exist?
6. What compatibility constraints exist?

Avoid creating a new abstraction before checking whether one already exists.

# Implementation Strategy

Prefer incremental changes.

When possible:

1. Identify the correct extension point.
2. Implement the smallest complete change.
3. Keep responsibilities separated.
4. Reuse existing project abstractions.
5. Update tests.
6. Validate behavior.
7. Review the diff.

# Functions

Functions should have a clear responsibility.

Prefer:

- meaningful names
- explicit inputs
- explicit outputs
- limited side effects
- short execution paths

Do not split functions merely to reduce line count.

Extract functionality when it represents a meaningful concept or improves reuse, readability, or testability.

# Classes

Introduce classes when state, behavior, lifecycle, polymorphism, or domain modeling genuinely benefits from them.

Do not create classes solely to wrap one trivial function.

Prefer composition over inheritance unless the existing architecture clearly uses inheritance appropriately.

# Types

Use type hints where they improve correctness and understanding.

Especially consider typing:

- public interfaces
- service boundaries
- complex data structures
- returned values
- callbacks
- reusable utilities

Avoid meaningless typing that makes code harder to read.

Do not use `Any` merely to silence the type checker when a meaningful type can be expressed.

# Data Models

Use the abstraction already chosen by the project.

This might include:

- dataclasses
- Pydantic
- TypedDict
- attrs
- domain entities
- plain classes

Do not introduce a second modeling library without justification.

# Async Code

When working with async code:

- preserve async boundaries
- avoid blocking calls inside the event loop
- await asynchronous operations correctly
- manage tasks deliberately
- handle cancellation appropriately
- avoid introducing async where it provides no benefit

# Configuration

Do not hardcode environment-dependent values.

Follow the existing configuration system.

Separate configuration from business logic.

# Completion

Before finishing:

- inspect modified code
- verify imports
- check failure cases
- run relevant tests
- run project checks when available
- inspect the final diff
