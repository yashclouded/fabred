import os





README_FILES = [
    "README.md",
    "README.MD",
    "README.txt",
    "README.rst"
]


def get_readme(repo_path):
    for file in README_FILES:
        path = os.path.join(repo_path, file)

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()

    return None


def get_all_files(repo_path):
    files = []

    ignore_dirs = {
        ".git",
        "node_modules",
        ".next",
        "venv",
        ".venv",
        "__pycache__",
        "dist",
        "build",
        ".idea",
        ".vscode"
    }

    for root, dirs, filenames in os.walk(repo_path):

        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for filename in filenames:

            path = os.path.join(root, filename)

            files.append(path)

    return files
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    except:
        return ""