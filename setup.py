from setuptools import find_packages, setup

from pyMBPT import __version__

with open("README.md", "r") as file:
    long_description = file.read()

if __name__ == "__main__":
    setup(
        name="amset",
        version=__version__,
        description="pyMBPT is a tool to calculate Many-Body Interaction Problem "
        "based on Density Functional Theory and Many-Body Perturbation Theory",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/hackingmaterials/amset",
        author="Alex Ganose",
        author_email="kmr754156381@gmail.com",
        license="modified BSD",
        keywords="mobility conductivity seebeck scattering lifetime rates dft vasp",
        packages=find_packages(),
        package_data={
            "amset": [
                "defaults.yaml",
                "interpolation/quad.json",
                "plot/amset_base.mplstyle",
                "plot/revtex.mplstyle",
            ]
        },
        data_files=["LICENSE"],
        zip_safe=False,
        install_requires=[
            "pymatgen>=2022.0.16",
            "scipy",
            "monty",
            "matplotlib",
            "BoltzTraP2",
            "tqdm",
            "tabulate",
            "memory_profiler",
            "spglib",
            "click",
            "sumo",
            "h5py",
            "pyFFTW",
            "interpolation",
            "numba",
        ],
        setup_requires=[
            "numpy",
        ],
        extras_require={
            "docs": [
                "mkdocs==1.3.0",
                "mkdocs-material==8.3.6",
                "mkdocs-minify-plugin==0.5.0",
                "mkdocs-macros-plugin==0.7.0",
                "markdown-include==0.6.0",
                "markdown-katex==202112.1034",
            ],
            "tests": ["pytest==7.1.2", "pytest-cov==3.0.0"],
            "all-electron": ["pawpyseed==0.7.1"],
            "dev": [
                "coverage==6.4.1",
                "codacy-coverage==1.3.11",
                "pycodestyle==2.8.0",
                "mypy==0.961",
                "pydocstyle==6.1.1",
                "flake8==4.0.1",
                "pylint==2.14.3",
                "black==22.3.0",
                "pre-commit==2.19.0",
            ],
        },
        python_requires=">=3.8",
        classifiers=[
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Information Technology",
            "Operating System :: OS Independent",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Scientific/Engineering",
        ],
        tests_require=["pytest"],
        entry_points={
            "console_scripts": [
                "amset = amset.tools.cli:cli",
            ]
        },
    )