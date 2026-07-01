import pytest

from game import Game
from game_result import GameResult


@pytest.fixture
def game():
    return Game()

def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "1s4", "121"])
def test_exception_when_input_is_invalid(game, invalid_input):
    assert_illegal_argument(game, invalid_input)

def test_return_solved_result_if_matched_number(game):
    game.question = "123"
    assert_matched_number(result=game.guess("123"), solved=True, strikes=3, balls=0)

def test_return_solved_result_if_unmatched_number(game):
    game.question = "123"
    assert_matched_number(result=game.guess("456"),solved=False,strikes=0,balls=0)

def test_return_solved_result_case1(game):
    game.question = "123"
    assert_matched_number(result=game.guess("125"),solved=False,strikes=2,balls=0)

def test_return_solved_result_case2(game):
    game.question = "123"
    assert_matched_number(result=game.guess("132"),solved=False,strikes=1,balls=2)
