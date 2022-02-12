from typing import Tuple, List, Union
from phue import Bridge as phue_Bridge
from control_huelight_python.utils import color_utils
import logging


class HueLight(object):
    def __init__(self, name: str = "Hue color lamp bedroom 1", id: int = 5) -> None:
        """ Initialize the HueLight object
        Args:
            name (str, optional): Name of the light that appear on the Hue app. Defaults to "Hue color lamp bedroom 1".
            id (int, optional): ID of the light defined by the Hue bridge. Defaults to 5.
        """
        super().__init__()
        self.name = name
        self.id = id
        self.phue_light = None  # Light() object from phue package


class HueBridgeController(object):
    def __init__(
        self,
        bridge_ip: str = "192.168.1.15",
        user_name="x-kHU4Ng800tNMpNIC51mF3l6V1bL9w4AuNB7-pI",
    ) -> None:
        """ Initialize the a Hue Bridge controller for multiple connected devices
        Args:
            bridge_ip (str, optional): IP address of the Hue bridge. Defaults to "192.168.1.15"
            user_name (str, optional): Your user name to log into the Hue bridge. Defaults to "x-kHU4Ng800tNMpNIC51mF3l6V1bL9w4AuNB7-pI".
        """
        super().__init__()
        self.bridge = phue_Bridge(bridge_ip, user_name)
        try:
            self.bridge.connect()
        except RuntimeError as e:
            print("Cannot connect")
            logging.error(e)
            return None
        # Connected lights that are already verified by the user
        self.verified_light_ids = []

    def check_light_connection(self, light: HueLight) -> bool:
        """ Check if the light is connected to the bridge. It will also fulfill missing information about the light
        Args:
            light (HueLight): Light to check
        Returns:
            bool: True if the light is connected to the bridge, False otherwise
        """
        connected = False
        if light.name is not None:
            for light_obj in self.bridge.lights:
                logging.debug(f"-> available light: {light_obj.name}")
                if light.name == light_obj.name:
                    light.id = light_obj.light_id
                    light.phue_light = light_obj
                    connected = True
                    self.verified_light_ids.append(light.id)
                    logging.debug(f"Light {light.name} is connected")
                    break
        elif light.id is not None:
            for light_obj in self.bridge.lights:
                if light.id == light_obj.light_id:
                    light.name = light_obj.name
                    light.phue_light = light_obj
                    connected = True
                    self.verified_light_ids.append(light.id)
                    logging.debug(f"Light {light.name} is connected")
                    break
        else:
            logging.error("Light must be given with either name or id. None is given!")
        return connected

    def set_light_temperature(
        self,
        light: HueLight,
        temp: int,
        brightness: int = 254,
        transition_time: int = 30,
    ) -> None:
        """ Set the temperature of a light
        Args:
            light (HueLight): Light to set
            temp (int): Color temperature in [154, 500]
            brightness (int, optional): Brightness of the light in [0, 254]. Defaults to 254.
            transition_time (int, optional): Transition time in [0, 65535]. Defaults to 3 seconds
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")

        logging.debug(f"Current light temperature: {light.phue_light.colortemp}")
        command = {
            "transitiontime": transition_time,
            "on": True,
            "ct": temp,
            "bri": brightness,
        }
        self.bridge.set_light(light.id, command)
        logging.debug(f"Set light temperature: {light.phue_light.colortemp}")

    def turn_light_on(self, light: HueLight) -> None:
        """ Turn on a light
        Args:
            light (HueLight): Light to turn on
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        light.phue_light.on = True

    def turn_light_off(self, light: HueLight) -> None:
        """ Turn off a light
        Args:
            light (HueLight): Light to turn off
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        light.phue_light.on = False

    def set_light_brightness(self, light: HueLight, brightness):
        """
        Set the brightness of a light
        Args:
            light (HueLight): Light to set
            brightness (int): Brightness of the light in [0, 254].
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        if not light.phue_light.on:
            light.phue_light.on = True
        # Transition: 5 seconds
        command = {"transitiontime": 50, "on": True, "bri": brightness}
        self.bridge.set_light(light.id, command)

    def increase_light_brightness(self, light: HueLight, step: int = 12) -> None:
        """
        Increase the brightness of a light by a step
        Args:
            light (HueLight): Light to increase
            step (int, optional): Step to increase the brightness. Defaults to 12.
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        if not light.phue_light.on:
            light.phue_light.on = True

        if light.phue_light.brightness + step >= 254:
            light.phue_light.brightness = 254
        else:
            light.phue_light.brightness += step

    def set_light_xy_color(
        self, light: HueLight, xy: Tuple, transition_time: int = 30
    ) -> None:
        """
        Set the color of a light in xy color space
        Args:
            xy (Tuple): Color in xy color space
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        if not light.phue_light.on:
            light.phue_light.on = True
        command = {"transitiontime": transition_time, "xy": xy}
        self.bridge.set_light(light.id, command)

    def set_light_rgb_color(
        self, light: HueLight, rgb: Tuple, transition_time: int = 30
    ) -> None:
        """
        Set the color of a light in rgb color space
        Args:
            rgb (tuple): Color in rgb color space
        """
        if not self.check_light_connection(light):
            raise RuntimeError(f"Light {light.name} is not connected")
        if not light.phue_light.on:
            light.phue_light.on = True

        if isinstance(rgb, str):
            rgb = color_utils.str_to_rgb(rgb)
        xy = color_utils.rgb_to_xy(rgb)
        command = {"transitiontime": transition_time, "xy": xy}
        self.bridge.set_light(light.id, command)
