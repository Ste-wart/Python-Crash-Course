from random import choice


class RandomWalk:
    """A class to generate random walks."""
    __slots__ = ['num_points', 'x_values', 'y_values']

    def __init__(self, num_points: int = 5000) -> None:
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def __repr__(self):
        return f'RandomWalk(points={self.num_points})'

    def fill_walk(self) -> None:
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            # Get the steps
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that goes nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    @staticmethod
    def get_step() -> int:
        """Decide which direction to go, and how far to go."""

        dirt = choice([1, -1])  # dirt = direction, dist = distance
        dist = choice([1, 2, 3, 4, 5])
        step = dirt * dist

        return step
