from src.main import typer
from typer.testing import CliRunner

runner = CliRunner()


def test_get_language_for_local():
    result = runner.invoke(typer, ["get-language-for-local", "cpp.txt"])
    assert result.exit_code == 0
    assert "C++" in result.stdout
