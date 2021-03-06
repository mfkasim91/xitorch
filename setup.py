import os
from setuptools import setup, find_packages

module_name = "xitorch"
file_dir = os.path.dirname(os.path.realpath(__file__))
absdir = lambda p: os.path.join(file_dir, p)

############### versioning ###############
verfile = os.path.abspath(os.path.join(module_name, "version.py"))
version = {"__file__": verfile}
with open(verfile, "r") as fp:
    exec(fp.read(), version)

############### setup ###############

def get_requirements(fname):
    with open(absdir(fname), "r") as f:
        return [line.strip() for line in f.read().split("\n") if line.strip() != ""]

setup(
    name=module_name,
    version=version["get_version"](),
    description='Differentiable scientific computing library',
    url='https://xitorch.readthedocs.io/',
    author='mfkasim1',
    author_email='firman.kasim@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="project library linear-algebra autograd functionals",
    zip_safe=False
)
