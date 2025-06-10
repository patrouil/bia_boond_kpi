from setuptools import setup, find_packages
import os

# Lecture du fichier README pour la description longue
with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lecture des requirements depuis requirements.txt
def read_requirements():
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    # Informations de base du package
    name="boondkpi",
    version="1.0.0",
    author="patrouil",
    author_email="patrouil@gmail.com",
    description="moteur de reporting Boond Manager de BIA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/patrouil/boondkpi",

    # Configuration des packages
    packages=find_packages(),
    # Ou spécifier manuellement : packages=["mon_package", "mon_package.sous_module"],

    # Fichiers de données à inclure
    package_data={
        "boond": ["boond/*.py"],
        "entities": ["entities/*.py"],
        "mapper": ["mapper/*.py"],
        "query": ["query/*.py"],
        "report": ["report/*.py"],
        "main": ["mailler.py", "boondkpi.py", "configuration.py", "boondkpi.sh"],
        "conf": ["conf/*.*"],
    },
    include_package_data=True,

    # Dépendances
    install_requires=read_requirements(),

    # Dépendances optionnelles
    #extras_require={
   #     "dev": ["pytest>=6.0", "black", "flake8"],
    #    "docs": ["sphinx", "sphinx-rtd-theme"],
    #    "api": ["fastapi", "uvicorn"],
    #},

    # Version Python requise
    python_requires=">=3.8",

    # Classification du package
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],

    # Mots-clés pour la recherche sur PyPI
    keywords="boond manager",

    # Scripts en ligne de commande
    entry_points={
        "console_scripts": [

        ],
    },

    # Métadonnées du projet (format moderne)
    project_urls={
        "Bug Reports": "https://github.com/votre-username/votre-repo/issues",
        "Source": "https://github.com/votre-username/votre-repo",
        "Documentation": "https://votre-package.readthedocs.io/",
    },

    # Configuration pour les tests
    test_suite="tests",
    tests_require=["pytest"],

    # Licence
    license="MIT",

    # Plateforme supportée
    platforms=["any"],

    # Inclusion automatique des fichiers MANIFEST.in
    zip_safe=False,
)