import os
import setuptools

dir_path = os.path.dirname(os.path.realpath(__file__))

with open("%s//README.md" % dir_path, "r") as header:
	long_description = header.read()

setuptools.setup(
	name="typeconstructor",
	version="0.1",
	author="Ben Rutan",
	author_email="brutan.github@gmail.com",
	description="Singleton used to dynamically construct objects based upon type.",
	long_description=long_description,
	url="https://github.com/BRutan/TypeConstructor",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
	
	