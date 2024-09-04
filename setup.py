import os
from setuptools import setup


# version
# with open(os.path.join(os.path.dirname(__file__), "ei", "VERSION")) as version_file:
#     VERSION = version_file.read().strip()

# readme
# with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as readme_file:
#     readme_description = readme_file.read().strip()

# requirements
with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    required = f.read().splitlines()
    print(required)

# description
description = "evaluate LLM's pragmaic competence"

# testing
test_deps = required + ["green>=2.5.0", "coverage", "mypy"]
# NOTE: <packagename> @ allows installation of git-based URLs
dev_deps = test_deps + [
    "black",
    "wheel",
]

setup(
    name="gricean_pragmatics",
    version="0.1",
    author="yancong222, elsayed-issa, afukada",
    description=description,
    #long_description=readme_description,
    keywords=["gricean", "pragmatics", "llms", "arabic", "japanese", "english"],
    packages=["gricean_pragmatics"],
    install_requires=required,
    url="",
    license="MIT",
    scripts=[
        os.path.join("bin", "gp-rest-api"),
        os.path.join("bin", "gp-ui"),
    ],
    classifiers=[
        "Natural Language :: English :: Japanese",
        "Topic :: LLMs :: Gricean Pragmatics",
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
