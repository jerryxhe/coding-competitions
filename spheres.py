# https://www.hackerrank.com/challenges/spheres

n = int(raw_input())
def find_if_will_intersect(initial_pos_1, initial_pos_2, initial_accel_1, initial_accel_2, radius_1, radius_2):
    critical_distance = radius_1+radius_2
    
    
for _ in xrange(n):
    [radius_1, radius_2]=map(int, raw_input().split(" "))
    initial_pos_1 = map(int, raw_input().split(" "))
    initial_accel_1 = map(int, raw_input().split(" "))
    initial_pos_2 = map(int, raw_input().split(" "))
    initial_accel_2 = map(int, raw_input().split(" "))
