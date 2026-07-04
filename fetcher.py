from pathlib import Path
import subprocess
import shutil


TEMP_DIR = Path("temp")


def clean_temp():
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)

    TEMP_DIR.mkdir(exist_ok=True)


def clone_repo(repo_url: str) -> Path:

    clean_temp()

    repo_name = repo_url.rstrip("/").split("/")[-1]
    destination = TEMP_DIR / repo_name

    print(f"Cloning {repo_name}...")

    result = subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            repo_url,
            str(destination),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return destination