File level_player_GUI.txt is JSON file used to configure level player GUI.
It contains dictionary in which dictionaries are assigned to names of the
parts of the level_player_GUI. 
It constains of parts that are described below:
"screen" - requires width, height - required
 It is used to set size of surface that is used to draw everything on it.
 It has constant size set by the arguments and at the end of the drawing
 cycle, it is scaled to size of the game window and shown to user.

"game_screen" - requires posX, posY, width, height - required
 Used to define which part of GUI will show the game inself (terrain,
 towers, enemies...). posX and posY are position of the top left corner
 of the game_screen while width and height are dimensions of it.