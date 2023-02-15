import pathlib
from setuptools import find_packages, setup
from cool_bayesian_networks import __version__

HERE = pathlib.Path(__file__).parent

VERSION = {}
with open(HERE / "cool_bayesian_networks" / "version.py") as fp:
    exec(fp.read(), VERSION)
PACKAGE_NAME = "cool_bayesian_networks"
AUTHOR = "Pedro Arriola, Oscar López, Yong Park & Santiago Taracena"
AUTHOR_EMAIL = "tar20017@uvg.edu.gt"
URL = "https://github.com/SantiagoTaracena01/cool-bayesian-networks.git"

LICENSE = "MIT"  # Tipo de licencia
DESCRIPTION = (
    "Permite el manejo y construccion de Redes Bayesianas"  # Descripción corta
)

LONG_DESCRIPTION = (HERE / "README.md").read_text(
    encoding="utf-8"
)  # Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"


# Paquetes necesarios para que funcione la libreía. Se instalarán en el caso de que no esten instalados
INSTALL_REQUIRES = ["build", "pgmpy"]

KEYWORDS = ["bayesian-networks", "artificial-intelligence", "machine-learning"]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.10",
]

setup(
    name=PACKAGE_NAME,
    version=VERSION["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
)
