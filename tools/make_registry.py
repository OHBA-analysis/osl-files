"""Writes registry.txt: one line per data file, with its SHA-256 checksum.

The packages that fetch these files download this registry at runtime and use
it both as the list of available files and to verify what they download. It is
regenerated automatically by .github/workflows/registry.yml, so there is no
need to run this by hand unless you want to check the result.
"""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Everything that is not a data file.
SKIP_DIRECTORIES = {".git", ".github", "docs", "LICENSES", "tools"}
SKIP_NAMES = {".DS_Store", ".gitignore", "NOTICE", "README.md", "registry.txt"}


def main() -> None:
    lines = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if relative.parts[0] in SKIP_DIRECTORIES or relative.name in SKIP_NAMES:
            continue
        checksum = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{relative.as_posix()} sha256:{checksum}")

    (ROOT / "registry.txt").write_text("\n".join(lines) + "\n")
    print(f"registry.txt: {len(lines)} files")


if __name__ == "__main__":
    main()
