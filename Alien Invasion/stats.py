from pathlib import Path
import json
from scoreboard import ScoreBoard


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = self.bring()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def bring(self):
        """Gets high score from file, if it exists."""
        path = Path('high_score.json')
        try:
            contents = path.read_text()
            value = json.loads(contents)
            return value
        except FileNotFoundError:
            return 0
