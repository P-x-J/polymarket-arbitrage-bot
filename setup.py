from setuptools import setup, find_packages

setup(
    name="polymarket-arbitrage-bot",
    version="0.1.0",
    description="A bot to detect and execute arbitrage opportunities on Polymarket",
    url="https://github.com/P-x-J/Polymarket-Arbitrage-Bot",
    packages=find_packages(where="src"),            # or find_packages() if top-level
    package_dir={"": "src"},                        # omit if not using src layout
    install_requires=[
        "requests", "web3",  # etc.
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

