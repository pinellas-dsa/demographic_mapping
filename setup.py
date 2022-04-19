"""Setup script for Saint Pete Housing package."""
import os

from setuptools import find_packages
from setuptools import setup


setup(
    name="pinallas_maps",
    version="0.0.1",
    description="Demographic research.",
    author="James Trimarco",
    author_email="james.trimarco@gmail.com",
    install_requires=[],
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)