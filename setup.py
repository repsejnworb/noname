#!/usr/bin/env python
import noname.version

from setuptools import setup, find_packages

setup(
    name='noname',
    version=noname.version.__version__,
    description="None yet",
    author="Repsej Nworb",
    author_email="repsejnworb@gmail.com",
    license="Proprietary",
    url="http://meatspin.com",
    packages=find_packages(),
    package_data={'noname': ['resources']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "noname = noname.main:main",
        ]
    },
)
