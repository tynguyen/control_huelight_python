"""
@Brief: test device setup
"""

from control_huelight_python.devices import HueLight, HueBridgeController
import logging

logging.basicConfig(level=logging.DEBUG)


def test_setup_devices():
    """
    @Brief: test device setup
    """
    huelight1 = HueLight(name="Hue color lamp bedroom 1")
    huelight2 = HueLight(name="Hue color lamp 2")
    huecontroller = HueBridgeController(None, None)

    # Test the device connection
    is_connected = huecontroller.check_light_connection(huelight1)
    assert is_connected is True
    is_connected = huecontroller.check_light_connection(huelight2)
    assert is_connected is True


if __name__ == "__main__":
    test_setup_devices()
