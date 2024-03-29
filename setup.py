from setuptools import find_packages
from setuptools import setup

setup(
    name='RssReaderGX',
    version='0.4.0',
    author='Pavel Martysiuk',
    author_email='martys388@gmail.com',
    description='Cmd utility',
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    python_requires='>=3.7',
    install_requires=['requests>=2.20.0', 'lxml == 4.4.0', 'beautifulsoup4>=4.7.0'],
    entry_points={'console_scripts': ['rss-reader = scripts.rss_reader:main']}
)
