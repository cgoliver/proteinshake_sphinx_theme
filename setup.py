import os
import os.path as osp
import re
from setuptools import find_packages, setup
from typing import List, Optional

__version__ = '0.1.0'


def package_files(
    root: str,
    whitelist: Optional[List[str]] = None,
) -> List[str]:
    pattern = f'.({"|".join(whitelist or [])})$'

    paths: List[str] = []
    for path, _, names in os.walk(root):
        for name in names:
            if whitelist is not None and not re.search(pattern, name):
                continue
            paths.append(osp.join('..', path, name))
    return paths


print(package_files('pyg_sphinx_theme/static'))

setup(
    name='pyg_sphinx_theme',
    version=__version__,
    author='PyG Team',
    author_email='team@pyg.org',
    url='https://github.com/pyg-team/pyg_sphinx_theme',
    install_requires=[
        'sphinx>=4.0',
        'sphinx_rtd_theme>=1.0',
    ],
    package_data={
        'pyg_sphinx_theme': [
            'theme.conf',
            *package_files('pyg_sphinx_theme/static', ['css', 'png', 'svg']),
        ]
    },
    entry_points={
        'sphinx.html_themes': [
            'pyg_sphinx_theme = pyg_sphinx_theme',
        ]
    },
    packages=find_packages(),
    include_package_data=True,
)
