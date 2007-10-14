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
    >>> tempdir = tmpdir('tmp')

Let's create a buildout to build and install the package.

    >>> write('buildout.cfg',
    ... """
    ... [buildout]
    ... parts = config-package
    ...
    ... [config-package]
    ... recipe = bopen.recipe.libinc
    ... config-commands =
    ...     %(testdata)s/sample-config --libs
    ...     %(testdata)s/sample-config --cflags
    ... """ % {'testdata': testdata, 'tempdir': tempdir})

This will download, extract and build our demo package with the
default build options.

    >>> print system(buildout)
    Installing config-package.
    config-package: .../testdata/sample-config --libs -> -L/usr/lib -lsample
    config-package: .../testdata/sample-config --cflags -> -I/usr/include
    config-package: 
            include_dirs: ['/usr/include']
            library_dirs: ['/usr/lib']
            libraries: ['sample']
            cflags: -I/usr/include
            ldflags: -L/usr/lib -lsample

