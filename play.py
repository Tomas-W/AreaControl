# from game.setup import Game
#
# game = Game()
#
# game.run_game()

from game_setup import GameSetup

game = GameSetup()
game.run_game()

# TODO: Refactor sound_is_on from Player?
# TODO: Fix pausing game
# TODO: Fix sprite group names
# TODO: Fix SkullCollector spawn (FireSkull spawning in wall)
# TODO: Optimize hitboxes
