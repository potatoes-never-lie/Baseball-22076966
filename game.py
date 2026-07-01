import random
import string

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

def play_game(correct_answer):

    game = Game()
    game.question = correct_answer
    print("=============게임을 시작합니다.===============\n")
    print("============단 10번의 기회만 주어집니다!!!!!!===========")
    cnt = 0
    is_solved: bool = False
    while cnt < 10:
        s = input("3자리 숫자를 써주세요.\n")
        try:
            result = game.guess(s)
            if result.solved:
                print("정답!!!!!!")
                is_solved = True
                break
            print("오답입니다 ..")
            print(result.__repr__())
        except TypeError as e:
            print(e.__str__())
            continue
        cnt += 1

    if not is_solved:
        print(f"정답은...{correct_answer} 이었습니다..")


if __name__ == "__main__":
    play_game("".join(random.choices(string.digits, k=3)))
