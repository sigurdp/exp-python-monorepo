# exp-python-monorepo

Inspiration drawn from: https://medium.com/opendoor-labs/our-python-monorepo-d34028f2b6fa

```
py
├── projects  # Each project contains code for a service and/or ETL
│   ├── project1
│   │   ├── Dockerfile
│   │   ├── pyproject.toml  # Each project has its own dependencies
│   │   ├── project1/       # Project code (Python modules) go here
│   │   └── tests/
│   └── project2...
├── lib  # Each lib is a Python package that you can install using poetry (or pip)
│   ├── lib1
│   │   ├── pyproject.toml  # Each lib specifies its dependencies
│   │   ├── opendoor/lib1/  # All internal packages are in the opendoor namespace
│   │   └── tests/
│   └── lib2...
└── tools
    ├── pippy  # Our service generator
    ├── pyfmt  # Code formatter to be used across all Python code
    ├── ci/    # Common CI/CD infrastructure
    └── other tools...
```

## Poetry stuff

poetry env use python3.11

Should look into Poetry 1.8 and `package-mode = false`

```
poetry config --list
poetry config virtualenvs.in-project true

poetry add --editable ../../libs/lib1
```


```
poetry self update
```
