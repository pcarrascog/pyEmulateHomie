#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
import homie
import logging
import random
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TEMPERATURE_INTERVAL = 3

config = homie.loadConfigFile("homie-python.json")
Homie = homie.Homie(config)
temperatureNode = Homie.Node("temperature", "temperature")
humidityNode = Homie.Node("humidity", "humidity")
relayNode = Homie.Node("relay","relay")


def main():
    Homie.setFirmware("awesome-temperature", "1.0.0")
    temperatureNode.advertise("value")
    temperatureNode.advertise("unit")

    humidityNode.advertise("value")
    humidityNode.advertise("unit")

    relayNode.advertise("value")
    temperatureNode.advertise("unit")

    Homie.setup()

    while True:
        temperature = round(random.uniform(10, 30),2)
        humidity = round(random.uniform(10, 90),2)

        logger.info("Temperature: {:0.2f} °C".format(temperature))
        temperatureNode.setProperty("value").send(temperature)
        temperatureNode.setProperty("unit").send("c")
        logger.info("Humidity: {:0.2f} %".format(humidity))
        humidityNode.setProperty("value").send(humidity)
        humidityNode.setProperty("unit").send("%")

        relayNode.setProperty("value").send("off")

        time.sleep(TEMPERATURE_INTERVAL)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        logger.info("Quitting.")