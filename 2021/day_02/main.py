FORWARD = "forward"
DOWN    = "down"
UP      = "up"

def instruction(s):
    action, number = s.split()
    return action, int(number)

def part1(commands):
    x = y = 0
    for command in commands:
        action, number = instruction(command)
        if action == FORWARD:
            x += number
        elif action == DOWN:
            y += number
        elif action == UP:
            y -= number

    print(x*y)

def part2(commands):
    x = y = aim = 0
    for command in commands:
        action, number = instruction(command)
        if action == FORWARD:
            x += number
            y += number*aim
        elif action == DOWN:
            aim += number
        elif action == UP:
            aim -= number

    print(x*y)

if __name__ == "__main__":
    with open("input.txt") as f:
        commands = [command for command in f.read().splitlines()]

    part1(commands)
    part2(commands)
