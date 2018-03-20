from textwrap import dedent
from utils import remove_pypy_from_travis_yml


def test_remove_pypy_from_travis_yml():
    text1 = dedent("""python:
      - "3.4"
      - "3.3"
      - "2.7"
      - "2.6"
      - "pypy"

    matrix:
      fast_finish: true
      allow_failures:
        - python: pypy

    before_install:
    """)

    expected1 = dedent("""python:
     - "3.4"
     - "3.3"
     - "2.7"
     - "2.6"

    matrix:
      fast_finish: true
      allow_failures:
        - python: pypy

    before_install:
    """)

    assert remove_pypy_from_travis_yml(text1) == expected1
