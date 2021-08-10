import numpy as np
import pandas as pd
import random
import operator
cities_list = ['city1' , 'city2' , 'city3' , 'city4' , 'city5','city6','city7','city8','city9','city10']
cities_all_distance=[[0,60,100,510,620,40,70,80,120,650],
                     [60,0,60,130,40,80,90,90,440,540],
                     [100,60,0,450,450,860,910,190,10,145],
                     [510,130,450,0,70,1500,440,220,660,250],
                     [620,40,450,70,0,260,160,330,120,50],
                     [40,80,860,1500,260,0,370,260,350,110],
                     [70,90,910,440,160,370,0,50,120,270],
                     [80,90,190,220,330,260,50,0,330,990],
                     [120,440,10,660,120,350,120,330,0,330],
                     [650,540,145,250,50,110,270,990,330,0]]
#It will return distance between two cities
def cities_distance(start,target):
    x=cities_list.index(start)
    y=cities_list.index(target)
    distance=cities_all_distance[x][y]
    return distance
#It will return a random route
def random_route(cities_list):
    random_city_route = random.sample(cities_list , len(cities_list))
    return random_city_route
#It will generate intial population
def initial_population(population_size , city_list):
    population = []
    for i in range(population_size):
        population.append(random_route(city_list))
    return population
#It will return the distance of the whole Path
def route_distance(route):
    city_route_distance=0
    for i in range(len(route)-1):
        city_route_distance +=cities_distance(route[i],route[i+1])
    return city_route_distance
#It will return the fitness of the route
def route_fitness(cities_list):
    total_distance = route_distance(cities_list)
    fitness = 1 / float(total_distance)
    return fitness
#It will return the top fitness so that we select for further breeding
def routes_fitness_probability(population, map_of_cities):
    fitness_results = {}
    for i in range(len(population)):
        fitness_results[i] = route_fitness(population[i])
    return sorted(fitness_results.items() , key=operator.itemgetter(1) , reverse=True)

#It will select the population on the basis of fitness
def selection(pop_ranked , elite_size):
    selection_results = []
    result = []
    for i in pop_ranked:
        result.append(i[0])
    for i in range(0 , elite_size):
        selection_results.append(result[i])
    return selection_results

#It will create new population
def mating_pool(population , selection_results):
    matting_pool = []
    for i in range(0 , len(selection_results)):
        index = selection_results[i]
        matting_pool.append(population[index])
    return matting_pool

def breed(parentA , parentB):
    child = []
    childPA = []
    childPB = []
    for i in range(0 , len(parentA)//2):
        childPA.append(parentA[i])
    for city in parentB:
        if city not in childPA:     
            childPB.append(city)
         
    child = childPA + childPB
    return child
    
#It will breed the population into childs
def breed_population(matting_pool):
    children = []
    for i in range(len(matting_pool) -1):
        children.append(breed(matting_pool[i] , matting_pool[i+1]))
    return children

#It will mutate the population
def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))
            city1 = individual[swapped]
            city2 = individual[swapWith]
            individual[swapped] = city2
            individual[swapWith] = city1
    return individual
#It will mutate the whole population
def mutate_population(population, mutationRate):
    mutatedPop = []
    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop
#It will generate the next generation by selectiong new generation and replaced it with previous one.
def next_generation(map_of_cities , current_population , mutation_rate , elite_size):
    pop_rank = routes_fitness_probability(current_population , map_of_cities)
    selection_results = selection(pop_rank , elite_size)
    matting_pool = mating_pool(current_population , selection_results)
    children = breed_population(matting_pool)
    next_generation = mutate_population(children , mutation_rate)
    return next_generation
#It is the main algorithm to give us the solution
def GA(city_lst, popSize, eliteSize, mutationRate, generations , map_of_city):
    init_pop = initial_population(popSize, city_lst)
    progress = []
    for i in range(generations):
        pop = next_generation(map_of_city , init_pop, mutationRate , eliteSize)
        progress.append(pop)
    bestRouteIndex = routes_fitness_probability(pop , map_of_city)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute

Shortest_Route=GA(cities_list, popSize=100, eliteSize=100, mutationRate=0.03, generations=100 ,map_of_city=cities_all_distance)
print(Shortest_Route)