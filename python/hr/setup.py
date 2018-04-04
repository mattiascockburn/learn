from setuptools import setup, find_packages
with open('README.rst') as f:
    readme = f.read()

setup(
    name="hr",
    version="0.1.0",
	packages=find_packages('src'),
	package_dir={'': 'src'},
    entry_points={
        'console_scripts': 'hr=hr.cli:main',
    },


    # metadata for upload to PyPI
    author="Mattias Giese",
    author_email="foobar@example.com,",
    description="This package manages users through a JSON inventory file",
    license="MIT",
    long_description=readme,
    #keywords="hello world example examples",
    #url="http://example.com/HelloWorld/",   # project home page, if any
    #project_urls={
    #    "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #    "Documentation": "https://docs.example.com/HelloWorld/",
    #    "Source Code": "https://code.example.com/HelloWorld/",
    #}

    # could also include long_description, download_url, classifiers, etc.
)
