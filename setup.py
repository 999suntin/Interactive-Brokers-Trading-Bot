from distutils.core import setup
from setuptools import setup, find_packages


# with open("README.md", "r") as fh:
#    long_description = fh.read()

setup(

    # Library Name.
    name='IB_Trading_Bot',

    # Want to make sure people know who made it.
    author='Vincent Ho, Alex Reed',

    # also an email they can use to reach out.
    author_email='coding.sigma@gmail.com',

    # read this as MAJOR VERSION 0, MINOR VERSION 1, MAINTENANCE VERSION 0
    version='0.1.0',
    description='A python client library for the Interactive Broker Web API.',

    # I have a long description but that will just be my README file.
    long_description="A Python library written to handle IB's Client Portal API, manage portfolio and execute trades.",

    # want to make sure that I specify the long description as MARKDOWN.
    long_description_content_type="text/markdown",

    # here is the URL you can find the code.
    url='https://github.com/Vincentho711/Interactive-Brokers-Trading-Bot',

    # there are some dependencies to use the library, so let's list them out.
    install_requires=[
        'certifi>=2019.11.28',
        'requests>=2.22.0',
        'urllib3>=1.25.3'
    ],

    # here are the packages I want "build."
    packages=find_packages(include=['ibw']),

    # additional classifiers that give some characteristics about the package.
    classifiers=[

        # I want people to know it's still early stages.
        'Development Status :: 3 - Alpha',

        # My Intended audience is mostly those who understand finance.
        'Intended Audience :: Financial and Insurance Industry',

        # My License is MIT.
        'License :: OSI Approved :: MIT License',

        # I wrote the client in English
        'Natural Language :: English',

        # The client should work on all OS.
        'Operating System :: OS Independent',

        # The client is intendend for PYTHON 3
        'Programming Language :: Python :: 3'
    ],

    # you will need python 3.7 to use this libary.
    python_requires='>3.7'
)






