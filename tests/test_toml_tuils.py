from pathlib import Path

import pytest

from poetry_version_increment_hook.toml_utils import (
    _read_toml,
    _write_toml,
    get_current_version,
    write_new_version,
)
from poetry_version_increment_hook.version import Version


@pytest.fixture()
def toml_data():
    data = {
        "tool": {
            "poetry": {
                "name": "project_name",
                "version": "1.2.3",
                "description": "test toml description",
                "authors": "lorem.ipsum@example.org",
            }
        }
    }
    yield data


@pytest.fixture()
def toml(toml_data):
    import toml

    path = Path.cwd().joinpath("test.toml")
    with open(path, "w") as f:
        f.write(toml.dumps(toml_data))
        f.close()

    yield path

    # path.unlink(missing_ok=False)


class TestTomlUtils:
    def test_read_toml(self, toml):
        data = _read_toml(toml)
        assert data["tool"]["poetry"]["version"] == "1.2.3"

    def test_read_toml_error(self):
        with pytest.raises(FileNotFoundError):
            _read_toml("file_not_exists.toml")

    def test_write_toml(self, toml, toml_data):
        toml_data["tool"]["poetry"]["lorem"] = "ipsum"

        _write_toml(toml_data, file_path=toml)

        data = _read_toml(toml)

        assert toml.exists()
        assert data["tool"]["poetry"]["lorem"] == "ipsum"

    def test_write_toml_error(self, toml_data):
        with pytest.raises(FileNotFoundError):
            _write_toml(toml_data, file_path="file_not_exists.toml")

    def test_get_current_version(self, toml):
        version = get_current_version(toml)
        assert version == Version(1, 2, 3)

    def test_get_current_version_error(self):
        with pytest.raises(FileNotFoundError):
            get_current_version("file_not_exists.toml")

    def test_new_version(self, toml):
        assert write_new_version(Version(1, 2, 4), path=toml)
