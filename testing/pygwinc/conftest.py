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
used by wield.
"""

import pytest
import os
import wield.pytest
from wield.pytest.fixtures import (  # noqa
    capture,
    tjoin,
    plot,
    tpath_preclear,
    tpath,
    tjoin,
    fpath,
    fjoin,
    closefigs,
    test_trigger,
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

