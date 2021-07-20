from setuptools import setup, version 

with open('README.md') as f:
    long_description = f.read()

setup(
    name='zarnevis',
    version='0.0.1', 
    author='Muhammadreza Haghiri',
    author_email='haghiri75@gmail.com',
    url='https://github.com/prp-e/zarnevis',
    description='Zarnevis, a tool for writing RTL text in computer vision projects',
    long_description_content_type='text/markdown',
    long_description=long_description,

)