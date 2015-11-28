from setuptools import setup, find_packages


setup(
    name='choral',
    versions='1.0a0dev',
    description='Choral is a Desktop podcast app',
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
    ]
)
