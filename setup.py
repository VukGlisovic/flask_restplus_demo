# https://packaging.python.org/tutorials/packaging-projects/
# Generate built distribution: python setup.py sdist bdist_wheel
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-restplus-demo",
    version="0.0.1",
    author="Vuk Glisovic",
    author_email="glisovicvuk@gmail.com",
    description="A package for keeping a groceries list.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VukGlisovic/flask_restplus_demo",
    packages=setuptools.find_packages(where='.', exclude=["docker"]),
    install_requires=["Flask==1.1.1", "flask-restplus==0.12.1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)