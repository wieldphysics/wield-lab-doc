#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2022 California Institute of Technology.
# SPDX-FileCopyrightText: © 2022 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
"""
import numpy as np
import pytest


from wield.pytest.fixtures import (  # noqa: F401
    tpath_join,
    dprint,
    fpath_join,
    tpath,
    # ws_tracemalloc_auto,  # if imported, will report after each test
)

import ws_parse_cov_html


def test_ws_doc_parse_cov_html(tpath_join, fpath_join, dprint):
    html_file = fpath_join('./index.html')
    d = ws_parse_cov_html.parse_cov_index(html_file)
    dprint(d)
