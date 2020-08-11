import os
import setuptools

source_path = os.path.dirname(os.path.abspath(__file__))

with open(r"%s\README.md" % source_path, "r") as header:
	long_description = header.read()

setuptools.setup(
	name="typeconstructor",
	version="0.2",
	author="Ben Rutan",
	author_email="brutan.github@gmail.com",
	description="Singleton used to dynamically construct objects based upon type if modules have been imported.",
	long_description=long_description,
	url="https://github.com/BRutan/typeconstructor",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
	
	