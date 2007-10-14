Supported options
=================

config-commnads
    a list of commands that return the linking options, one per line

Example usage
=============


We'll use a simple config command to demonstrate the recipe.

    >>> import os.path
    >>> testdata = join(os.path.dirname(__file__), 'testdata')
    >>> ls(testdata)
    d .svn
    - sample-config

The options are accessible by other recipes:

    >>> mkdir(sample_buildout, 'recipes')
    >>> write(sample_buildout, 'recipes', 'echo.py',
    ... """
    ... import logging
    ...
    ... class Echo:
    ...
    ...     def __init__(self, buildout, name, options):
    ...         self.name, self.options = name, options
    ...
    ...     def install(self):
    ...         log = logging.getLogger(self.name)
    ...         log.info(self.options.get('echo', ''))
    ...         return ()
    ...
    ...     def update(self):
    ...         pass
    ... """)

    >>> write(sample_buildout, 'recipes', 'setup.py',
    ... """
    ... from setuptools import setup
    ...
    ... setup(
    ...     name = "recipes",
    ...     entry_points = {'zc.buildout': ['echo= echo:Echo']},
    ...     )
    ... """)

Let's create a buildout to build and install the package.

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... develop = recipes
    ... parts = package
    ...
    ... [package]
    ... recipe = recipes:echo
    ... echo =
    ...     include_dirs: ${config-package:include_dirs}
    ...     library_dirs: ${config-package:library_dirs}
    ...     libraries: ${config-package:libraries}
    ...     cflags: ${config-package:cflags}
    ...     ldflags: ${config-package:ldflags}
    ...
    ... [config-package]
    ... recipe = bopen.recipe.libinc
    ... config-commands =
    ...     %(testdata)s/sample-config --cflags
    ...     %(testdata)s/sample-config --libs
    ...     %(testdata)s/sample-config --version
    ... """ % {'testdata': testdata})

This will download, extract and build our demo package with the
default build options.

    >>> print system(buildout)
    Develop: ...
    config-package: .../testdata/sample-config --cflags -> -I/usr/include -I/usr/include/sample
    config-package: .../testdata/sample-config --libs -> -L/usr/lib -L/usr/lib/sample -lsample -lsample_rt
    config-package: .../testdata/sample-config --version -> 1.0
    config-package: 
            include_dirs: ['/usr/include', '/usr/include/sample']
            library_dirs: ['/usr/lib', '/usr/lib/sample']
            libraries: ['sample', 'sample_rt']
            cflags: -I/usr/include -I/usr/include/sample
            ldflags: -L/usr/lib -L/usr/lib/sample -lsample -lsample_rt
    Installing config-package.
    Installing package.
    package: 
        include_dirs: ['/usr/include', '/usr/include/sample']
        library_dirs: ['/usr/lib', '/usr/lib/sample']
        libraries: ['sample', 'sample_rt']
        cflags: -I/usr/include -I/usr/include/sample
        ldflags: -L/usr/lib -L/usr/lib/sample -lsample -lsample_rt

