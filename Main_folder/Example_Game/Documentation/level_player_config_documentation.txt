File level_player_config.txt is used to configure LevelPlayer.
It is JSON file containing one dictionary with required constants.
Currently contained constants are (name : format/type):
"TILE_SIZE" : integer
 Used to configure size of tiles, it affects terrain, enemies and
 towers when they are being drawn. In addition to that, it affects
 user input because larger tiles are easier to click on.
 Set it properly to avoid problems with drawing items in game_screen.

"MAX_TERRAIN_WIDTH" : integer
"MAX_TERRAIN_HEIGHT" : integer
 Used to set maximal size of terrain in tiles. Trying to load bigger
 terrains will throw exception TerrainHasWrongSizeException. It main
 function is to force constant size of all terrains to prevent problems
 with showing whole terrain.

"LOGIC_CYCLE_INTERVAL" : integer
 Used to set interval of logic cycle in miliseconds. Larger number
 slows the game down while smaller number increases speed of the game.
 Does not affect drawing cycle interval.