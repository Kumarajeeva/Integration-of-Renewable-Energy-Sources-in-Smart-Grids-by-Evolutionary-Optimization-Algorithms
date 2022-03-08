# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:01:20 2019

@author: Jeeva
"""
import numpy


a= numpy.random.uniform(low=0, high=1, size=(5,1))
b=[[2],[2],[2],[3],[3]]
c=numpy.random.uniform(low=140,high=250,size=(5,1))
num_chromosomes = 5
num_weights = 3

new_population = numpy.concatenate((a,b,c),axis=1)
print("Initial Population")
print(new_population)

def pop_function(f,p):
    # Calculating the function value of each solution in the current population.
    function=(0.5*(1-(f)))+(0.5*(numpy.divide(500,p)))
    return function

function= pop_function(a,c)
print('FITNESS')
print(function)



num_generations = 8
for generation in range(num_generations):
    print("Generation : ", generation)
    

    parents = numpy.empty((num_chromosomes, new_population.shape[1]))
    for parent_num in range(num_chromosomes):
        max_function = numpy.where(function == numpy.max(function))
        max_function = max_function[0][0]
        parents[parent_num, :] = new_population[max_function, :]
        function[max_function] = -99999999999
    selectedparents=parents[0:4]
    elitism=parents[0:2]
    parentformutation=parents[4]
    print('EVALUATION')
    print(parents)
    print('Selected parents')
    print(selectedparents)

    pop_size=(5,3)
    offspring_size=(pop_size[0]-selectedparents.shape[0], num_weights)


    offspring1 = numpy.empty(offspring_size)
    offspring2 = numpy.empty(offspring_size)
    
    crossover_point = 1

    for k in range(offspring_size[0]):
        
        parent1_idx = k%selectedparents.shape[0]
        
        parent2_idx = (k+1)%selectedparents.shape[0]
        
        offspring1[k, 0:crossover_point] = selectedparents[parent1_idx, 0:crossover_point]
        
        offspring1[k, crossover_point:] = selectedparents[parent2_idx, crossover_point:]

        parent3_idx = (k+2)%selectedparents.shape[0]
        
        parent4_idx = (k+3)%selectedparents.shape[0]
        
        offspring2[k, 0:crossover_point] = selectedparents[parent3_idx, 0:crossover_point]
        
        offspring2[k, crossover_point:] = selectedparents[parent4_idx, crossover_point:]

    offspring=numpy.vstack((offspring1,offspring2))
    print('Offsprings after Crossover')
    print(offspring)        


    mutationrate=0.5
    r=numpy.random.uniform(0,0.5,1)
    random_value = numpy.random.uniform(0, 1.0, 1)
    
    if r<mutationrate:
        mutate=numpy.random.uniform(0.6,1.0,1)
        parentformutation[0] = random_value
        parentformutation[2] = mutate*250

    print('After Mutation')        
    print(parentformutation)

    new_population=numpy.vstack((elitism,offspring,parentformutation))

    print('New Population')
    print(new_population)
    
    gene1=new_population[:,0]
    gene3=new_population[:,2]
    function=pop_function(gene1,gene3)
    print('function')
    print(function)
    
# Obtaining the best solution after finishing all generations.

best_individual = numpy.where(function == numpy.max(function))

print("Best solution : ", new_population[best_individual, :])
