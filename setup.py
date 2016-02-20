from setuptools import setup, find_packages
from choral import __version__, __author__, __author_email__, __main_url__, __license__

long_description = open('README.md').read()


setup(
    name='choral',
    version=__version__,

    # Packaging
    packages=find_packages(),
    entry_points={
        'gui_scripts': ['choral = choral.main:start']
    },
    install_requires=['colorlog==2.6.1', 'python-magic==0.4.10'],
    include_package_data=True,
    zip_safe=False,

    # Package metadata
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    description=long_description.split('\n')[0],
    long_description=long_description,
    url=__main_url__,
    keywords='podcast music radio gtk3 desktop',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Intended Audience :: End Users/Desktop',
        'Environment :: X11 Applications',
        'Environment :: X11 Applications :: Gnome',
        'Environment :: X11 Applications :: GTK',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Operating System :: POSIX :: Linux',

    ]
)
