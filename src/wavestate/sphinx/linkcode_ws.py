"""
    sphinx.ext.linkcode
    ~~~~~~~~~~~~~~~~~~~

    Add external links to module code in Python object descriptions.

    :copyright: Copyright 2007-2021 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.

    modified for wavestate to allow configuration of the [source] link by
    changing linkcode_resolve to output both a name, uri pair. It is
    assigned to the linkcode_ws_resolve configuration parameter.
"""

import os
from typing import Any, Dict, Set

from docutils import nodes
from docutils.nodes import Node

import sphinx
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.errors import SphinxError
from sphinx.locale import _


class LinkcodeError(SphinxError):
    category = "linkcode error"



def doctree_read(app: Sphinx, doctree: Node) -> None:
    env = app.builder.env

    resolve_ws_target = getattr(env.config, 'linkcode_ws_resolve', None)
    if not callable(env.config.linkcode_ws_resolve):
        raise LinkcodeError(
            "Function `linkcode_resolve` is not given in conf.py")

    domain_keys = {
        'py': ['module', 'fullname'],
        'c': ['names'],
        'cpp': ['names'],
        'js': ['object', 'fullname'],
    }

    # the use of doctree[0].source is a bit of a hack
    # Sphinx does some transforms that clobber the source link
    # of the root document
    # luckily all children seem to keep theirs
    def get_relpath_root():
        srcpath, srcfile = os.path.split(doctree[0].source)
        source_path = os.path.relpath(srcpath, app.srcdir)
        source_path_inv_pre = os.path.relpath(app.srcdir, app.outdir)
        source_path_inv_src = os.path.relpath(source_path_inv_pre, source_path)
        source_path_inv_out = os.path.relpath('.', source_path)
        return source_path_inv_src, source_path_inv_out
    relpath_root = None
    # print(type(doctree), type(doctree.document))
    # print(doctree[0].source)

    for objnode in doctree.traverse(addnodes.desc):
        domain = objnode.get('domain')
        for signode in objnode:
            if not isinstance(signode, addnodes.desc_signature):
                continue

            # Convert signode to a specified format
            info = {}
            for key in domain_keys.get(domain, []):
                value = signode.get(key)
                if not value:
                    value = ''
                info[key] = value
            if not info:
                continue

            # Call user code to resolve the link
            map_name_uri = resolve_ws_target(domain, info)
            for name, uri in map_name_uri.items():
                internal = False
                if uri.startswith('/'):
                    if relpath_root is None:
                        relpath_root = get_relpath_root()
                    if uri.startswith('//'):
                        uri = os.path.join(relpath_root[0], uri[2:])
                        internal = True
                    else:
                        uri = os.path.join(relpath_root[1], uri[1:])
                        internal = True
                inline = nodes.inline('', _('[{}]'.format(name)), classes=['viewcode-link'])
                onlynode = addnodes.only(expr='html')
                onlynode += nodes.reference('', '', inline, internal=internal, refuri=uri)
                signode += onlynode


def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect('doctree-read', doctree_read)
    app.add_config_value('linkcode_ws_resolve', None, '')
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
