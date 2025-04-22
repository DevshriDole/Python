def remove_repeats(input_string):
    result = ""
    seen = set()
    for char in input_string:
        if char not in seen:
            seen.add(char)
            result += char
    return result

input_string = "laptop"
output = remove_repeats(input_string)
print("output: ", output)

