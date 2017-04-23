#Program hosting core that runs the game

import moduleGameCore

if __name__ == "__main__": #Runs the game only if launched as the top most script
    gameCore = moduleGameCore.GameCore()
    gameCore.run()


