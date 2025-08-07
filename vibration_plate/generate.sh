#!/bin/bash

set -ex

./shake_plate.py -x -13.5 -z 100 -y 89 -d 2 -s 1000 shake_slow.gcode
./shake_plate.py -x -13.5 -z 100 -y 89 -d 2 -s 2500 shake_medium.gcode
./shake_plate.py -x -13.5 -z 100 -y 89 -d 2 --progress-multiplier-ms=70 shake_1m.gcode
./shake_plate.py -x -13.5 -z 100 -y 89 -d 2 --progress-multiplier-ms=70 -i 10_000 shake_10m.gcode
./shake_plate.py -x -13.5 -z 100 -y 89 -d 2 --progress-multiplier-ms=70 -i 51_500 shake_1h.gcode
./shake_plate.py -x -13.5 -z 100 -y 90 -d 1 shake_plate

gzip -kf *.gcode
