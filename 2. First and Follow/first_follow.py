# =================================================================================================================== #
#                                              PROJECT FIRST AND FOLLOW                                               #
# =================================================================================================================== #
# Project: First and Follow                                                                                           #
# Developer: Miguel Marines                                                                                           #
# =================================================================================================================== #


# Libraries --------------------------------------------------------------------------------------------------------- #
import numpy as np
import copy


# =================================================================================================================== #
#                                   FUNCTION: ELIMINATE EPSILONS FROM GRAMAR                                          #
# =================================================================================================================== #
def function_eliminate_epsilons(grammar):

    # Copy grammar matrix.
    aux_matrix_grammar = copy.deepcopy(grammar)

    # Eliminate epsilons (spaces).
    for i in aux_matrix_grammar:
        for j in i:
            if len(j) == 1:
                if ord(j) == 39:
                    i.remove(j)
    
    for i in aux_matrix_grammar:
        for j in i:
            if len(j) == 1:
                if ord(j) == 39:
                    i.remove(j)
    
    # Initialize the epsilon's array.
    epsilons = []

    # Fill the epsilon's array with the epsilons.
    for i in aux_matrix_grammar:
        if(len(i) == 2):
            epsilons.append(i[0])

    # Initialize the new grammar's matrix.
    new_matrix_grammar = []

    # Fill the grammar's matrix without the productions that have epsilon.
    for i in aux_matrix_grammar:
        if(len(i) > 2):
            new_matrix_grammar.append(i)

    # Delete variable from production if it can be epsilon.
    for i in new_matrix_grammar:
        if(i[-1] in epsilons):
            i.pop()
    
    # Return new matrix grammar without epsilons and variables that can be epsilon.
    return new_matrix_grammar



# =================================================================================================================== #
#                                               FUNCTION: COMBINE MATRIX                                              #
# =================================================================================================================== #
def function_combine_matrix(matrix_1, matrix_2):
    
    # Copy the first matrix into the new matrix.
    matrix_3 = copy.deepcopy(matrix_1)

    # Copy the second matrix into the new matrix.
    for i in matrix_2:
        matrix_3.append(i)

    # Initialize the auxiliary array and the new matrix.
    aux_array = []
    new_matrix = []

    # Combine matrix.
    for i in range(len(final_array_no_terminals)):
        aux_array = np.concatenate((matrix_3[i], matrix_3[-(len(final_array_no_terminals))+i]))
        new_matrix.append(aux_array)

    # Return new matrix.
    return new_matrix


# =================================================================================================================== #
#                            FUNCTION: ELIMINATE SPACES AND REPEATED ELEMENTS FROM MATRIX                             #
# =================================================================================================================== #
def function_eliminate_spaces_repited(matrix):
    
    # Initialize the auxiliary array and the new matrix.
    aux_array = []
    new_matrix = []

    # Eliminate repeated elements and epsilons(spaces).
    for i in matrix:
        for j in i:
            if ((j not in aux_array) and (j != "' '")):
                aux_array.append(j)
        new_matrix.append(aux_array)
        aux_array = []
    
    # Return new matrix.
    return new_matrix


# =================================================================================================================== #
#                                                 FUNCTION: FIRSTS                                                    #
# =================================================================================================================== #
def function_first(matrix_grammar, final_array_terminals, final_array_no_terminals, evaluate_no_terminal):
    
    # Initialize the first array.
    array_first = []
    
    # Analyze the grammar one production at a time for firsts.
    for i in matrix_grammar:
        
        if(i[0] == evaluate_no_terminal):
            
            if(i[2] in final_array_terminals):
                array_first.append(i[2])
            
            if(i[2] in final_array_no_terminals):
                evaluate_no_terminal = i[2]
      
            if((i[2] not in final_array_no_terminals) and (i[2] not in final_array_terminals)):
                array_first.append("' '")

    # Initialize the final first array.
    final_array_first = []

    # Fill the final first array.
    for item in array_first:
        if item not in final_array_first:
            final_array_first.append(item)
    
    # Return the final first array.
    return final_array_first


# =================================================================================================================== #
#                                           FUNCTION: FOLLOW 1 (Rules 1 and 2)                                        #
# =================================================================================================================== #
def function_follow_1(matrix_grammar, final_array_no_terminals, evaluate_no_terminal, matrix_first):
    
    # Initialize arrays and matrices.
    array_follow = []
    aux_array_first = []
    aux_matrix_first = []
    aux_final_array_no_terminals = copy.deepcopy(final_array_no_terminals)

    # Assign the firsts to its no terminal.
    for i in matrix_first:
        aux_array_first.append(aux_final_array_no_terminals[0])
        aux_final_array_no_terminals.pop(0)

        for j in i:
            aux_array_first.append(j)
        
        aux_matrix_first.append(aux_array_first)
        aux_array_first = []

    # Add defoult follow to the first no termial.
    if(evaluate_no_terminal == final_array_no_terminals[0]):
        array_follow.append("$")
    
    # First 2 follow rules.
    for i in matrix_grammar:
        aux = copy.deepcopy(i)
        aux.pop(0)
        for j in aux:
            if((matrix_grammar.index(i)== 1) and (len(i) == 0)):
                if(j == final_array_no_terminals[0]):
                    array_follow.append("$")
                    print("dsfsfsa")
            if((j == evaluate_no_terminal) and (len(aux) - aux.index(j) > 1)):            
                nextelem = aux.index(j) + 1

                if(aux[nextelem] not in final_array_no_terminals):
                    array_follow.append(aux[nextelem])
                if(aux[nextelem] in final_array_no_terminals):
                    befelement = final_array_no_terminals.index(evaluate_no_terminal) - 1
                    for k in aux_matrix_first:
                        if(final_array_no_terminals[befelement] == k[0]):
                            aux_array_firsts = copy.deepcopy(k)
                            aux_array_firsts.pop(0)
                            for l in k:
                                array_follow.append(l)

    # Delete duplicates.
    final_array_follow = []
    for item in array_follow:
        if((item not in final_array_follow) and (item not in final_array_no_terminals)):
            final_array_follow.append(item)
    
    # Return array with follows.
    return final_array_follow


# =================================================================================================================== #
#                                           FUNCTION: FOLLOW 2 (Rule 3)                                               #
# =================================================================================================================== #
def function_follow_2(matrix_grammar, final_array_no_terminals, evaluate_no_terminal, matrix_follow):
    
    # Initialize arrays and matrices.
    array_follow = []
    aux_array_follow = []
    aux_matrix_follow = []
    aux_final_array_no_terminals = copy.deepcopy(final_array_no_terminals)

    # Assign the follows to its no terminal.
    for i in matrix_follow:
        aux_array_follow.append(aux_final_array_no_terminals[0])
        aux_final_array_no_terminals.pop(0)
        for j in i:
            aux_array_follow.append(j)
        aux_matrix_follow.append(aux_array_follow)
        aux_array_follow = []

    # 3th follow rule.
    for i in matrix_grammar:
        aux = copy.deepcopy(i)
        aux.pop(0)
        for j in aux:
            if((j == evaluate_no_terminal) and (j == aux[-1]) and (evaluate_no_terminal == aux[-1])):
                for k in aux_matrix_follow:
                    befelement = final_array_no_terminals.index(evaluate_no_terminal) - 1
                    aux_array_follow = copy.deepcopy(k)

                    if(final_array_no_terminals[befelement] == aux_array_follow[0]):
                        if(k[0] != final_array_no_terminals[-1]):
                            aux_array_follow.pop(0)
                            for l in k:
                                if(l not in final_array_no_terminals):
                                    array_follow.append(l)

    # Delete duplicates.
    final_array_follow = []
    for item in array_follow:
        if((item not in final_array_follow) and (item not in final_array_no_terminals)):
            final_array_follow.append(item)
    
    # Return array with follows.
    return final_array_follow











# =================================================================================================================== #
#                                        GRAMMAR AND TERMINALS AND NO TERMINALS                                       #
# =================================================================================================================== #

# Input of the number of lines to write.
number_lines = int(input())

# Initialize the gramar matrix.
matrix_grammar = []

# Initialize the terminal and no terminal arrays.
array_terminals = []
array_no_terminals = []

# Cicle to fill the terminal and no terminal arrays.
for i in range(number_lines):
    
    # User input
    user_input = input()
    production_array = user_input.split(" ")

    # Fill grammar matrix with grammar productions.
    matrix_grammar.append(production_array)

    # Fill no terminal array.
    array_no_terminals.append(production_array[0])
    
    # Fill terminal array.
    for j in range(len(production_array)):
        if (j > 1):
            array_terminals.append(production_array[j])


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


# =================================================================================================================== #
#                                       PRINT GRAMMAR, TERMINALS AND NO TERMINALS                                     #
# =================================================================================================================== #
# Terminals --------------------------------------------------------------------------------------------------------- #
# print()
# print("Terminal:", end = ' ')
# print(*final_array_terminals, sep=", ")

# No Terminals ------------------------------------------------------------------------------------------------------ #
# print("None Terminal:", end = ' ')
# print(*final_array_no_terminals, sep=", ")

# Gramar ------------------------------------------------------------------------------------------------------------ #
# print()
# print("Gramar:")
# print(matrix_grammar)


# =================================================================================================================== #
#                                                       FIRSTS                                                        #
# =================================================================================================================== #
# Initialize the first array and matrix.
array_first = []
matrix_first = []

# Cicle to analyze for each no terminal the firsts.
for i in final_array_no_terminals:
    evaluate_no_terminal = i
    array_first = function_first(matrix_grammar, final_array_terminals, final_array_no_terminals, evaluate_no_terminal)
    matrix_first.append(array_first)

# =================================================================================================================== #
#                                                     PRINT FIRSTS                                                    #
# =================================================================================================================== #
# Firsts ------------------------------------------------------------------------------------------------------------ #
# print()
# print("Firsts:")
# print(matrix_first)


# =================================================================================================================== #
#                                                       FOLLOWS                                                       #
# =================================================================================================================== #
# Initialize arrays and matrices.
array_follow = []
matrix_follow_1 = []
matrix_follow_2 = []

# Follow function 1.
for i in final_array_no_terminals:
    evaluate_no_terminal = i
    array_follow = function_follow_1(matrix_grammar, final_array_no_terminals, evaluate_no_terminal, matrix_first)
    matrix_follow_1.append(array_follow)

# Follow function 2.
for i in final_array_no_terminals:
    evaluate_no_terminal = i
    final_array_follow = function_follow_2(matrix_grammar, final_array_no_terminals, evaluate_no_terminal, matrix_follow_1)
    matrix_follow_2.append(final_array_follow)

# Combine matrix.
final_matrix_follow_1 = function_combine_matrix(matrix_follow_1, matrix_follow_2)


# =================================================================================================================== #
#                                     FOLLOWS TAKE INTO ACOUNT THE EPSILONS                                           #
# =================================================================================================================== #
# Eliminate epsilons from grammar. 
final_matrix_grammar = function_eliminate_epsilons(matrix_grammar)
final_matrix_grammar = function_eliminate_epsilons(final_matrix_grammar)

# Initialize matrix.
matrix_follow_3 = []

# Follow function 2.
for i in final_array_no_terminals:
    evaluate_no_terminal = i
    final_array_follow = function_follow_2(final_matrix_grammar, final_array_no_terminals, evaluate_no_terminal, final_matrix_follow_1)
    matrix_follow_3.append(final_array_follow)

# Combine matrix.
final_matrix_follow_2 = function_combine_matrix(final_matrix_follow_1, matrix_follow_3)


# =================================================================================================================== #
#                                          FOLLOWS CICLE TO GET ALL FOLLOWS                                           #
# =================================================================================================================== #
# Initialize matrix.
final_matrix_follow_3 = copy.deepcopy(final_matrix_follow_2)

# Follow function 2.
for i in range(len(final_array_no_terminals)):
    
    # Initialize matrix.
    matrix_follow_4 = []
    
    # Follow function 2.
    for i in final_array_no_terminals:
        evaluate_no_terminal = i
        final_array_follow = function_follow_2(matrix_grammar, final_array_no_terminals, evaluate_no_terminal, final_matrix_follow_3)
        matrix_follow_4.append(final_array_follow)

    # Combine matrix.
    final_matrix_follow_3 = function_combine_matrix(final_matrix_follow_2, matrix_follow_4)
    final_matrix_follow_3 = copy.deepcopy(final_matrix_follow_3)

# Initialize matrix.
matrix_follow_5 = []

# Follow function 2.
for i in final_array_no_terminals:
    evaluate_no_terminal = i
    final_array_follow = function_follow_2(final_matrix_grammar, final_array_no_terminals, evaluate_no_terminal, final_matrix_follow_3)
    matrix_follow_5.append(final_array_follow)

# Combine matrix.
final_matrix_follow_4 = function_combine_matrix(final_matrix_follow_3, matrix_follow_5)

# Eliminate spaces and repited elements form matrix.
final_matrix_follow = function_eliminate_spaces_repited(final_matrix_follow_4)


# =================================================================================================================== #
#                                                    PRINT FOLLOWS                                                    #
# =================================================================================================================== #
# Follows ----------------------------------------------------------------------------------------------------------- #
# print()
# print("Follows:")
# print(final_matrix_follow)


# =================================================================================================================== #
#                                             PRINT FIRST AND FOLLOWS                                                 #
# =================================================================================================================== #
# First and Follows ------------------------------------------------------------------------------------------------- #
print()
for i in range(len(final_array_no_terminals)):

    print(final_array_no_terminals[i], end = ' ')
    print("=> FIRST = {", end = ' ')
    print(*matrix_first[i], sep=", ", end = ' ')
    print("}, FOLLOW = {", end = ' ')
    print(*final_matrix_follow[i], sep=", ", end = ' ')
    print("}")
   
    # print(final_array_no_terminals[i], " => FIRST = {", *matrix_first[i], "}, FOLLOW = {", *final_matrix_follow[i], "}" )
print()