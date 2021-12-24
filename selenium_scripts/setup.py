from setuptools import setup, find_packages

setup(name='selenium_scripts', version='1.0', packages=find_packages(),
    install_requires=[
        "async-generator==1.10",
        "attrs==21.2.0",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "cryptography==36.0.1",
        "h11==0.12.0",
        "idna==3.3",
        "importlib-metadata==4.10.0",
        "iniconfig==1.1.1",
        "outcome==1.1.0",
        "packaging==21.3",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pycparser==2.21",
        "pyopenssl==21.0.0",
        "pyparsing==3.0.6",
        "pytest==6.2.5",
        "selenium==4.1.0",
        "six==1.16.0",
        "sniffio==1.2.0",
        "sortedcontainers==2.4.0",
        "toml==0.10.2",
        "trio-websocket==0.9.2",
        "trio==0.19.0",
        "typing-extensions==4.0.1",
        "urllib3[secure]==1.26.7",
        "wsproto==1.0.0",
        "zipp==3.6.0"
    ])