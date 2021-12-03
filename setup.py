import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="mildom",
    version="1.4.2",
    author="Alpaca131",
    author_email="iwa124816@gmail.com",
    description="Unofficial wrapper for mildom api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alpaca131/mildom_lib",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests>=2.25.1"
    ],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
