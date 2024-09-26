from setuptools import setup, find_packages

setup(
    name="pii-masker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "numpy",
    ],
    author="Xuying LI",
    author_email="xuyingl@hydrox.ai",
    description="A package for masking Personally Identifiable Information (PII) in text.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HydroXai/pii-masker",
)