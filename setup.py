from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in barcode/__init__.py
from barcode import __version__ as version

setup(
	name="barcode",
	version=version,
	description="Barcode",
	author="Matiyas Solution",
	author_email="revasiya.h786@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
