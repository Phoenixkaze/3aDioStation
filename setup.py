import setuptools

with open("README-EN.md") as rm:
    long_description = rm.read()

setuptools.setup(
    name="threadiostaion",
    version="1.0.0",
    author="GarliCat",
    author_email="phoenixkaze@live.com",
    description="3DS FBI remote install tool with GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Phoenixkaze/3aDioStation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)”,
        "Operating System :: OS Independent",
    ],
)