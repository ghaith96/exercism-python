from datetime import datetime, timedelta

EARTH_YEAR_IN_SECONDS = 315_576_00

planet_year_in_seconds_map = dict(
    earth=EARTH_YEAR_IN_SECONDS,
    mercury=EARTH_YEAR_IN_SECONDS * 0.2408467,
    venus=EARTH_YEAR_IN_SECONDS * 0.61519726,
    mars=EARTH_YEAR_IN_SECONDS * 1.8808158,
    jupiter=EARTH_YEAR_IN_SECONDS * 11.862615,
    saturn=EARTH_YEAR_IN_SECONDS * 29.447498,
    uranus=EARTH_YEAR_IN_SECONDS * 84.016846,
    neptune=EARTH_YEAR_IN_SECONDS * 164.79132,
)


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / planet_year_in_seconds_map["earth"], 2)

    def on_mercury(self):
        return round(self.seconds / planet_year_in_seconds_map["mercury"], 2)

    def on_venus(self):
        return round(self.seconds / planet_year_in_seconds_map["venus"], 2)

    def on_mars(self):
        return round(self.seconds / planet_year_in_seconds_map["mars"], 2)

    def on_jupiter(self):
        return round(self.seconds / planet_year_in_seconds_map["jupiter"], 2)

    def on_saturn(self):
        return round(self.seconds / planet_year_in_seconds_map["saturn"], 2)

    def on_uranus(self):
        return round(self.seconds / planet_year_in_seconds_map["uranus"], 2)

    def on_neptune(self):
        return round(self.seconds / planet_year_in_seconds_map["neptune"], 2)
