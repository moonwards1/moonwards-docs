Input Mapping
=============

Description
-----------

This is a singleton that helps a set of keys to be saved as an input map for later use. This input map will be persistent as it is loaded each time the game is started.

Usage
-----

You can access this singleton via the name `Input_Map` followed by one of the next Functions

Members
-------
const CONFIG_FILE = "user://inputmap.cfg"
array INPUT_ACTIONS = []

Functions
---------

* void load_config():


* :godot_class:`int<int.html>` save_to_config():
