from pathlib import Path
import json
from scoreboard import ScoreBoard


class Safe:

    def __init__(self):
        self.sb = ScoreBoard(self)

    def store(self, path):
        """Stores The user's favorite number"""
        high_score = self.sb.prep_high_score()
        contents = json.dumps(high_score)
        path.write_text(contents)

    def bring(self, file):
        path = Path(file)
        """Retrieves The user's favorite number"""
        if path.exists():
            contents = path.read_text()
            value = json.loads(contents)
            return value
        else:
            return None
