import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_min_queue-naman-bhalla",
    version="0.0.1",
    author="Naman Bhalla",
    author_email="namanbhalla1998@gmail.com",
    description="An Implementation of a Queue with O(1) find-min",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Naman-Bhalla/py_min_queue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)