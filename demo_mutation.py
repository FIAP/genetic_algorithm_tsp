# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:41:21 2023

@author: SérgioPolimante
"""

import random
import copy 
#### MUTATION ###
def mutate(solution, mutation_probability):

    mutated_solution = copy.deepcopy(solution)
    
    # Check if mutation should occur    
    if random.random() < mutation_probability:
        
        # Ensure there are at least two cities to perform a swap
        if len(solution) < 2:
            return solution
    
        # Select a random index (excluding the last index) for swapping
        index = random.randint(0, len(solution) - 2)
        
        
        
        # Swap the cities at the selected index and the next index
        mutated_solution[index], mutated_solution[index + 1] = solution[index + 1], solution[index]
    
        
        
    return mutated_solution
        
        
    
# Example usage:
original_solution =[(99, 100), (2, 50), (1, 71)]
mutation_probability = 1

mutated_solution = mutate(original_solution, mutation_probability)
print("Original Solution:", original_solution)
print("Mutated Solution:", mutated_solution)