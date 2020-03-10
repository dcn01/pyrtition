from setuptools import setup, find_packages


setup(
    name="pyrtition",
    version="1.0",
    packages=find_packages(exclude="tests"),
    license='MIT',
    author='Jeremy Carter',
    author_email='jeremychild@gmail.com',
    python_requires='>=3.6',
)