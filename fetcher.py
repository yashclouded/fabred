import os
import shutil
import tempfile
from git import Repo

TEMP_FOLDER = "temp_repos"


def clean_temp():
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)

    os.makedirs(TEMP_FOLDER, exist_ok=True)


def clone_repo(repo_url: str):
    clean_temp()

    repo_name = repo_url.rstrip("/").split("/")[-1]
    repo_path = os.path.join(TEMP_FOLDER, repo_name)

    Repo.clone_from(
        repo_url,
        repo_path,
        depth=1
    )

    return repo_path