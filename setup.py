from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(
    name='zarnevis',
    version='0.0.1', 
    author='Muhammadreza Haghiri',
    author_email='<haghiri75@gmail.com>',
    url='https://github.com/prp-e/zarnevis',
    license='MIT',
    description='Zarnevis, a tool for writing RTL text in computer vision projects',
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['numpy', 'pillow', 'arabic-reshaper', 'python-bidi'],
    keywords = ['persian', 'arabic', 'rtl', 'text', 'cv', 'computer-vision'],
    classifiers = ["Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",]
)