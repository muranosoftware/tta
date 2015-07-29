import setuptools
from os import path


def _read(fname):
    try:
        return open(path.join(path.dirname(__file__), fname)).read()
    except IOError:
        return ''


def load_requirements(file_name):
    requirements = []
    for l in _read(file_name).split('\n'):
        if l and not l.startswith('#'):
            if l.startswith('-r'):
                requirements.extend(load_requirements(l[3:]))
            else:
                requirements.append(l)
    return requirements


requirements = load_requirements('requirements.txt')


setuptools.setup(
    name="tta",
    version="0.1.2",
    url="https://github.com/erm0l0v/tta",

    author="Kirill Ermolov",
    author_email="erm0l0v@ya.ru",

    description="Time Tracker Autocompleter for Muranosoft",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(exclude=['*.tests', 'tests']),

    install_requires=requirements,

    scripts=['tta/tta.py'],

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
