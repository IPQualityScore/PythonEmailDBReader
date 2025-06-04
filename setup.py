from setuptools import setup, find_packages

setup(
    name="IPQSEMAILDBREADER",
    version="1.0.0",
    description="Allows you to lookup important details about any email, checks our (IPQS) db for matches.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="IPQS",
    author_email="support@ipqualityscore.com",
    url="https://github.com/IPQualityScore/PythonEmailDBReader",
    packages=find_packages(),
    install_requires=[
        "functools", "typing", "struct", "os", "hashlib", "threading"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
