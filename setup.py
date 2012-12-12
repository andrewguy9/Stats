from distutils.core import setup

setup(
    name='Stats',
    version='0.1.0',
    author='Andrew Thomson',
    author_email='athomsonguy@gmail.com',
    packages=['stats', 'stats.test'],
    scripts=['bin/sample'],
    url='http://pypi.python.org/pypi/Stats/',
    license='LICENSE.txt',
    description='Tools for capturing samples and counts',
    long_description=open('README.txt').read(),
    install_requires=[
    ],
)
