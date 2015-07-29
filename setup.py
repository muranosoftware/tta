import setuptools

setuptools.setup(
    name="tta",
    version="0.1.0",
    url="https://github.com/erm0l0v/tta",

    author="Kirill Ermolov",
    author_email="erm0l0v@ya.ru",

    description="Time Tracker Autocompleter for Muranosoft",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
