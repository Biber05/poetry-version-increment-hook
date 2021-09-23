from enum import Enum

import git

MASTER_RE = ["main", "master", "release"]

DEVELOP_RE = ["develop", "dev"]

FEATURE_RE = ["feature", "feat"]

HOTFIX_RE = ["hotfix", "fix", "patch"]


class Branch(Enum):
    MASTER = 1
    DEVELOP = 2
    HOTFIX = 3
    FEATURE = 4
    UNKNOWN = 0


def get_current_branch() -> Branch:
    """
    get branch category

    Returns:
        Branch
    """
    branch_name = _read_git_branch()

    if branch_name in MASTER_RE:
        return Branch.MASTER

    elif branch_name in DEVELOP_RE:
        return Branch.DEVELOP

    elif branch_name.split("/")[0] in FEATURE_RE:
        return Branch.FEATURE

    elif branch_name.split("/")[0] in HOTFIX_RE:
        return Branch.HOTFIX

    return Branch.FEATURE


def _read_git_branch() -> str:
    """
    read active branch from current repository

    Returns:
        branch name as string
    """
    from pathlib import Path

    repo = git.Repo.init(Path.cwd().parent)
    return repo.active_branch.name
