## Purpose

Adding with a click a lot of hours to the European Daimoku Counter (for the UK).


## Requirements

* Install Python if you don't have it:
https://www.python.org/downloads/
(make sure to check the box "ADD PYTHON TO PATH" during installation.

* Install Firefox if you don't have it:
https://www.mozilla.org/en-GB/firefox/new/


## Setup

* Copy the folder somewhere on your computer and save the path to it somewhere.

* Open your command line and change directory to the location you copied in the previous point.
```
cd "path/to/copied/folder"
```

* Setup your own environment:

```
python -m venv myenv
```

* Activate it:
    * Windows: `.\myenv\Scripts\activate`
    * Mac: `source myenv/bin/activate`

* Install the requirements.
```
pip install -r requirements.txt
```

## How to use

Run the program specifying how many minutes you want to add (in this case 10).
```
python -m addDmk 10
```

If the program is working, you will see the browser opening and going the European counter URL and then selecting the options by itself and submit.
The program will repeat this process the number of times needed to get to the amount of minutes specified.

# Important note
While the program is running DON'T type or click anything, because that would interfere with the program and make it to fail.
At the end a summary message should appear, with the amount of minutes added to the counter.