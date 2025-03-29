from setuptools import setup, find_packages

setup(
    name="jenkinsfile",  # Replace with your package name
    version="1.0.0",
    author="Mamatha1206",
    author_email="mamathaedulakanti@gmail.com",
    description="A sample Python application",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Mamatha1206/jenkins_practice",  # Update with your repo link
    packages=find_packages(),
    install_requires=[
        "requests",  # Example dependencies
        "flask"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
