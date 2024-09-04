# Contribution and Development

- When developing inside the `gricean-pragmatics` repository, clone it and install the required packages under the `gricean_pragmatics` package as follows:

## Installation (Conda):

```bash
conda create --name [ENV NAME] python=3.8 ipython
source activate [ENV NAME]
# run the following command from the project root:
pip install -e ".[all]"
```

- Dependencies for running tests and generating the documentation are included in `[all]`

## Testing (Conda):

- Tests are written using the unittest module in the Python standard library. All tests are in the tests directory.

```bash
conda activate [ENV NAME]
green -vvv .
```

- Execute the command `green -vvv .` from the project root.

