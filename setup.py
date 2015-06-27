#!/usr/bin/env python
# Generated by jaraco.develop 2.18
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.txt', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []

setup_params = dict(
	name='chucknorris',
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description="chucknorris",
	long_description=long_description,
	url="https://bitbucket.org/jaraco/chucknorris",
	packages=setuptools.find_packages(),
	include_package_data=True,
	install_requires=[
	],
	setup_requires=[
		'setuptools_scm',
	] + pytest_runner + sphinx,
	tests_require=[
		'pytest',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points={
	},
)
if __name__ == '__main__':
	setuptools.setup(**setup_params)
