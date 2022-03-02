import setuptools
setuptools.setup(
    name="FootballLib",
    version="0.1",
    author="none",
    author_email="nhatphuc2021b@gmail.com",
    maintainer="none",
    maintainer_email="nhatphuc2021b@gmail.com",
    description="Easier, less time to do code football project",
    url="https://github.com/Phuoc6C01/FootballLib",
    classifiers=[
         "Development Status :: 3 - Alpha",
         "License :: OSI Approved :: MIT License",
         "Natural Language :: Vietnamese",
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3 :: Only",
         "Intended Audience :: Other Audience"
    ],
    keywords="football",
    project_urls={
        "Bug Info":"https://github.com/Phuoc6C01/FootballLib/issues",
        "Main":"https://github.com/Phuoc6C01/FootballLib"
    },
    python_requires='>=3',
    package_dir={
        "": "main"
    },
    packages=setuptools.find_packages(where="main")
)