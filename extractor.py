from pathlib import Path

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules",
    "dist",
    "build",
    ".idea",
    ".vscode",
    ".next",
}

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".cpp",
    ".c",
    ".cs",
    ".go",
    ".rs",
    ".php",
    ".rb",
    ".swift",
    ".kt",
    ".scala",
    ".ipynb",
    ".md",
    ".txt",
    ".toml",
    ".json",
    ".yaml",
    ".yml",
}


def get_all_files(repo_path: Path):


    files = []

    for path in repo_path.rglob("*"):

        if not path.is_file():
            continue

        if any(folder in IGNORE_DIRS for folder in path.parts):
            continue

        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(path)

    return files


def read_file(file_path: Path):


    try:
        return file_path.read_text(
            encoding="utf-8",
            errors="ignore",
        )

    except Exception:
        return ""


def get_readme(repo_path: Path):

    candidates = [
        "README.md",
        "readme.md",
        "README.rst",
        "README.txt",
    ]

    for name in candidates:

        file = repo_path / name

        if file.exists():
            return read_file(file)

    return ""


def get_dependency_files(repo_path: Path):


    dependency_files = [
        "requirements.txt",
        "pyproject.toml",
        "package.json",
        "Cargo.toml",
        "go.mod",
        "Pipfile",
    ]

    found = []

    for file in dependency_files:

        path = repo_path / file

        if path.exists():
            found.append(path)

    return found


def extract_repository(repo_path: Path):
# extracts the README, all files, and dependency files from a cloned repository.

    return {
        "readme": get_readme(repo_path),
        "files": get_all_files(repo_path),
        "dependency_files": get_dependency_files(repo_path),
    }