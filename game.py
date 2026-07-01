from game_result import GameResult


class Game:

    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("cannot read question")

    @question.setter
    def question(self, question):
        self._question = question

    def _is_duplicated_numbers(self, guess_number: str):
        return guess_number[0] == guess_number[1] or guess_number[0] == guess_number[2] or guess_number[1] == guess_number[2]

    def _assert_invalidate_values(self, guess_number):

        if guess_number is None:
            raise TypeError("입력이 None 입니다")

        if len(guess_number) != 3:
            raise TypeError("입력은 3자리 문자열입니다")

        if not guess_number.isdigit():
            raise TypeError("입력은 숫자 문자열만 가능합니다")

        if self._is_duplicated_numbers(guess_number):
            raise TypeError("중복된 숫자가 존재합니다")

    def guess(self, guess_number):
        self._assert_invalidate_values(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        else:
            _strike = 0
            _ball = 0

            for idx, digit in enumerate(guess_number):
                if digit == self._question[idx]:
                    _strike += 1
                elif digit in self._question:
                    _ball += 1

            return GameResult(False, _strike, _ball)
