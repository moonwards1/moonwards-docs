Input Mapping
=============
Methods
-------

+--------------------+---------------------------------------------------------------------------------------------+
| void               | :ref:`load_config<input_map_load_config>` **(** :godot_class:`bool` enable_next=true **)**  |
+--------------------+---------------------------------------------------------------------------------------------+
| :godot_class:`int` | :ref:`save_to_config<input_map_save_to_config>` **( )**                                     |
+--------------------+---------------------------------------------------------------------------------------------+
| void               | :ref:`save_all<input_map_save_all>` **( )**                                                 |
+--------------------+---------------------------------------------------------------------------------------------+

Constants
---------
* :godot_class:`string` CONFIG_FILE

Default value = "user://inputmap.cfg"

Members
-------
* :godot_class:`array` INPUT_ACTIONS


Description
-----------

This is a singleton that helps a set of keys to be saved as an input map for later use. This input map will be persistent as it is loaded each time the game is started.

You can access this singleton via the name ``Input_Map`` followed by one of the methods of the class.

Method Descriptions
-------------------

.. _input_map_load_config:

* void **load_config** ( )

Loads the file specified in ``CONFIG_FILE``, if it can not find it, this function will create it.


.. _input_map_save_to_config:

* :godot_class:`int` **save_to_config** (:godot_class:`string` section, :godot_class:`int` key, :godot_class:`int` value)

This is a generic function to save specific information to a :godot_class:`ConfigFile<configfile>`. Can be used for saving any value, related to any key, under any section.
For input information, the section is "input", the key is the action name and the value is the scancode of the action.


.. _input_map_save_all:

* void **save_all** ( )

Saves the current Input Map into a :godot_class:`ConfigFile<configfile>` saved in ``CONFIG_FILE`` that can be later accessed using :ref:`load_config <input_map_load_config>`.
