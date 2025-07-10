from setuptools import setup, find_packages

setup(
    name='polymarket-arbitrage-bot',
    version='0.1.0',
    description='Scans Polymarket for arbitrage opportunities in both single-market (binary) and multi-market (categorical) events',
    author='P-x-J',
    url='https://github.com/P-x-J/Polymarket-Arbitrage-Bot',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Or your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
