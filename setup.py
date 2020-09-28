from setuptools import setup
from setuptools import find_packages

setup(
    name="package_info",
    use_scm_version=True,
    setup_requires=[
        "setuptools_scm",
    ],
    description="Get PKG-INFO metadata as JSON",
    author="Joseph Hunkeler",
    author_email="jhunk@stsci.edu",
    license="BSD",
    project_urls={
        "Source": "https://github.com/astroconda/package_info",
    },
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "package_info=package_info.cli.__main__:main",
        ],
    },
)
