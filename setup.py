import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wwebpy",
    version="1.0.0",
    author="KazeDevID",
    author_email="michaelagam91@gmail.com",
    description="A Python library to automate easily whatsapp web",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KazeDevID/wwebpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment :: Mozilla",
        "Natural Language :: English",
        "Topic :: Communications :: Chat",
    ],
    python_requires='>=3.6',
)
