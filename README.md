# PyFHIaims

![python](https://img.shields.io/badge/python-3.7%7C3.8-blue)
![license](https://img.shields.io/badge/license-MPL--2.0-orange)
[![code style](https://img.shields.io/badge/code%20style-black-202020.svg)](https://github.com/ambv/black)


## Installing

```
pip install git+https://github.com/jhrmnn/pyfhiaims.git
```

## Examples

```python
from fhiaims.inputs import Aims
from fhiaims.outputs import parse_aims

aims = Aims()
inputs = aims(
    species_defaults="light",
    atoms=[("Ar", 0, 0, 0)],
    tags=dict(
        xc="pbe",
        relativistic="atomic_zora scalar",
        sc_iter_limit=10,
    ),
)
# save inputs files, run FHI-aims...
energy = parse_aims(open("aims.out"))["total_energy"]
```

## Developing

```
git clone git@github.com:jhrmnn/pyfhiaims.git
cd pyfhiaims
poetry install -E test
flake8
isort
black .
coverage run -m pytest && coverage report
```
