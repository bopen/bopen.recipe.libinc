from setuptools import setup, find_packages

version = '0.1'

setup(name='bopen.recipe.libinc',
      version=version,
      description="",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Alessandro Amici',
      author_email='',
      url='http://pypi.python.org/pypi/bopen.recipe.libinc',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['bopen.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
