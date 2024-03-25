import os
from setuptools import setup


# version
with open(os.path.join(os.path.dirname(__file__), "ei", "VERSION")) as version_file:
    VERSION = version_file.read().strip()

# readme
# with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as readme_file:
#     readme_description = readme_file.read().strip()

# requirements
with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    required = f.read().splitlines()
    print(required)

# description
description = "perform automatic elicited imitation"

# testing
test_deps = required + ["green>=2.5.0", "coverage", "mypy"]
# NOTE: <packagename> @ allows installation of git-based URLs
dev_deps = test_deps + [
    "black",
    "wheel",
]

setup(
    name="ei",
    version=VERSION,
    author="elsayed-issa, yancong222, afukada, Ayaakaaa",
    description=description,
    #long_description=readme_description,
    keywords=["elicited", "imitation", "ei", "speech", "japanese", "english"],
    packages=["ei"],
    install_requires=required,
    url="",
    license="MIT",
    scripts=[
        os.path.join("bin", "ei-rest-api"),
        os.path.join("bin", "ei-ui"),
    ],
    classifiers=[
        "Natural Language :: English :: Japanese",
        "Topic :: Language/Acquisition :: Elicited Imitation",
    ],
    include_package_data=True,
    tests_require=test_deps,
    extras_require={
        "test": test_deps,
        # "dev": dev_deps,
        "all": dev_deps
        # 'docs': docs_deps
    },
)
