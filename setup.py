from setuptools import setup, find_packages

this_directory =  Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="polymarket-arbitrage-bot",
    version="0.1.0",
    long_description=long_description,                                     
    long_description_content_type="text/markdown",  
    url="https://github.com/P-x-J/Polymarket-Arbitrage-Bot",
    packages=find_packages(),                     
    install_requires=[
        "requests", "web3", #etc
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)

