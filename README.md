# set_sys_path_py
Script to automatically set sys.path in python projects where terminal struggles to find .venv path properly. 

Currently using as a workaround for a bug in Linux version of Cursor IDE.

Requires pip.

## Usage

Place script in folder where your .py scripts are located. Import at top of your .py script using:

`from _set_sys_path import *`
