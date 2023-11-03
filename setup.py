from setuptools import setup, find_packages

setup(
    name='dynamicscrapper',
    version='0.3.0',
    author='Saidi Souhaieb',
    author_email='Saidisouhaieb@takiacademyteam.com',
    description='A package to scrap the web dynamically',
    long_description="""# Markdown supported!\n\n* Cheer\n* Celebrate\n""",
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
