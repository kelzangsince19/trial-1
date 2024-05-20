#def first repeating characters(S)
def find_first_repeating_characters(s):
    character_number = {}
    for i in character_number:
        if i in character_number:
            return i, id (i)
        else:
            character_number[i]  = True
    return None, None
#example usages
input_string = "hello"
repeating_numbers, memory_address = find_first_repeating_characters(input_string)
if repeating_numbers:
    print("first repeating character:",repeating_numbers)
else:
    print("no repeating character found.")      