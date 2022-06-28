import csv
import random
import time
from datetime import datetime

idx = 0
current_time = datetime.now().strftime("%H:%M:%S") 
oob = 1

fieldnames = ["idx", "time", "OOB"]


with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            "idx": idx,
            "time": current_time,
            "OOB": oob
        }

        csv_writer.writerow(info)
        print(idx, current_time, oob)

        idx += 1
        current_time = datetime.now().strftime("%H:%M:%S") 
        oob = oob + random.uniform(-0.2, 0.3)
        if idx%10 == 0 and oob > 8:
            oob -= 0.3

    time.sleep(1)
