from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="keywordextractor",
    version="2.0.0",
    description="""This Library allows Developers to get Keywords from Text 
    The input Text must be String and output would be list of Keywords     
     """,
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/soumilshah1995/AppleStock",
    author="Soumil Nitin Shah",
    author_email="soushah@my.bridgeport.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["keywordextractor"],
    include_package_data=True,
    install_requires=["requests"]
)