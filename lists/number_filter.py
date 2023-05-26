n = int(input())
original_list = [int(input()) for _ in range(n)]
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

filtered = list()
command = input()

for i in original_list:
    filter_command = (
        (command == COMMAND_EVEN and i % 2 == 0) or
        (command == COMMAND_NEGATIVE and i < 0) or
        (command == COMMAND_POSITIVE and i >= 0) or
        (command == COMMAND_ODD and i % 2 != 0)
        )

    if filter_command:
        filtered.append(i)

print(filtered)
