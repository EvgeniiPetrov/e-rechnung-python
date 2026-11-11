# Repository Guidelines

## Security

- Never commit credentials, API keys, passwords,
  access tokens, or private certificates.
- Never include real invoices or personal data
  in tests, examples, or documentation.
- Use synthetic data for examples and tests.
- Do not expose sensitive information in logs
  or error messages.
- Do not modify environment variables or local
  configuration files without explicit permission.

## Project Structure & Module Organization

- `src/e_rechnung/` contains the Python package.
  - `cli.py` provides the command-line entry point.
  - `domain/` contains pure validation and business-rule functions.
  - `ubl/`, `validation/`, and `storage/` are reserved for future XML generation, KoSIT integration, and local output handling.
- `tests/` contains pytest tests. Name test modules `test_<feature>.py`.
- `sample-data/` holds synthetic, version-controlled invoice examples.
- `runtime/` is for local input, generated XML, and reports; never commit its contents.
- `tools/kosit/` is for locally installed KoSIT artifacts. Do not commit JARs, configurations, or real invoices.

## Build, Test, and Development Commands

Run commands from the repository root:

```powershell
python scripts/check_environment.py
uv sync
uv run python -m e_rechnung --help
uv run pytest -q
uv run ruff check .
```

Use uv sync --locked --offline and uv run --offline ... when working from a prepared offline cache. Do not use a manual PYTHONPATH.

## Coding Style & Naming Conventions

Use Python 3.13+ and four-space indentation. Keep domain functions small, deterministic, and free of file I/O, printing, XML handling, and subprocess calls.

Use snake_case for modules, functions, variables, and test names. Prefer explicit type annotations on production functions. Use Decimal constructed from strings for monetary values; do not use float for invoice amounts.

Ruff is the configured linter. Run uv run ruff check . before submitting changes.

## Architecture Simplicity

The project name is `e-rechnung-python`. Prefer a small, direct module structure and
working code over premature abstractions. Do not introduce design patterns, service
layers, factories, repositories, or dependency injection unless a concrete requirement
and tests demonstrate their need. Extend the existing `domain/`, `cli.py`, `ubl/`, and
`validation/` modules directly when that keeps the code clear.

## Agent Workflow

- Before making changes, inspect the relevant code,
  tests, and documentation.
- For tasks involving multiple modules, architectural changes,
  or unclear requirements, present an implementation plan
  and wait for approval before modifying files.
- For small, clearly specified tasks, proceed directly
  with implementation.
- Follow the task requirements and acceptance criteria
  strictly.
- Do not implement functionality outside the requested scope.
- Do not perform unrelated refactoring.
- If requirements are ambiguous or incomplete, ask
  for clarification before making assumptions that
  affect behavior or architecture.
- Keep changes focused and limited to the task.
- Update documentation when behavior or project
  conventions change.

## Testing Guidelines

Use pytest. Add positive, invalid-input, and boundary tests for each behavior change. Keep tests independent of the network, current directory, and locally installed KoSIT files unless explicitly testing that integration.

Run the focused test first, for example:

uv run pytest -q tests/test_validate_currency.py

Then run the full suite.

## Commit and Pull Request Guidelines

Follow the existing Conventional Commits-style convention:
`<type>: <description>`.

Use lowercase types such as:
`feat`, `fix`, `test`, `chore`, `refactor`, and `docs`.

Examples:
- `feat: validate issue date`
- `fix: handle empty currency`
- `test: add currency edge cases`

Keep each change focused.

Never create commits, push changes, or create pull requests
without explicit user permission.

In a pull request, explain the behavior change, affected files,
test command and result, and any documentation or compatibility impact.

Never include real invoices, credentials, or generated runtime artifacts.

## Git Operations

- Never create commits automatically.
- Never amend, rebase, reset, or rewrite Git history
  without explicit permission.
- Never push changes to a remote repository
  without explicit permission.
- Never create or merge pull requests without
  explicit permission.
- Do not discard or overwrite uncommitted user changes.
- After completing a task, present the changes
  and wait for user review.
  - Complete all requested implementation and verification
  steps before presenting the final report.
- Do not stop merely because implementation is complete
  if requested verification steps remain.
- Wait for user approval before creating a commit.

## Completion Report

After completing a task, provide:

1. Summary of implemented changes.
2. List of modified and created files.
3. Tests executed and their results.
4. Ruff check results, if applicable.
5. Known limitations or unresolved issues.
6. Any deviations from the original requirements.

Clearly distinguish between completed, partially
completed, and unverified work.

Never claim that a test or command passed
if it was not actually executed.
