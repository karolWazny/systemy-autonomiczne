import random
import time

import influx_handler
DELAY = 120

cur_temp = 22
cur_hum = 30

if __name__ == "__main__":
    while True:
        cur_hum = int(cur_hum + random.random() * 5 - 2.5)
        cur_temp = float(cur_temp + random.random() * 3 - 1.5)
        influx_handler.write_measurement(measurement='pomiary',
                                         device_id='TEST',
                                         temp=cur_temp,
                                         hum=cur_hum)
        print(f"Temp: {cur_temp}, humidity: {cur_hum}")
        time.sleep(DELAY)
