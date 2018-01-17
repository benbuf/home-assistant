""" 
Support for battery powered enocean actuators
enocean equipment profile: A5-20-01
"""

import logging

import voluptuous as vol

from homeassistant.components.enocean import *
from homeassistant.components.climate import (
    ClimateDevice,
    ATTR_CURRENT_TEMPERATURE, ATTR_AWAY_MODE, SERVICE_SET_AWAY_MODE, SERVICE_SET_TEMPERATURE)
from homeassistant.const import (
    TEMP_CELSIUS, CONF_DEVICES)

DEPENDENCIES = ['enocean']
_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Enocean actuator"""
    if discovery_info is None:
        return

    temp_unit = hass.config.units.temperature_unit

    devices = []

    for name, device_cfg in config[CONF_DEVICES].items():
        id = device_cfg[CONF_ID]
        name = device_cfg[CONF_NAME]
        devices.append(EnoceanActuator(id, name))

    add_devices(devices)


class EnoceanActuator(ClimateDevice):
    """ Representation of an Enocean battery powered actuator. EEP A5-20-01"""

    def __init(self, id, name):
        self.id = id
        self.name = name

