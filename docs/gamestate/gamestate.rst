gamestate
=========

**Inherits:**:godot_class:`extends Node`

**Category:** <FILL THIS SPACE>

Brief Description
-----------------

<FILL A BRIEF DESCRIPTION HERE>

Methods
-------
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`bindsig<gamestate_method_bindsig>` **(** _signal, _sub, obj, obj2, d = 0 **)**                                                                                              |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`bindtg<gamestate_method_bindtg>` **(** _signal, _sub = null **)**                                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`bindtgc<gamestate_method_bindtgc>` **(** _signal, _sub = null **)**                                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`bindtgd<gamestate_method_bindtgd>` **(** _signal, _sub = null **)**                                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`bindgg<gamestate_method_bindgg>` **(** _signal, _sub = null **)**                                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`queue_attach<gamestate_method_queue_attach>` **(** path, node, permanent = false **)**                                                                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`queue_tree_signal<gamestate_method_queue_tree_signal>` **(** path, sig, permanent = false **)**                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`queue_attach_on_tree_change<gamestate_method_queue_attach_on_tree_change>` **(**  **)**                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_network_log<gamestate_method_sg_network_log>` **(** msg **)**                                                                                                            |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_gslog<gamestate_method_sg_gslog>` **(** msg **)**                                                                                                                        |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`on_scene_change_log<gamestate_method_on_scene_change_log>` **(**  **)**                                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_getsocket<gamestate_method_net_getsocket>` **(**  **)**                                                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_tree_connect<gamestate_method_net_tree_connect>` **(** bind=true **)**                                                                                                  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_connection_fail<gamestate_method_net_connection_fail>` **(**  **)**                                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_client_connected<gamestate_method_net_client_connected>` **(** id **)**                                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_client_disconnected<gamestate_method_net_client_disconnected>` **(** id **)**                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_server_connected<gamestate_method_net_server_connected>` **(**  **)**                                                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_server_disconnected<gamestate_method_net_server_disconnected>` **(**  **)**                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_server_up<gamestate_method_net_server_up>` **(**  **)**                                                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_set_mode<gamestate_method_server_set_mode>` **(** host="localhost" **)**                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_tree_changed<gamestate_method_server_tree_changed>` **(**  **)**                                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_user_connected<gamestate_method_server_user_connected>` **(** id **)**                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_user_disconnected<gamestate_method_server_user_disconnected>` **(** id **)**                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_tree_user_connected<gamestate_method_server_tree_user_connected>` **(** id **)**                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`server_tree_user_disconnected<gamestate_method_server_tree_user_disconnected>` **(** id **)**                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_connection_failed<gamestate_method_sg_connection_failed>` **(**  **)**                                                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_connected_to_server<gamestate_method_sg_connected_to_server>` **(**  **)**                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`client_server_connect<gamestate_method_client_server_connect>` **(** host, port=DEFAULT_PORT **)**                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`change_scene<gamestate_method_change_scene>` **(** scene **)**                                                                                                              |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_player_scene<gamestate_method_sg_player_scene>` **(**  **)**                                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`is_player_scene<gamestate_method_is_player_scene>` **(**  **)**                                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_apply_opt<gamestate_method_player_apply_opt>` **(** pdata, player, id **)**                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_register<gamestate_method_player_register>` **(** pdata, localplayer=false, opt_id = "avatar" **)**                                                                  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`sg_player_id<gamestate_method_sg_player_id>` **(** id **)**                                                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`remote register_client<gamestate_method_remote register_client>` **(** id, pdata **)**                                                                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`remote unregister_client<gamestate_method_remote unregister_client>` **(** id **)**                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_get<gamestate_method_player_get>` **(** prop, id=null **)**                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_remap_id<gamestate_method_player_remap_id>` **(** oid, nid **)**                                                                                                     |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`create_player<gamestate_method_create_player>` **(** id **)**                                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_local_camera<gamestate_method_player_local_camera>` **(** activate = true **)**                                                                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_noinput<gamestate_method_player_noinput>` **(** enable = false **)**                                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`_server_disconnected<gamestate_method__server_disconnected>` **(**  **)**                                                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`_connected_fail<gamestate_method__connected_fail>` **(**  **)**                                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`end_game<gamestate_method_end_game>` **(**  **)**                                                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`_ready<gamestate_method__ready>` **(**  **)**                                                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`printd<gamestate_method_printd>` **(** s **)**                                                                                                                              |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`log_all_signals<gamestate_method_log_all_signals>` **(**  **)**                                                                                                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`log_all_signals_print_1<gamestate_method_log_all_signals_print_1>` **(** sg **)**                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`log_all_signals_print_2<gamestate_method_log_all_signals_print_2>` **(** a1, sg **)**                                                                                       |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`log_all_signals_print_3<gamestate_method_log_all_signals_print_3>` **(** a1, a2, sg **)**                                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`loading_done<gamestate_method_loading_done>` **(** var error **)**                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`load_level<gamestate_method_load_level>` **(** var resource **)**                                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_up<gamestate_method_net_up>` **(**  **)**                                                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_down<gamestate_method_net_down>` **(**  **)**                                                                                                                           |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`net_client<gamestate_method_net_client>` **(** id, connected **)**                                                                                                          |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`player_scene<gamestate_method_player_scene>` **(**  **)**                                                                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                       | :ref:`AddChatUI<gamestate_method_AddChatUI>` **(**  **)**                                                                                                                         |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Signals
-------

.. _gamestate_signal_gslog:

- **gslog** **(** msg **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_user_join:

- **user_join** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_user_leave:

- **user_leave** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_user_name_disconnected:

- **user_name_disconnected** **(** name **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_user_name_connected:

- **user_name_connected** **(** name **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_user_msg:

- **user_msg** **(** id, msg **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_player_id:

- **player_id** **(** id **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_server_up:

- **server_up** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_server_connected:

- **server_connected** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_server_select:

- **server_select** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_network_error:

- **network_error** **(** message **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_network_log:

- **network_log** **(** message **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_scene_change:

- **scene_change** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_scene_change_name:

- **scene_change_name** **(** name **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_scene_change_error:

- **scene_change_error** **(** msg **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_loading_progress:

- **loading_progress** **(** percentage **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_loading_done:

- **loading_done** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_loading_error:

- **loading_error** **(** msg **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_player_scene:

- **player_scene** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_connection_failed:

- **connection_failed** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_connection_succeeded:

- **connection_succeeded** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_game_ended:

- **game_ended** **(** **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_game_error:

- **game_error** **(** what **)** 

!<FILL DESCRIPTION HERE>!

.. _gamestate_signal_			= sig,:

- **			= sig,** **(** **)**

!<FILL DESCRIPTION HERE>!

Description
-----------

!<FILL DESCRIPTION HERE>!

Method Descriptions
-------------------

.. _gamestate_method_bindsig:

- :godot_class:`Title <FILL>` **bindsig** **(** _signal, _sub, obj, obj2, d = 0 **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_bindtg:

- :godot_class:`Title <FILL>` **bindtg** **(** _signal, _sub = null **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_bindtgc:

- :godot_class:`Title <FILL>` **bindtgc** **(** _signal, _sub = null **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_bindtgd:

- :godot_class:`Title <FILL>` **bindtgd** **(** _signal, _sub = null **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_bindgg:

- :godot_class:`Title <FILL>` **bindgg** **(** _signal, _sub = null **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_queue_attach:

- :godot_class:`Title <FILL>` **queue_attach** **(** path, node, permanent = false **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_queue_tree_signal:

- :godot_class:`Title <FILL>` **queue_tree_signal** **(** path, sig, permanent = false **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_queue_attach_on_tree_change:

- :godot_class:`Title <FILL>` **queue_attach_on_tree_change** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_network_log:

- :godot_class:`Title <FILL>` **sg_network_log** **(** msg **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_gslog:

- :godot_class:`Title <FILL>` **sg_gslog** **(** msg **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_on_scene_change_log:

- :godot_class:`Title <FILL>` **on_scene_change_log** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_getsocket:

- :godot_class:`Title <FILL>` **net_getsocket** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_tree_connect:

- :godot_class:`Title <FILL>` **net_tree_connect** **(** bind=true **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_connection_fail:

- :godot_class:`Title <FILL>` **net_connection_fail** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_client_connected:

- :godot_class:`Title <FILL>` **net_client_connected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_client_disconnected:

- :godot_class:`Title <FILL>` **net_client_disconnected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_server_connected:

- :godot_class:`Title <FILL>` **net_server_connected** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_server_disconnected:

- :godot_class:`Title <FILL>` **net_server_disconnected** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_server_up:

- :godot_class:`Title <FILL>` **net_server_up** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_set_mode:

- :godot_class:`Title <FILL>` **server_set_mode** **(** host="localhost" **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_tree_changed:

- :godot_class:`Title <FILL>` **server_tree_changed** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_user_connected:

- :godot_class:`Title <FILL>` **server_user_connected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_user_disconnected:

- :godot_class:`Title <FILL>` **server_user_disconnected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_tree_user_connected:

- :godot_class:`Title <FILL>` **server_tree_user_connected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_server_tree_user_disconnected:

- :godot_class:`Title <FILL>` **server_tree_user_disconnected** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_connection_failed:

- :godot_class:`Title <FILL>` **sg_connection_failed** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_connected_to_server:

- :godot_class:`Title <FILL>` **sg_connected_to_server** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_client_server_connect:

- :godot_class:`Title <FILL>` **client_server_connect** **(** host, port=DEFAULT_PORT **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_change_scene:

- :godot_class:`Title <FILL>` **change_scene** **(** scene **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_player_scene:

- :godot_class:`Title <FILL>` **sg_player_scene** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_is_player_scene:

- :godot_class:`Title <FILL>` **is_player_scene** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_apply_opt:

- :godot_class:`Title <FILL>` **player_apply_opt** **(** pdata, player, id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_register:

- :godot_class:`Title <FILL>` **player_register** **(** pdata, localplayer=false, opt_id = "avatar" **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_sg_player_id:

- :godot_class:`Title <FILL>` **sg_player_id** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_remote register_client:

- :godot_class:`Title <FILL>` **remote register_client** **(** id, pdata **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_remote unregister_client:

- :godot_class:`Title <FILL>` **remote unregister_client** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_get:

- :godot_class:`Title <FILL>` **player_get** **(** prop, id=null **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_remap_id:

- :godot_class:`Title <FILL>` **player_remap_id** **(** oid, nid **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_create_player:

- :godot_class:`Title <FILL>` **create_player** **(** id **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_local_camera:

- :godot_class:`Title <FILL>` **player_local_camera** **(** activate = true **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_noinput:

- :godot_class:`Title <FILL>` **player_noinput** **(** enable = false **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method__server_disconnected:

- :godot_class:`Title <FILL>` **_server_disconnected** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method__connected_fail:

- :godot_class:`Title <FILL>` **_connected_fail** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_end_game:

- :godot_class:`Title <FILL>` **end_game** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method__ready:

- :godot_class:`Title <FILL>` **_ready** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_printd:

- :godot_class:`Title <FILL>` **printd** **(** s **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_log_all_signals:

- :godot_class:`Title <FILL>` **log_all_signals** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_log_all_signals_print_1:

- :godot_class:`Title <FILL>` **log_all_signals_print_1** **(** sg **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_log_all_signals_print_2:

- :godot_class:`Title <FILL>` **log_all_signals_print_2** **(** a1, sg **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_log_all_signals_print_3:

- :godot_class:`Title <FILL>` **log_all_signals_print_3** **(** a1, a2, sg **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_loading_done:

- :godot_class:`Title <FILL>` **loading_done** **(** var error **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_load_level:

- :godot_class:`Title <FILL>` **load_level** **(** var resource **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_up:

- :godot_class:`Title <FILL>` **net_up** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_down:

- :godot_class:`Title <FILL>` **net_down** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_net_client:

- :godot_class:`Title <FILL>` **net_client** **(** id, connected **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_player_scene:

- :godot_class:`Title <FILL>` **player_scene** **(**  **)**

!<FILL DESCRIPTION HERE>!

.. _gamestate_method_AddChatUI:

- :godot_class:`Title <FILL>` **AddChatUI** **(**  **)**

!<FILL DESCRIPTION HERE>!

