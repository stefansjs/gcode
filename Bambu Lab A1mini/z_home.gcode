; This is all copied from an orcaslicer-generated print file
M73 P0 R302
M73 C69
M201 X20000 Y20000 Z1500 E5000
M203 X500 Y500 Z30 E30
M204 P20000 R5000 T20000
M205 X9.00 Y9.00 Z5.00 E3.00 ; sets the jerk limits, mm/sec

; enable software endstops
M211 S1; enable software endstops
M120; enable endstops

; move to the top of the gantry
G90
G0 Z188 F1000
M400 S1

; disable endstops
M211 S0; disable software endstops
M121; disable endstops

; reset z position to the top of the gantry
G92 Z188

; Then move (slowly) down to z=100
G0 Z100 F250

; wait for moves to finish
M400 S1
