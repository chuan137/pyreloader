import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyreloader",
    version = "0.1.4",
    author = "Chuan Miao",
    author_email = "chuan137@gmail.com",
    description = ("Reload a python program on kill signal."),
    license = "MIT",
    keywords = "reload server",
    url = "https://github.com/chuan137/pyreloader",
    py_modules=['pyreloader'],
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
    entry_points={'console_scripts': [
        'pyreloader = pyreloader:main',
    ]},
)
