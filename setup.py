from setuptools import setup, find_packages

setup(
    name="hfcrypt",
    description="Host encrypted apps on Hugging Face Spaces",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    version="2.1.0",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        "console_scripts": [
            "hfcrypt=hfcrypt.cli:app",
        ],
    },
)
