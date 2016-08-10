import io
from setuptools import setup

with io.open('README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='zenbot',
    version='0.1.4',
    url='https://github.com/underyx/zenbot',
    author='Bence Nagy',
    author_email='bence@underyx.me',
    download_url='https://github.com/underyx/zenbot/releases',
    long_description=README,
    packages=['zenbot'],
    install_requires=[
        'aiohttp',
        'gunicorn',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
    ]
)
