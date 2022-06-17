import setuptools
from io import open
from os import path

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent


def strip_and_chop(s) -> str:
    t_str = s.strip()
    # local pip install have "--install options" which messes up this
    #  dependency list, so chop out "--install-options" or any other -- flags
    loc = t_str.find('--')
    if loc > 0:
        t_str = t_str[:loc].strip()
    return t_str


# automatically captured required modules for
# install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [strip_and_chop(x) for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-')) and x != '']
# dependency_links = [x.strip().replace('git+', '') for x in all_reqs \
#                     if 'git+' not in x]

setuptools.setup(
    name="paper_cli",
    version='0.0.1',
    author="Tyler McMaster",
    description="Proof of Concept for Papermill",
    packages=setuptools.find_namespace_packages("paper_cli"),
    include_package_data=True,
    package_dir={"": "paper_cli"},
    install_requires=install_requires,
    package_data={"paper_cli": ["py.typed"]},
    provides=['paper_cli'],
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'paper = scripts.app_cli:cli',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: UNLICENSED",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
