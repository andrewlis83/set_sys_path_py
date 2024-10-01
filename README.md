# set_sys_path_py
Simple script to automatically set sys.path in python projects where .venv struggles to find it properly. 

Currently using as a workaround for a bug in Linux version of Cursor IDE.

Requires pip.

## Usage

Place script in folder where your .py scripts are located. Import at top of your .py script using:

`from _set_sys_path import *`
