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

    for objnode in doctree.traverse(addnodes.desc):
        domain = objnode.get('domain')
        uris: Set[str] = set()
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
            name, uri = resolve_ws_target(domain, info)
            if not uri:
                # no source
                continue

            # removing this to have more links
            if uri in uris or not uri:
                # only one link per name, please
                # continue
                pass
            uris.add(uri)

            inline = nodes.inline('', _('[{}]'.format(name)), classes=['viewcode-link'])
            onlynode = addnodes.only(expr='html')
            onlynode += nodes.reference('', '', inline, internal=False, refuri=uri)
            signode += onlynode


def setup(app: Sphinx) -> Dict[str, Any]:
    app.connect('doctree-read', doctree_read)
    app.add_config_value('linkcode_ws_resolve', None, '')
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
