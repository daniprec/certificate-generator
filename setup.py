import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="certifigen",
    use_scm_version=False,
    author="Daniel Precioso",
    description="Python package to generate certificates of assistance",
    long_description=long_description,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    setup_requires=["setuptools_scm"],
    install_requires=["black", "PyPDF2", "pandas", "pip-tools", "toml", "typer"],
)
