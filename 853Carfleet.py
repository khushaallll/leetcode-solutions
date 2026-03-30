target = 100
position = [0,2,4]
speed = [4,2,1]

def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    fleet = 0
    prev_time = 0

    pos_speed_pairs = sorted(zip(position, speed), reverse=True)

    for pos, spee in pos_speed_pairs:
        current_time = (target-pos)/spee

        if current_time > prev_time:
            fleet += 1
            prev_time = current_time
            
    return fleet
        
print(carFleet(target, position, speed))