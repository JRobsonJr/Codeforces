# 29B: Traffic Lights

l, d, v, g, r = map(int, input().split())
total_time = l / v

def next_green(time, g, r):
    start_green = 0
    end_green = g
    while True:
        if time < end_green:
            return start_green, end_green
        else:
            start_green = end_green + r
            end_green = start_green + g

def is_green_at_time(time, g, r):
    start_green, end_green = next_green(time, g, r)
    return start_green <= time < end_green

if is_green_at_time(d / v, g, r):
    print(l / v)
else:
    start_green, end_green = next_green(d / v, g, r) 
    print(l / v + start_green - d / v)