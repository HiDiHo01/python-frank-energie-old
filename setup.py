from setuptools import setup, find_packages

setup(
    name="python-frank-energie",  # Package name (must be unique on PyPI)
    version="2025.3.30",
    description="Asynchronous Python package for Frank Energie. Retrieve energy prices for Frank energie.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HiDiHo01/python-frank-energie",  # GitHub repo URL
    author="HiDiHo01",
    author_email="HiDiHo@gmail.com",
    license="MIT",
    packages=find_packages(),  # Automatically finds your package
    install_requires=[],  # Dependencies (e.g., ["requests", "numpy"])
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
