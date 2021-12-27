import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


REQUIREMENTS = [
    'tensorflow >= 2.5',
    'keras-tuner',
    'transformers'
]

setuptools.setup(
    name="howie",
    version="0.0.1",
    author="Sioan Zohar",
    author_email="zohar.sioan@gmail.com",
    description="Guessing feelings and needs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sioan/howie",
    project_urls={
        "Bug Tracker": "https://github.com/sioan/howie/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=REQUIREMENTS,
    python_requires=">=3.6",

    entry_points={
        'console_scripts': [
            'keras_train = howie.keras_train:main',
        ],
    },
)
