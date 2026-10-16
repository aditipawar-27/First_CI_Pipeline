# First_CI_Pipeline

![Python CI](https://github.com/aditipawar-27/First_CI_Pipeline/actions/workflows/python-ci.yml/badge.svg)

A small Continuous Integration (CI) project. Ten Python programs (Programs 21 to 30), each with its own pytest test file. A GitHub Actions workflow runs every test automatically on each push.

## How the pipeline works

```
Write program + test -> pytest locally -> git add / commit / push
                                              |
                                              v
                         GitHub Actions starts (ubuntu-latest)
        1. Check out code   2. Set up Python 3.12
        3. pip install -r requirements.txt   4. pytest
                                              |
                          green tick = all pass / red cross = fix and push again
```

The workflow is defined in [`.github/workflows/python-ci.yml`](.github/workflows/python-ci.yml). It runs on every push and pull request to `main`.

## Programs

| No. | Program                           | Function                           | File                             |
| --- | --------------------------------- | ---------------------------------- | -------------------------------- |
| 21  | Largest word in a sentence        | `largest_word(sentence)`           | `codes/21_largest_word.py`       |
| 22  | Check anagram strings             | `is_anagram(first, second)`        | `codes/22_anagram_strings.py`    |
| 23  | Sort a list without `sort()`      | `bubble_sort(numbers)`             | `codes/23_sort_without_sort.py`  |
| 24  | Merge two sorted lists            | `merge_sorted_lists(list1, list2)` | `codes/24_merge_sorted_lists.py` |
| 25  | Maximum and minimum of a list     | `find_max_min(numbers)`            | `codes/25_max_min_list.py`       |
| 26  | Sum of a list without `sum()`     | `sum_of_list(numbers)`             | `codes/26_sum_of_list.py`        |
| 27  | Rotate a list by k positions      | `rotate_list(items, k)`            | `codes/27_rotate_list.py`        |
| 28  | Intersection of two sets          | `set_intersection(first, second)`  | `codes/28_set_intersection.py`   |
| 29  | Armstrong number check            | `is_armstrong(number)`             | `codes/29_armstrong_number.py`   |
| 30  | Decimal to binary without `bin()` | `decimal_to_binary(number)`        | `codes/30_decimal_to_binary.py`  |

Each program has a matching test file in `test_cases/` named `test_<number>_<name>.py`.

## Project structure

```
First_CI_Pipeline/
|-- .github/workflows/python-ci.yml   GitHub Actions workflow
|-- codes/                            the 10 programs
|-- test_cases/                       the 10 pytest test files
|-- .gitignore
|-- pytest.ini                        pythonpath = codes, testpaths = test_cases
|-- requirements.txt                  pytest
`-- README.md
```

## Run it locally

Requires Python 3.12 or newer and Git.

```bash
git clone https://github.com/YOUR-USERNAME/First_CI_Pipeline.git
cd First_CI_Pipeline

python -m venv .venv
# Windows (Command Prompt):  .venv\Scripts\activate
# Windows (PowerShell):      .venv\Scripts\Activate.ps1
# Mac / Linux / Git Bash:    source .venv/bin/activate

pip install -r requirements.txt
pytest -v
```

Run a single program, for example Program 21:

```bash
python codes/21_largest_word.py
```

Run a single test file:

```bash
pytest test_cases/test_21_largest_word.py
```

## Notes

- File names start with a number, so the tests load each program with `importlib.import_module("21_largest_word")` instead of a normal `import` statement.
- `pytest.ini` adds the `codes` folder to Python's search path so those imports work.
- Programs 23, 25, 26 and 30 avoid the built-ins they replace (`sort()`/`sorted()`, `max()`/`min()`, `sum()`, `bin()`).
