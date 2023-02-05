from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "Bayesian networks library"

setup(
    name="cool-bayesian-networks",
    version=VERSION,
    author="Pedro Arriola, Oscar López, Yong Park & Santiago Taracena",
    author_email="<tar20017@uvg.edu.gt>",
    description=DESCRIPTION,
    packages=find_packages(),
    keywords=["python", "bayesian networks", "machine learning", "artificial intelligence"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
