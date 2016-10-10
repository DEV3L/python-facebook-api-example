from setuptools import setup, find_packages

setup(
    name='facebook_api_example',
    packages=find_packages(),
    version='0.1',
    description='This program posts a hello world message to a Facebook page.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-facebook-api-example',
    download_url='https://github.com/DEV3L/python-facebook-api-example/tarball/0.1',
    keywords=['dev3l', 'facebook', 'graph'],  # arbitrary keywords
    install_requires=[
        'pytest',
        'facebook-sdk'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'facebook_api_example = facebook_api_example.main'
        ]},
)
