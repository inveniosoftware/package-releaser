from utils import update_setup_py_pypi_classifiers
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
        'Development Status :: 5 - Production/Stable',"""
    assert update_setup_py_pypi_classifiers(text1) == exp_text1
    assert update_setup_py_pypi_classifiers(exp_text1) == exp_text1
