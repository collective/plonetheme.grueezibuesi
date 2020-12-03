# -*- coding: utf-8 -*-
"""Installer for the plonetheme.gruezibuesi package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='plonetheme.gruezibuesi',
    version='1.0a1',
    description="A kitten inspired Plone Theme",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone CMS',
    author='Peter Holzer',
    author_email='peter.holzer@agitator.com',
    url='https://github.com/collective/plonetheme.gruezibuesi',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/plonetheme.gruezibuesi',
        'Source': 'https://github.com/collective/plonetheme.gruezibuesi',
        'Tracker': 'https://github.com/collective/plonetheme.gruezibuesi/issues',
        # 'Documentation': 'https://plonetheme.gruezibuesi.readthedocs.io/en/latest/',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['plonetheme'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'plone.app.themingplugins',
        'collective.themefragments',
        'z3c.jbot',
        'Products.GenericSetup>=1.8.2',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.app.dexterity',
        'plone.app.referenceablebehavior',
        'plone.app.relationfield',
        'plone.app.lockingbehavior',
        'plone.schema',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing>=5.0.0',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = plonetheme.gruezibuesi.locales.update:update_locale
    """,
)
