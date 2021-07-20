from setuptools import setup, version 

with open('README.md') as f:
    long_description = f.read()

setup(
    name='zarnevis',
    version='0.0.1', 
    description='Zarnevis, a tool for writing RTL text in computer vision projects',
    long_description_content_type='text/markdown',
    long_description=long_description,
)