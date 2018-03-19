TROVE_DEV_STATUS = " " * 8 + "Development Status :: 5 - Production/Stable"

def filter_text(text, fn):
    return '\n'.join(line for line in text.split('\n') if not fn(line))

def map_text(text, match_fn, map_fn):
    pass

def remove_setup_py_pypi_classifier(text):
    def pypy_fn(line):
        return 'Implementation :: PyPy' in line
    return filter_text(text, pypy_fn)

