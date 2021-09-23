from pathlib import Path
from typing import Dict, Union

import toml

from poetry_version_increment_hook.version import Version


def get_current_version(path: Union[Path, str] = "pyproject.toml") -> Version:
    """

    Args:
        path:

    Returns:

    """
    data = _read_toml(path=path)
    version = data["tool"]["poetry"]["version"]
    return Version(*[int(x) for x in version.split(".")])


def write_new_version(
    version: Version, path: Union[Path, str] = "pyproject.toml"
) -> bool:
    """

    Args:
        version:
        path:

    Returns:

    """
    data = _read_toml(path)
    data["tool"]["poetry"]["version"] = version.__str__()
    _write_toml(data, path)

    return get_current_version(path=path) == version


def _read_toml(path: Union[Path, str]) -> Dict:
    """
    Args:
        path: path to yaml file

    Returns:
        dict of yaml values.
    """
    path = Path(path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"Cannot find YAML file - {path}")

    return toml.load(str(path))


def _write_toml(data: Dict, file_path: Union[Path, str] = "pyproject.toml"):
    """
    Args:
        data: dict of yaml values.
        file_path: path to yaml file

    """

    path = Path(file_path)
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(
            f"Cannot find TOML file {path} - should be present."
        )

    try:
        with open(path, "r+") as f:
            f.write(toml.dumps(data))
    finally:
        f.close()
