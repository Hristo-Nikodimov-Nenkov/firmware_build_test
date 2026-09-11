from .configuration import Configuration

configuration_files = {
    "controller":"/config/controller.json",
    "wifi":"/config/wifi.json",
    "deposit":"/config/deposit.json",
    "refills":"/config/auto_refills.json",
    "state_logger": "/config/state_logger.json",
    "status_led_strip":"/config/devices/gpio/status_led_strip.json",
    "valves":"/config/devices/gpio/valves.json",
    "water_contact_sensor":"/config/devices/gpio/water_contact_sensor.json",
    "atm_sensor":"/config/devices/i2c/atm_sensor.json",
    "dep_sensor":"/config/devices/i2c/dep_sensor.json",
    "ext_storage" : "/config/devices/spi/ext_storage.json",
}

configurations = {k: Configuration(v) for k, v in configuration_files.items()}
