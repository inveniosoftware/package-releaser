import pytest
import os

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

@pytest.fixture()
def example_contents():
    filenames = [
    ]
    # Load all files contents
    contents = []
    dpath = os.path.join(os.path.dirname(__file__), 'data')
    for in_fn, out_fn in filenames:
        filetype = in_fn.split('_')[0]
        with open(os.path.join(dpath, in_fn), 'r') as fp:
            in_cnt = fp.read()
        with open(os.path.join(dpath, out_fn), 'r') as fp:
            out_cnt = fp.read()
        contents.append((filetype, in_fn, in_cnt, out_cnt))
    return contents

