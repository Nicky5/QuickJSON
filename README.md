# QuickJSON

[QuickJSON](https://pypi.org/project/QuickJSON-nicky/) is a python library that focuses on removing the ```open(file, 'w')``` hassle from your daily json file saving needs

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the package.

```bash
pip install QuickJSON
```

## Usage

Import the package to use it.
```python
import QuickJSON
```
\
Create a new QJSON object.
(everything after the "path" parameter will handed over to the ```dict``` super call.
```python
settings = QuickJSON.QJSON('path/to/json.json')
```
The object will behave like a normal python dictionary.

With following method all of the information stored inside the json file at the before 
given path will be stored in the current QJSON object.
Items that are already stored in the object wont be deleted. They will only be overwritten if 
you set no_override to False (by default set to False).
```python
settings.load(no_override=False)
```
\
Storing data works exactly like a normal python dictionary.
```python
settings['a key'] = 'a value'
```
\
Once you are done you can save the QJSON object to the previus path with the following command:

```python
settings.save()
```
\
You can also clear move or copy the JSON file by invoking one of the following functions:
```python
settings.copy_save('new/directory/for/json.json')
settings.merge_save('new/directory/for/json.json')
settings.clear_save()
```
The functions do not modify the content of the dictionary itself, but modify the to file saved content, so make sure to save before copying or moving anything.
``.clear_save`` and ```.move_save``` will also remove any empty folders left behind

\
 ```.save()```, ```.load()```, ```.move_save()``` and ```.copy_save``` will automatically check if any given directory is valid. They will generate any missing directories and files if necessary and return an empty dictionary if file is not found or corrupt. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
No License (yey)
