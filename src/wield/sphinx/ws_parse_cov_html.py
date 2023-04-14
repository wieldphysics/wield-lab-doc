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


from wavestate.pytest.fixtures import (  # noqa: F401
    tpath_join,
    dprint,
    fpath_join,
    tpath,
    # ws_tracemalloc_auto,  # if imported, will report after each test
)

import html.parser


class CovHTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.d = {}
        self.link = None

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            attrs = dict(attrs)
            self.link = attrs['href']

    def handle_endtag(self, tag):
        if tag.lower() == 'a':
            self.link = None

    def handle_data(self, data):
        if self.link is not None:
            self.d[data] = self.link


def parse_cov_index(fname):
    p = CovHTMLParser()
    with open(fname, 'r') as F:
        p.feed(F.read())
    return p.d

def test_ws_doc_parse_cov_html(tpath_join, fpath_join, dprint):
    html_file = fpath_join('./index.html')
    d = parse_cov_index(html_file)
    dprint(d)
