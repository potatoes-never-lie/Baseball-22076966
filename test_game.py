import pytest

from game import Game

@pytest.fixture
def game():
    return Game()

def assert_illegal_argument(game, guess_number):
    try:
        game.guess(guess_number)
        pytest.fail()
    except TypeError:
        pass

def test_exception_when_input_is_invalid(game):
    assert_illegal_argument(game, None)
    assert_illegal_argument(game, "12")
    assert_illegal_argument(game, "1234")
    assert_illegal_argument(game, "1s4")
    assert_illegal_argument(game, "121")

