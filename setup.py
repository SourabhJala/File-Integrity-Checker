from setuptools import setup, find_packages

setup(
    name="sourang-file-integrity-checker",
    version="1.0.0",
    author="Sourang",
    description="3D Cryptographic File Integrity Monitoring and Adversarial Tamper Detection Tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sourang/file-integrity-checker",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "sourang_integrity": [
            "web/*",
            "web/vendor/*"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Monitoring",
    ],
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.0.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "sourang-integrity=sourang_integrity.cli:main",
        ],
    },
)
