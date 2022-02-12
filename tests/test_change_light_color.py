"""
@Brief: test changing colormode, color, temporature and brightness of a light
"""

from control_huelight_python.devices import HueLight, HueBridgeController
from control_huelight_python.utils import color_utils
import logging
import time

logging.basicConfig(level=logging.INFO)


def test_change_color_and_colortemperature_continuously():
    huelight1 = HueLight(name="Hue color lamp bedroom 1")
    huecontroller = HueBridgeController(None, None)
    huecontroller.check_light_connection(huelight1)
    # Change color of the light from blue -> cyan -> green -> yellow -> orange -> red -> violet -> magenta -> blue
    # For each color, change the color temperature from cool to warm in 5 steps, stay 2 seconds between each step

    colors = [
        "blue",
        "cyan",
        "green",
        "yellow",
        "orange",
        "red",
        "violet",
        "magenta",
        "blue",
    ]
    for color_name in colors:
        for warm_percent in range(10, 100, 10):
            color = color_utils.pick_rgb_color_by_name(
                color_name,
                warmness_percentage=warm_percent / 100.0,
                brightness_percentage=1,
            )
            logging.info(
                f"Set the color of light 1 to {color_name}, warm {warm_percent}%"
            )

            huecontroller.set_light_rgb_color(huelight1, color, transition_time=10)
            time.sleep(2)


def test_change_color_and_colortemperature():
    huelight1 = HueLight(name="Hue color lamp bedroom 1")
    huelight2 = HueLight(name="Hue color lamp 2")
    huecontroller = HueBridgeController(None, None)
    huecontroller.check_light_connection(huelight1)
    huecontroller.check_light_connection(huelight2)

    # Change the color to warm orange
    color_name = "orange"
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.8, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight1, color, transition_time=10)
    logging.info(
        f"Set the color of light 1 to {color_name}: {huelight1.phue_light.xy} ~ {color}"
    )
    # Change the color to cool orange
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.2, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight2, color, transition_time=10)
    logging.info(
        f"Set the color of light 2 to {color_name}: {huelight2.phue_light.xy} ~ {color}"
    )
    time.sleep(12)

    # Change the color to warm cyan
    color_name = "cyan"
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.8, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight1, color, transition_time=10)
    logging.info(
        f"Set the color of light 1 to {color_name}: {huelight1.phue_light.xy} ~ {color}"
    )
    # Change the color to cool cyan
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.2, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight2, color, transition_time=10)
    logging.info(
        f"Set the color of light 2 to {color_name}: {huelight2.phue_light.xy} ~ {color}"
    )
    time.sleep(12)

    # Change the color to warm magenta
    color_name = "magenta"
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.8, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight1, color, transition_time=10)
    logging.info(
        f"Set the color of light 1 to {color_name}: {huelight1.phue_light.xy} ~ {color}"
    )
    # Change the color to cool magenta
    color = color_utils.pick_rgb_color_by_name(
        color_name, warmness_percentage=0.2, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight2, color, transition_time=10)
    logging.info(
        f"Set the color of light 2 to {color_name}: {huelight2.phue_light.xy} ~ {color}"
    )
    time.sleep(12)

    # Change the color to warm blue
    warm_blue = color_utils.pick_rgb_color_by_name(
        "blue", warmness_percentage=0.8, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight1, warm_blue, transition_time=10)
    logging.info(
        f"Set the color of light 1 to warm blue: {huelight1.phue_light.xy} ~ {warm_blue}"
    )
    # Change the color to cool blue
    # cool_blue = color_utils.set_rgb_color_warmness(color, 0.7)
    cool_blue = color_utils.pick_rgb_color_by_name(
        "blue", warmness_percentage=0.2, brightness_percentage=0.8
    )
    huecontroller.set_light_rgb_color(huelight2, cool_blue, transition_time=10)
    logging.info(
        f"Set the color of light 2 to cool blue: {huelight2.phue_light.xy} ~ {cool_blue}"
    )
    time.sleep(12)

    # Change the color to warm red
    # color = "red"
    # warm_red = color_utils.set_rgb_color_warmness(color, 1)
    warm_red = color_utils.pick_rgb_color_by_name("red", warmness_percentage=0.8)
    huecontroller.set_light_rgb_color(huelight1, warm_red)
    logging.info(
        f"Set the color of light 1 to warm red: {huelight1.phue_light.xy} ~ {warm_red}"
    )
    time.sleep(6)
    # Change the color to cool red
    # cool_red = color_utils.set_rgb_color_warmness(color, 0.5)
    cool_red = color_utils.pick_rgb_color_by_name("red", warmness_percentage=0.2)
    huecontroller.set_light_rgb_color(huelight2, cool_red)
    logging.info(
        f"Set the color of light 2 to cool red: {huelight2.phue_light.xy} ~ {cool_red}"
    )
    time.sleep(6)


def test_change_colortemperature():
    """
    @Brief: test changing the color temperature of a light
    """
    huelight1 = HueLight(name="Hue color lamp bedroom 1")
    huelight2 = HueLight(name="Hue color lamp 2")
    huecontroller = HueBridgeController(None, None)
    huecontroller.check_light_connection(huelight1)
    huecontroller.check_light_connection(huelight2)

    # Change color
    # Change color of the light 1 to red
    color = "red"
    huecontroller.set_light_rgb_color(huelight1, color)
    logging.info(f"Set the color of light 1 to {huelight1.phue_light.xy} ~ {color}")
    time.sleep(5)

    # Change color of the light 2 to warm blue
    color = "warm_blue"

    # Change temp of the light 1 to 154 (smallest)
    logging.info("Current temperature of light 1: %s", huelight1.phue_light.colortemp)
    temp = 154
    logging.info("Current temperature of light 1: %s", huelight1.phue_light.colortemp)
    huecontroller.set_light_temperature(huelight1, temp)
    logging.info(f"Set temperature of light 1 to {huelight1.phue_light.colortemp}")
    time.sleep(5)
    # Set temperature of light 1 to 500
    temp = 500
    huecontroller.set_light_temperature(huelight1, temp)
    logging.info(f"Set temperature of light 1 to {huelight1.phue_light.colortemp}")
    time.sleep(5)

    # Change temp of the light 2 to 154 (smallest)
    temp = 154
    logging.info("Current temperature of light 2: %s", huelight2.phue_light.colortemp)
    huecontroller.set_light_temperature(huelight2, temp)
    logging.info(f"Set temperature of light 2 to {huelight2.phue_light.colortemp}")

    # Change temp of the light 2 to 500 (max)
    temp = 500
    huecontroller.set_light_temperature(huelight2, temp)
    logging.info(f"Set temperature of light 2 to {huelight2.phue_light.colortemp}")
    time.sleep(5)

    # Change color of the light 2 to green
    color = "green"
    huecontroller.set_light_rgb_color(huelight2, color)
    logging.info(f"Set the color of light 2 to {huelight2.phue_light.xy} ~ {color}")
    time.sleep(5)

    # Set brightness to 30%
    brightness = 84
    huecontroller.set_light_brightness(huelight1, brightness)
    logging.info(f"Set the brightness of light 1 to {huelight1.phue_light.brightness}")

    # Increase brightness of light 1 to 100%
    while huelight1.phue_light.brightness < 254:
        huecontroller.increase_light_brightness(huelight1)
        logging.info(
            f"Increase brightness of light 1 to {huelight1.phue_light.brightness}"
        )
        time.sleep(2)


if __name__ == "__main__":
    # test_change_colortemperature()
    # test_change_color_and_colortemperature()
    test_change_color_and_colortemperature_continuously()
