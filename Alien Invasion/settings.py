class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen Settings
        # The argument (1200, 800) is a tuple that defines the dimensions of the game window,
        # which will be 1,200 pixels wide by 800 pixels high.
        # (You can adjust these values depending on your display size.)
        self.screen_width = 1200
        self.screen_height = 600
        # Set the background color.
        self.bg_colour = (230, 230, 230)

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_allowed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 80, 60)

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed = 2.5
        self.ship_speed = 1.8
        self.alien_speed = 1.0
        self.fleet_direction = 1  # fleet_direction of 1 represents right; -1 represents left.
        self.alien_points = 50  # Scoring points

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
