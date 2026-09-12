---
name: git-workflow
description: Use Git safely while inspecting changes, understanding repository state, and preparing clean development work without performing destructive or remote operations unexpectedly.
---

# Git Workflow

Use Git to understand and validate changes.

# Before Working

Inspect the repository state when relevant.

Check:

- current branch
- modified files
- staged files
- untracked files

Assume existing user changes may be intentional.

Never overwrite or discard them without explicit authorization.

# During Development

Use Git to inspect:

- current modifications
- historical context when useful
- previous implementations
- relevant blame/history when necessary

Do not use Git history as a substitute for understanding current code.

# Diff Review

Before considering development work complete, inspect the final diff.

Look for:

- accidental changes
- debug code
- formatting noise
- unrelated modifications
- generated files that should not be included
- secrets
- incomplete edits

# Destructive Operations

Do not perform destructive Git actions without explicit permission.

Examples include:

- `git reset --hard`
- deleting branches
- rewriting shared history
- force pushes
- discarding user changes

# Commits

Only create commits when requested or explicitly permitted.

A commit should contain a coherent change.

Avoid mixing unrelated work.

Use concise, meaningful commit messages that explain the change.

# Remote Operations

Do not push changes unless explicitly authorized.

Do not force push unless the user explicitly requests it and the consequences are understood.

# Existing User Work

Treat existing uncommitted changes as user-owned work.

Do not:

- revert them
- reformat them unnecessarily
- move them
- include them in unrelated work

If they conflict with the requested task, work around them when possible and explain the conflict when necessary.
