import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MuseCP",
    version="1.0.1",
    author="Michael Kade",
    author_email="mike@mikda.com",
    description="Library for controlling a Acurus Muse Processor",
    long_description="Library for controlling a Acurus Muse Processor from Indy Labs",
    url="https://github.com/MikeKade/MuseCP",
    license="GNU",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
)
