#!/usr/bin/env python

"""
Generates a .gcode file for using a bed-slinger as a vibration plate
"""

from pathlib import Path


def main(output_path, distance, speed, acceleration, iterations, start_y, start_x=None, start_z=None,
         progress_multiplier=None,
         **kwargs):
    progress = 0

    startup_gcode = f"""
M73 P0  ; set progress to 0%
G28 X Y ; Home the x and y axes
                 
G90
M201 Y{acceleration}; set max acceleration
; M203 Y10000; set max speed
; M204 P20000 R5000 T20000 ; set starting acceleration
G1 F{speed} ; set the speed for every future move

; do the vibratiosn for {iterations} iterations
"""
    
    end_gcode = """
M400
M73 P100
; done
"""

    with output_path.open('wt') as fh:
        fh.write(startup_gcode)

        fh.write(f"G1 Y{start_y}")
        if start_x is not None:
            fh.write(f" X{start_x}")
        if start_z is not None:
            fh.write(f" Z{start_z}")
        fh.write("\n")
        
        for iter in range(iterations):
            # write move commands
            fh.write(f"""
  ; iteration {iter}
  G1 Y{start_y+distance}
  G1 Y{start_y}
""")
            
            #write progress
            progress = int(100 * iter / iterations)
            fh.write(f"  M73 P{progress}")
            if progress_multiplier:
                time_remaining_ms = progress_multiplier * iter / iterations
                fh.write(f" R{int(time_remaining_ms / 1000 / 60)}\n")
            else:
                fh.write("\n")

        fh.write(end_gcode)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('output_path', type=Path)
    parser.add_argument('--distance', '-d', default=10, type=int, help="(ms) total y motion to shake the bed")
    parser.add_argument('--iterations', '-i', default=1000, type=int, help='number of vibration iterations')
    parser.add_argument('--speed', '-s', default=10_000, type=int, help='speed in stepper motor units')
    parser.add_argument('--acceleration', '-a', default=10_000, type=int, help='acceleration in stepper motor units')
    parser.add_argument('--start-x', '-x', default=None, type=float)
    parser.add_argument('--start-y', '-y', default=90, type=float)
    parser.add_argument('--start-z', '-z', default=120, type=float)
    parser.add_argument('--progress-multiplier-ms', '-p', type=float, help='iteration duration in ms')
    # parser.add_argument('--steps-per-mm', )
    args = parser.parse_args()

    main(**vars(args))
