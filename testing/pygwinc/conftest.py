#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2022 California Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2022 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
This conftest is a stub to replace the fixtures in gwinc's conftest with those
used by wavestate.
"""

import pytest
import os
import wavestate.pytest
from wavestate.pytest.fixtures import (  # noqa
    capture,
    tpath_join,
    plot,
    tpath_preclear,
    tpath,
    tpath_join,
    fpath,
    fpath_join,
    closefigs,
    test_trigger,
    dprint,
)


@pytest.fixture()
def ic():
    """
    Fixture to provide icecream imports without requiring that the package exist
    """
    try:
        from icecream import ic
        return ic
    except ImportError:
        pass
    try:
        from IPython.lib.pretty import pprint
        return pprint
    except ImportError:
        from pprint import pprint
        return pprint


#these are used with the pprint fixture
try:
    import icecream
except ImportError:
    icecream = None
    pass
try:
    from IPython.lib.pretty import pprint, pretty
    pformat = pretty
except ImportError:
    from pprint import pprint, pformat


pprint = dprint
