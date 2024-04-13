# ====================================== #
# Developer: Miguel Marines              #
# Activity: Terminals and Non-Terminals  #
# ====================================== #

# Input of the number of lines to write.
number_lines = int(input())


# Initialize the terminal and no terminal arrays.
array_terminals = []
array_no_terminals = []


# Cicle to fill the terminal and no terminal arrays.
for i in range(number_lines):
    
    # User input
    user_input = input()
    string_array = user_input.split(" ")

    # Fill no terminal array.
    array_no_terminals.append(string_array[0])
    
    # Fill terminal array.
    for j in range(len(string_array)):
        if (j > 1):
            array_terminals.append(string_array[j])


# Initialize the auxiliary terminal and final no terminal arrays.
aux_array_terminals = []
final_array_no_terminals = []


# Remove duplicate elements.
for item in array_terminals:
    if item not in aux_array_terminals:
        aux_array_terminals.append(item)

for item in array_no_terminals:
    if item not in final_array_no_terminals:
        final_array_no_terminals.append(item)


# Remove no terminals from the terminals array.
for item in aux_array_terminals:
    if len(item) == 1:
        if ord(item) == 39:
            aux_array_terminals.remove(item)


# Initialize final terminal array.
final_array_terminals = []


# Remove no terminals from the terminals array.
for item in aux_array_terminals:
    if item not in final_array_no_terminals:
        final_array_terminals.append(item)


# Removes spaces if needed
final_array_terminals = ' '.join(final_array_terminals).split()


# Print result.
print()
print("Terminal: ", end = ' ')
print(*final_array_terminals, sep=", ")

print("None Terminal: ", end = ' ')
print(*final_array_no_terminals, sep=", ")
print()
