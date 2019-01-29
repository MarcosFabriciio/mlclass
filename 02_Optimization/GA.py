import numpy, requests, json

def cal_pop_fitness(equation_inputs, pop):
    # Calculating the fitness value of each solution in the current population.
    # The fitness function calulates the sum of products between each input and its corresponding weight.
    fitness = []
    angle = []
    for dude in pop:
        for i in range(6):
            angle.append(str(int(dude[i])%360))
        url = 'https://aydanomachado.com/mlclass/02_Optimization.php?phi1='+ angle[0] +'&theta1='+ angle[1] +'&phi2='+ angle[2] +'&theta2='+ angle[3] +'&phi3='+ angle[4] +'&theta3='+ angle[5] + '&dev_key=Ponte de Safena' 
        fitness.append(json.loads(requests.get(url).text)['gain'])

    return numpy.array(fitness)

def select_mating_pool(pop, fitness, num_parents):
    # Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
    parents = numpy.empty((num_parents, pop.shape[1]))
    for parent_num in range(num_parents):
        max_fitness_idx = numpy.where(fitness == numpy.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = pop[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999
    return parents

def crossover(parents, offspring_size):
    offspring = numpy.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually, it is at the center.
    crossover_point = numpy.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        random_value = int(numpy.random.uniform(-360, 360))
        offspring_crossover[idx, 4] = (offspring_crossover[idx, 4] + random_value) % 361
    return offspring_crossover
