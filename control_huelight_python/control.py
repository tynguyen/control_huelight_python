from phue import Bridge
import logging
from control_huelight_python.utils import color_utils

# from color_utils import MOOD_BOOSTING_COLOR_MAP, COLOR_RGB_MAP

logging.basicConfig(level=logging.INFO)


class BedroomHueLight(object):
    # user_name = "IIvz5qbqEzvJt-0pc6Xt4QAWVt5Od0rbsnzrUIYJ"
    light_unique_id = "00:17:88:01:06:c6:ed:f5-0b"
    light_name = "Hue color lamp bedroom 1"
    light_id = 5


def login_hue_bridge(
    bridge_ip="192.168.1.15", user_name="x-kHU4Ng800tNMpNIC51mF3l6V1bL9w4AuNB7-pI"
):
    bridge = Bridge(bridge_ip)
    return bridge


class BedroomHuelightController(object):
    def __init__(self, bedroom_hue_light_name):
        self.bridge = login_hue_bridge()
        # self.bridge.connect()
        self.light_name = bedroom_hue_light_name
        self.light_id = self.get_light_id()

    def get_light_id(self):
        for light in self.bridge.lights:
            if light.name == self.light_name:
                return light.light_id

    def turn_on(self):
        for light in self.bridge.lights:
            if light.name == self.light_name:
                light.on = True

    def turn_off(self):
        for light in self.bridge.lights:
            if light.name == self.light_name:
                light.on = False

    def set_brightness(self, brightness):
        # Transition: 5 seconds
        command = {"transitiontime": 50, "on": True, "bri": brightness}
        self.bridge.set_light(self.light_id, command)

    def set_color(self, xy):
        command = {"transitiontime": 50, "xy": xy}
        self.bridge.set_light(self.light_id, command)


def set_light_for_a_mood(mood_name: str = "encourage"):
    """Change the color of the light to the color of the mood
    Available moods: encourage, force_speedup, calm, fresh
    """
    # Get the color of the mood
    mood_colors = color_utils.get_mood_color(mood_name)
    if isinstance(mood_colors, list):
        mood_color = mood_colors[0]
    else:
        mood_color = mood_colors
    mood_color_rgb = color_utils.COLOR_RGB_MAP[mood_color]
    mood_color_xy = color_utils.rgb_to_xy(mood_color_rgb)

    # Set the color of the light
    light = BedroomHueLight()
    controller = BedroomHuelightController(light.light_name)
    logging.info(
        f"Set the color of the light to {mood_name}. Color: {mood_color} | xy: {mood_color_xy}"
    )
    controller.set_brightness(100)
    controller.set_color(mood_color_xy)


def set_encouragement_mood():
    """Change the color to encourage the user's mood
    # Set the color to the color of the mood
    """
    mood_name = "encourage"
    set_light_for_a_mood(mood_name)


def set_super_performance_mood():
    """Change the color to speed up the working speed
    """
    mood_name = "force_speedup"
    set_light_for_a_mood(mood_name)


def set_modern_mood():
    """Change the color to refresh the user's mood
    """
    mood_name = "modern"
    set_light_for_a_mood(mood_name)


def set_fresh_mood():
    """Change the color to refresh the user's mood
    """
    mood_name = "fresh"
    set_light_for_a_mood(mood_name)


if __name__ == "__main__":
    light = BedroomHueLight()
    controller = BedroomHuelightController(light.light_name)
    # controller.turn_on()
    controller.set_brightness(50)
    controller.set_color([0.1, 0.2])
