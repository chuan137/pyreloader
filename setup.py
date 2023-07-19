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
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[],
    entry_points={'console_scripts': [
        'reloader = reloader:main',
    ]},
)
