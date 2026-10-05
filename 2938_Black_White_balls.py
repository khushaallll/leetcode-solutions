def minimumSteps(s: str) -> int:
    one_count = 0
    swaps = 0
    for bit in s:
        if bit == "1":
            one_count += 1

        if bit == "0":
            swaps = swaps + one_count

    return swaps 

        

s = "1010"
print(minimumSteps(s))