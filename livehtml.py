#!/usr/bin/env python
import os
import sys
import shlex
import subprocess
from livereload import Server


import errno


def shell(cmd):
    """Execute a shell command.

    You can add a shell command::

        server.watch(
            'style.less', shell('lessc style.less', output='style.css')
        )

    :param cmd: a shell command, string or list
    :param output: output stdout to the given file
    :param mode: only works with output, mode ``w`` means write,
                 mode ``a`` means append
    :param cwd: set working directory before command is executed.
    :param shell: if true, on Unix the executable argument specifies a
                  replacement shell for the default ``/bin/sh``.
    """

    def run_shell():
        ret = subprocess.run(args=cmd, shell=True, capture_output=False)

    return run_shell

server = Server()

if len(sys.argv) == 1:
    arg = 'html'
elif len(sys.argv) > 1:
    arg = sys.argv[1]

server.watch('docs/**/*.rst', shell('make {}'.format(arg)))
server.serve(root='build/sphinx/html')
