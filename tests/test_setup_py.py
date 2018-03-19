from utils import remove_setup_py_pypi_classifier
from textwrap import dedent

def test_pypy_classifier():
    text1 = """\
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 4 - Beta',"""

    exp_text1 = """\
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 4 - Beta',"""
    assert remove_setup_py_pypi_classifier(text1) == exp_text1
    assert remove_setup_py_pypi_classifier(exp_text1) == exp_text1

