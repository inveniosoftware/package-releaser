import re
# Compiled regular expression pattern
RE_DEV_STATUS = re.compile(r"(.*)('Development Status ::.*')(.*)")

# Constants
TROVE_DEV_STATUS = "Development Status :: 5 - Production/Stable"

def filter_text(text, fn):
    return '\n'.join(filter(fn, text.split('\n')))

def map_text(text, fn):
    return '\n'.join(map(fn, text.split('\n')))

def remove_setup_py_pypi_classifier(text):
    def pypy_trove(line):
        return 'Implementation :: PyPy' not in line
    return filter_text(text, pypy_trove)

def update_setup_py_development_status(text):
    def dev_status(line):
        m = re.match(RE_DEV_STATUS, line)
        if m:
            pref, cls, suff = m.groups()
            return pref + "'{}'".format(TROVE_DEV_STATUS) + suff
        else:
            return line
    return map_text(text, dev_status)


def update_setup_py_pypi_classifiers(text):
    functs = [
        remove_setup_py_pypi_classifier,
        update_setup_py_development_status,
    ]
    for fn in functs:
        text = fn(text)
    return text

