# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:19:37 2023

@author: SérgioPolimante
"""

import random

def order_crossover(parent1, parent2):
    length = len(parent1)
    
    # Choose two random indices for the crossover
    start_index = random.randint(0, length - 1)
    end_index = random.randint(start_index + 1, length)
    
    start_index, end_index = 0, 3

    print (start_index, end_index)
    # Initialize the child with a copy of the substring from parent1
    child = parent1[start_index:end_index]

    # Fill in the remaining positions with genes from parent2
    remaining_positions = [i for i in range(length) if i < start_index or i >= end_index]
    print(remaining_positions)
    remaining_genes = [gene for gene in parent2 if gene not in child]
    print(remaining_genes)

    for position, gene in zip(remaining_positions, remaining_genes):
        child.insert(position, gene)

    return child


# # Example usage:
# parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# parent2 = [9, 3, 7, 8, 2, 6, 5, 1, 4]

# child = order_crossover(parent1, parent2)
# print("Parent 1:", [0, 1, 2, 3, 4, 5, 6, 7, 8])
# print("Parent 1:", parent1)
# print("Parent 2:", parent2)
# print("Child   :", child)


# Example usage:
parent1 = [(1, 1), (2, 2), (3, 3), (4,4), (5,5), (6, 6)]
parent2 = [(6, 6), (5, 5), (4, 4), (3, 3),  (2, 2), (1, 1)]

# parent1 = [1, 2, 3, 4, 5, 6]
# parent2 = [6, 5, 4, 3, 2, 1]


child = order_crossover(parent1, parent2)
print("Parent 1:", [0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Child   :", child)


