.. _singleton_gamestate:

Gamestate
=========

**Inherits:** :godot_class:`Node<node>` **<** :godot_class:`Object<object>`

**Category:** Singleton

Brief Description
-----------------

Handles multiplayer gamestate.

Methods
-------

+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| :ref:`float<class_float>`                             | :ref:`get_playback_position<class_AudioStreamPlayer3D_method_get_playback_position>` **(** **)**           |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| :ref:`AudioStreamPlayback<class_AudioStreamPlayback>` | :ref:`get_stream_playback<class_AudioStreamPlayer3D_method_get_stream_playback>` **(** **)**               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| void                                                  | :ref:`play<class_AudioStreamPlayer3D_method_play>` **(** :ref:`float<class_float>` from_position=0.0 **)** |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| void                                                  | :ref:`seek<class_AudioStreamPlayer3D_method_seek>` **(** :ref:`float<class_float>` to_position **)**       |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| void                                                  | :ref:`stop<class_AudioStreamPlayer3D_method_stop>` **(** **)**                                             |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

Signals
-------

.. _singleton_gamestate_signal_user_join:

- **user_join** **(** **)**

Emits when user is fully registered.

.. _singleton_gamestate_signal_user_leave:

- **user_leave** **(** **)**

Emits when a registered user leaves.

.. _singleton_gamestate_signal_user_name_disconnected:

- **user_name_disconnected** **(** :godot_class:`String<string>` name **)**

Emits when user is connected for chat.

.. _singleton_gamestate_signal_user_name_connected:

- **user_name_connected** **(** :godot_class:`String<string>` name **)**

Emits when user is disconnected from chat.

.. _singleton_gamestate_signal_user_msg:

- **user_msg** **(** :godot_class:`int` id, :godot_class:`string` msg **)**

Emits message of id user.

.. _singleton_gamestate_signal_player_id:

- **player_id** **(** :godot_class:`int` id **)**

Emits id of player after establishing a connection.

.. _singleton_gamestate_signal_server_up:

- **server_up** **(** **)**

No description provided.

.. _singleton_gamestate_signal_server_connected:

- **server_connected** **(** **)**

No description provided.

.. _singleton_gamestate_signal_server_select:

- **server_select** **(** **)**

Shows dialog to connect to a server or create a server.

.. _singleton_gamestate_signal_network_error:

- **network_error** **(** :godot_class:`string` message **)**

No description provided.

.. _singleton_gamestate_signal_network_log:

- **network_log** **(** :godot_class:`string` message **)**

Emmit on change in server status, client status - conenction, establishing connection, etc.

.. _singleton_gamestate_signal_scene_change:

- **scene_change** **(** **)**

No description provided.

.. _singleton_gamestate_signal_scene_change_name:

- **scene_change_name** **(** name **)**

No description provided.

.. _singleton_gamestate_signal_scene_change_error:

- **scene_change_error** **(** msg **)**

No description provided.

.. _singleton_gamestate_signal_loading_progress:

- **loading_progress** **(** percentage **)**

No description provided.

.. _singleton_gamestate_signal_loading_done:

- **loading_done** **(** **)**

.. _singleton_gamestate_signal_loading_error:

- **loading_error** **(** msg **)**

No description provided.

.. _singleton_gamestate_signal_player_scene:

- **player_scene** **(** **)**

No description provided.

Emit when a scene for players is detected

.. _singleton_gamestate_signal_connection_failed:

- **connection_failed** **(** **)**

No description provided.

.. _singleton_gamestate_signal_connection_succeeded:

- **connection_succeeded** **(** **)**

No description provided.

.. _singleton_gamestate_signal_game_ended:

- **game_ended** **(** **)**

No description provided.

.. _singleton_gamestate_signal_game_error:

- **game_error** **(** what **)**

No description provided.


Description
-----------

Does something with multiplayer

Tutorials
---------

- Should be done

Method Descriptions
-------------------

.. _class_AudioStreamPlayer3D_method_get_playback_position:

- :ref:`float<class_float>` **get_playback_position** **(** **)**

Returns the position in the :ref:`AudioStream<class_AudioStream>`.

.. _class_AudioStreamPlayer3D_method_get_stream_playback:

- :ref:`AudioStreamPlayback<class_AudioStreamPlayback>` **get_stream_playback** **(** **)**

.. _class_AudioStreamPlayer3D_method_play:

- void **play** **(** :ref:`float<class_float>` from_position=0.0 **)**

Plays the audio from the given position 'from_position', in seconds.

.. _class_AudioStreamPlayer3D_method_seek:

- void **seek** **(** :ref:`float<class_float>` to_position **)**

Sets the position from which audio will be played, in seconds.

.. _class_AudioStreamPlayer3D_method_stop:

- void **stop** **(** **)**

Stops the audio.
