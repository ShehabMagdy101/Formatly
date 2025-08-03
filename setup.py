from setuptools import setup, find_packages

setup(
    name='formatly',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "streamlit",
        "PyPDF2",
        "regex",
        "tqdm",
        "transformers",
        "datasets",
        "peft",
        "trl",
        "accelerate"
    ],
    entry_points={
        "console_scripts": [
            "formatly-cli=src.main:main"
        ]
    },
)
