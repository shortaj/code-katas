"""Takes in a list of inputs and returns a list of the largest set of related elements."""

def conveyor_search(input_list):
    """Return the largest group of related unique elements."""
    belt = list(input_list)
    output = []
    while True:
        if not belt:
            return output
        temp = belt[0]
        set_counter = 1
        counter = 0
        if len(list(set(temp))) > len(output):
            output = list(set(temp))
        while True:
            if set_counter > len(belt):
                break
            try:
                if temp[counter] in belt[set_counter]:
                    temp.extend(belt[set_counter])
                    temp = list(set(temp))
                    if len(list(set(temp))) > len(output):
                        output = list(set(temp))
                    set_counter += 1
                    counter = 0
                else:
                    counter += 1
            except IndexError:
                set_counter += 1
                counter = 0
        belt.pop(0)