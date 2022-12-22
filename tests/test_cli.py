import pytest
from click.testing import CliRunner
from cli import make_change
from mlib.mchange import change



# def test_change():
#     assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)

@pytest.fixture
def runner():
    yield CliRunner()

@pytest.fixture
def amount():
    yield [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] 

def test_change(amount):
    assert amount == change(1.34)


def test_cli_help(runner):
#   runner = CliRunner()
  result = runner.invoke(make_change, ['--help'])
  assert result.exit_code == 0
  assert "Usage" in result.output

def test_cli_change(runner,amount):
#   runner = CliRunner()  
  result = runner.invoke(make_change, ['--amount', '1.34'])
  assert result.exit_code == 0
  assert "5" in result.output

