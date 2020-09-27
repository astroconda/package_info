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
    packages=find_packages(),
)
