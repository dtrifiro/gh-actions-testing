from setuptools import setup

setup(
    name="gh-actions-testing",
    version="0.0.1",
    description="testing",
    long_description="Testing out packaging on gh actions",
    url="https://github.com/dtrifiro/gh-actions-testing",
    author="Daniele Trifirò",
    author_email="daniele@iterative.ai",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    py_modules=["testing"],
    entry_points={
        "console_scripts": [
            "hello=testing:main",
        ],
    },
)
