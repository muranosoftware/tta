from os import path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _read(fname):
    try:
        return open(path.join(path.dirname(__file__), fname)).read()
    except IOError:
        return ''


def load_requirements(file_name):
    requirements_list = []
    for l in _read(file_name).split('\n'):
        if l and not l.startswith('#'):
            if l.startswith('-r'):
                requirements_list.extend(load_requirements(l[3:]))
            else:
                requirements_list.append(l)
    return requirements_list


requirements = load_requirements('requirements.txt')

setup(
    name="tta",
    version="0.1.7",
    url="https://github.com/erm0l0v/tta",

    author="Kirill Ermolov",
    author_email="erm0l0v@ya.ru",

    description="Time Tracker Autocompleter for Muranosoft",
    long_description=open('README.rst').read(),

    packages=['tta'],

    install_requires=requirements,

    entry_points={
        'console_scripts': [
            'tta = tta.__main__:main',
        ]
    },

    keywords='Time Tracker, Autocomplete, Muranosoft',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],

    test_suite='tests',
)
