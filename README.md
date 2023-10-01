# als-version-patcher
quick patcher for als files, to open recent project on older live version.


## Setup

Install Dependencies:

````
python3 -m pip install requirements.txt
````


Install tool with pip

````
python3 -m pip install .
````


## Run
```
> python3 -m als_patcher --help
usage: __main__.py [-h] [-i I] [-o O] [-v V]

als version modifier

options:
  -h, --help  show this help message and exit
  -i I        Path to the input als file
  -o O        Path to the output als file
  -v V        Ableton target version
```


## Add a Live Version

Complete the ini file with the differents values coming from your als file xml header



## Warning
- This method has been tested only for Live11.5 to Live11.0
- This method works only if no new features/ new synth are not used (synth not present in the target older version)



