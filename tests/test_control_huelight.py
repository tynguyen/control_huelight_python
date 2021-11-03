import logging
from control_huelight_python import control
import time


def test_control_huelight():
    # Send encouragement to user
    logging.info("Setting Encourage mood...")
    control.set_encouragement_mood()
    logging.info("Set Encourage mood. Sleep for 5 seconds")
    time.sleep(5)
    logging.info("Setting Speedup mood...")
    control.set_super_performance_mood()
    logging.info("Set Speedup mood. Sleep for 5 seconds")
    time.sleep(5)
    control.set_fresh_mood()
    logging.info("Set fresh mood. Sleep for 5 seconds")
    time.sleep(5)
    logging.info("Completed tests")
    # control.set_modern_mood()
    # logging.info("Set modern mood. Sleep for 5 seconds")
    # time.sleep(5)


if __name__ == "__main__":
    test_control_huelight()
