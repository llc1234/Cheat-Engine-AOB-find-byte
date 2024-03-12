def find_string_differences(strings):
    if len(strings) < 2:
        print("Please provide at least two strings for comparison.")
        return

    split_strings = [s.split() for s in strings]

    min_length = min(len(s) for s in split_strings)

    modified_numbers = []

    for i in range(min_length):
        numbers_at_index = [s[i] for s in split_strings]

        if all(num == numbers_at_index[0] for num in numbers_at_index):
            modified_numbers.append(numbers_at_index[0])
        else:
            modified_numbers.append('??')

    modified_string = ' '.join(modified_numbers)

    print(modified_string)

strings = []

while True:
    inp = input("->")
    if inp == "start":
        find_string_differences(strings)
    else:
        strings.append(inp)