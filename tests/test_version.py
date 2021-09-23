import pytest

from poetry_version_increment_hook.version import Version


@pytest.fixture()
def version():
    yield Version(1, 2, 3)


class TestVersionClass:
    def test_str(self, version):
        assert version.__str__() == "1.2.3"

    def test_inc_major(self, version):
        version.inc_major()

        assert version.major == 2
        assert version.__str__() == "2.2.3"

    def test_inc_minor(self, version):
        version.inc_minor()

        assert version.minor == 3
        assert version.__str__() == "1.3.3"

    def test_inc_patch(self, version):
        version.inc_patch()

        assert version.patch == 4
        assert version.__str__() == "1.2.4"

    def test_inc_all(self, version):
        version.inc_major()
        version.inc_minor()
        version.inc_patch()

        assert version.__str__() == "2.3.4"
