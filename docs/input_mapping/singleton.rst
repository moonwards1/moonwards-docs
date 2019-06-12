Input Mapping
=============
Methods

:ref:`save_all<_input_map_save_allk>`

Description
-----------

This is a singleton that helps a set of keys to be saved as an input map for later use. This input map will be persistent as it is loaded each time the game is started.

Usage
-----

You can access this singleton via the name `Input_Map` followed by one of the next methods

Members
-------
const CONFIG_FILE = "user://inputmap.cfg"
array INPUT_ACTIONS = []

Method Descriptions
---------
.. _input_map_load_config:
* void **load_config** ( )
Loads the file specified in ``CONFIG_FILE``, if it can not find it, this function will create it.


.. _input_map_save_to_config:
* :godot_class:`int<int.html>` **save_to_config** (:godot_class:`String <string.html>` section, :godot_class:`int <int.html>` key, :godot_class:`int <int.html>` value))
This is a generic function to save specific information to a :godot_class:`ConfigFile <configfile.html`. Can be used for saving any value, related to any key, under any section.
For input information, the section is "input", the key is the action name and the value is the scancode of the action.


.. _input_map_save_all:
* void **save_all** ( )
Saves the current Input Map into a :godot_class:`ConfigFile <configfile.html` saved in ``CONFIG_FILE`` that can be later accessed using **load_config**
