# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB, BC = map(int,(input(),input()))
angle_rad = math.atan2(AB, BC)
angle_deg = math.degrees(angle_rad)
print(f'{round(angle_deg)}\u00b0')
