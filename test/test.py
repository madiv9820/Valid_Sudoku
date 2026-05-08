"""🧭 This test file turns each JSON case into its own unittest so every
scenario gets clear pass/fail reporting, plus a small timeout guard.

Instead of putting all cases inside one big `test()` loop, we generate
one real test method per case. That way, `unittest` can show exactly
which scenario passed or failed in verbose mode. """

import json
import os
import time
import unittest
from typing import List
from timeout_decorator import TimeoutError, timeout
from source.solution import Solution


def _to_test_name(title: str) -> str:
    # 🏷️ Convert each friendly title into a safe unittest method name.
    # `unittest` expects names like `test_something`, so we clean the title
    # and turn spaces / emojis / punctuation into underscores.
    sanitized = ''.join(char.lower() if char.isalnum() else '_' for char in title)
    compact = '_'.join(part for part in sanitized.split('_') if part)
    return f'test_{compact}'


def _format_board(board: List[List[str]]) -> str:
    horizontal_border = '+-------+-------+-------+'
    lines = [horizontal_border]

    for rowIndex, row in enumerate(board):
        if rowIndex and rowIndex % 3 == 0:
            lines.append(horizontal_border)

        chunks = [' '.join(row[start:start + 3]) for start in range(0, 9, 3)]
        lines.append(f'| {" | ".join(chunks)} |')

    lines.append(horizontal_border)

    return '\n'.join(lines)


def _make_testcase(testcase):
    # 🧱 Build one real unittest method per JSON case for better test output.
    # This function returns another function, which becomes an actual test
    # method on `TestSolution`.
    def test_method(self):
        title: str = testcase['title']
        board: List[List[str]] = testcase['input']['board']
        expectedOutput: bool = testcase['output']
        description: str = testcase.get('description', 'No description provided.')

        # 🎬 Print a small intro card before each testcase begins.
        print('\n' + '=' * 60)
        print(f'🧪 Test Case : {title}')
        print(f'📝 Scenario  : {description}')
        print('🧩 Board     :')
        print(_format_board(board))
        print('⏳ Starting soon...')
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        try:
            # ▶️ Run the solution for this specific case under the timeout guard.
            actualOutput: bool = self._run_case(board=board)
        except TimeoutError:
            # ⏱️ Turn timeout exceptions into normal unittest failures.
            print(f'⏱️ Result    : Time Limit Exceeded in {title}')
            print('=' * 60)
            self.fail(f'⏱️ Time Limit Exceeded: {title}')

        # ✅ A passing case shows up naturally in verbose unittest output.
        # If values differ, unittest prints the custom message below.
        if actualOutput == expectedOutput:
            print(f'✅ Result    : Passed with answer {actualOutput}')
        else:
            print(f'❌ Result    : Expected {expectedOutput}, got {actualOutput}')

        print('=' * 60)
        # 💤 Pause between tests so the output feels paced and readable.
        time.sleep(self.DISPLAY_DELAY_SECONDS)

        self.assertEqual(
            actualOutput,
            expectedOutput,
            f'❌ Value Mismatch in {title}\n'
            f'Expected = {expectedOutput}\n'
            f'Actual   = {actualOutput}'
        )

    return test_method


class TestSolution(unittest.TestCase):
    # 🎛️ Tweak this to make the test run faster or more cinematic.
    DISPLAY_DELAY_SECONDS = 2

    def setUp(self):
        # 🛠️ Each test gets a fresh solution instance to keep runs predictable.
        # This avoids one testcase accidentally affecting another.
        self.__solution = Solution()
        return super().setUp()

    @timeout(1)
    def _run_case(self, board: List[List[str]]) -> bool:
        # ⚡ Give every testcase its own timeout instead of timing the whole file.
        # If one case is too slow, only that case fails.
        return self.__solution.isValidSudoku(board=board)


_CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
_FILE_PATH = os.path.join(_CURRENT_DIRECTORY, 'cases.json')


with open(_FILE_PATH, mode='r', encoding='utf-8') as readFile:
    # 🧪 Register every case as a standalone test so verbose mode is meaningful.
    # `setattr(...)` adds methods like `test_classic_valid_board`
    # directly onto the `TestSolution` class before the test runner starts.
    for testcase in json.load(readFile):
        setattr(TestSolution, _to_test_name(testcase['title']), _make_testcase(testcase))


if __name__ == '__main__':
    # ▶️ Verbose mode shows each generated testcase as it passes or fails.
    unittest.main(verbosity=2)
