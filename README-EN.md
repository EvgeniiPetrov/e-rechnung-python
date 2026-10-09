[Deutsch](README.md) | [Русский](README-RU.md) | [English](README-EN.md)

# e-rechnung

**A Python application for generating and validating structured electronic invoices for Germany.**

> **Status:** In development. XRechnung XML generation and KoSIT Validator integration have not yet been implemented.

## Purpose

**e-rechnung** is intended to process structured invoice data in **JSON**, produce **XRechnung XML using the UBL 2.1 syntax**, and validate the generated files with the **KoSIT Validator**.

## Planned features

- Read and validate structured invoice data from JSON
- Generate electronic invoices in XRechnung format (UBL 2.1)
- Validate XML files using the KoSIT Validator
- Save generated files and validation reports
- Future extensions: invoice import and a web interface

## Current status

The repository currently contains the Python package structure, a basic command-line interface (**CLI**), and initial automated tests. Core functionality is under development.

**Technologies:** Python 3.13+, XML, JSON, pytest, Ruff, uv.

## Quick start

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/). Run from the project root:

```powershell
uv sync
uv run python -m e_rechnung --help
uv run pytest -q
```


## Project structure

```text
src/e_rechnung/    Python package and CLI
  domain/          Data models and business rules (planned)
  ubl/             XML generation (planned)
  validation/      KoSIT integration (planned)
tests/             Automated tests
sample-data/       Synthetic sample data
runtime/           Local input and output files
                   (not intended for version control)
tools/kosit/       Local KoSIT tools (provided separately)
docs/              Technical documentation
```


## Disclaimer

This project is **not affiliated** with KoSIT or German public authorities. Compliance of generated invoices with XRechnung has **not yet been demonstrated**. Do not commit real invoices, personal data, or credentials to this repository.
