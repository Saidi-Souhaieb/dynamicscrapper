from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='dynamicscrapper',
    version='5.3.8',
    author='Saidi Souhaieb',
    author_email='Saidisouhaieb@takiacademyteam.com',
    description='A package to scrap the web dynamically',
    long_description_content_type='text/markdown',
    long_description=readme,
    packages=find_packages(include=['selenium', 'click']),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
