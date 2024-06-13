from setuptools import find_packages, setup

setup(
    name="helloasso_api_wrapper",
    version="0.0.1",
    description="Python wrapper for Helloasso APIV5",
    url="https://github.com/HelloAsso/HaApiV5",
    author="ECLAIR",
    maintainer="ECLAIR",
    license="MIT License",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "helloasso-apiv5==1.0.0",
        "pydantic>=2.5",
    ],
    python_requires=">=3.6",
)
