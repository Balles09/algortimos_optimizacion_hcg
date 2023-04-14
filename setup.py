### Archivp de  configuracion (setup.py)

from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="algoritmos_optimizacion_hcg",
    version="0.0.1",
    author="Daniel Ballesteros",
    author_email="a01654687@tec.com",
    description="HACER GUERRERO GRANDE DE NUEVO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Balles09/algortimos_optimizacion_hcg.git",
    install_requires=[
        "numpy>=1.21.6"
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)

