from pathlib import Path

from poetry_version_increment_hook.git_utils import get_current_branch, Branch
from poetry_version_increment_hook.toml_utils import (
    get_current_version,
    write_new_version,
)


def run():
    toml_files = list(Path.cwd().parent.parent.glob("**/pyproject.toml"))

    if len(toml_files) == 0:
        FileNotFoundError("Could not find any pyproject.toml files.")

    path = toml_files[0]

    current_version = get_current_version(path=path)
    current_branch = get_current_branch()

    if current_branch is Branch.MASTER:
        current_version.inc_major()

    elif current_branch is Branch.DEVELOP:
        current_version.inc_minor()

    elif current_branch is Branch.HOTFIX:
        current_version.inc_patch()

    write_new_version(version=current_version, path=path)


if __name__ == "__main__":
    run()
