import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "reloader",
    version = "0.1",
    author = "Chuan Miao",
    author_email = "chuan137@gmail.com",
    description = ("Reload a program on signal HUP."),
    license = "MIT",
    keywords = "reload server",
    url = "https://github.com/chuan137/reloader",
    py_modules=['reloader'],
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    entry_points={'console_scripts': [
        'reloader = reloader:main',
    ]},
)
