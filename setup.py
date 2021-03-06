import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="istart",
    version="0.0.1",
    author="Atulya Narayan",
    author_email="atulya.iims@gmail.com",
    description="Kick start data science package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atulyanarayan/istart",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
