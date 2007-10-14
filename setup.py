from setuptools import setup, find_packages

version = '0.1'
name = 'bopen.recipe.libinc'

setup(name='bopen.recipe.libinc',
      version=version,
      description="",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Buildout",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='development buildout recipe',
      author='Alessandro Amici',
      author_email='a.amici@bopen.it',
      url='http://pypi.python.org/pypi/bopen.recipe.libinc',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bopen.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zc.buildout',
      ],
      tests_require = ['zope.testing'],
      test_suite = '%s.tests.test_suite' % name,
      entry_points={
        'zc.buildout' : ['default = %s:Recipe' % name],
      },
      )
