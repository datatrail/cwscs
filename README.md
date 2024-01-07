# CataWiki Special Collection Service

Package to work with data from CataWiki.

## Project structure
```
- src
  - packagename
- tests
```

## Setup project
```
git clone ...
cd 
py -3.10 -m venv .venv
.venv\Scripts\activate.bat
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt
py -m pip install -r requirements-dev.txt
```

Visual Studio Code (settings.json):
```
{
    "python.analysis.extraPaths": [
        "./src"
    ],
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "./src"
      }
}
```


## Tests



## Links
- [Github: Manning - Publishing python packages](https://github.com/daneah/publishing-python-packages)

