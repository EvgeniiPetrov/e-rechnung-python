"""Проверка окружения без сторонних библиотек и без подключения к сети.

Из корня репозитория:
    python scripts/check_environment.py
"""

from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    print("Python:", sys.version.split()[0])
    print("Python executable:", sys.executable)
    print("Project root:", root)
    print("pyproject.toml:", (root / "pyproject.toml").is_file())
    for package in ("pytest", "ruff", "lxml", "defusedxml"):
        print(f"{package} installed:", importlib.util.find_spec(package) is not None)
    for executable in ("git", "uv", "java"):
        print(f"{executable} available:", shutil.which(executable) or "no")
    if sys.version_info < (3, 13):
        print("WARNING: learning scaffold requires Python 3.13+")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
