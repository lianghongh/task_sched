from deap import base, creator
from deap import tools
from deap import algorithms
import numpy as np
import random,math

def number_generate():
    return random.randint(0,1)

def evalute(x):
    s = 0
    last = len(x) - 1
    for i in range(last, -1, -1):
        s += x[i] * 2 ** (last - i)
    d = 3 / 2 ** len(x)
    x=-1+s*d
    return x*math.sin(10*math.pi*x)+2,


def prepare(evalute_func):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    IND_SIZE = 8
    toolbox = base.Toolbox()
    toolbox.register("attribute", number_generate)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit,indpb=1)
    toolbox.register("select", tools.selTournament,tournsize=3)
    toolbox.register("evalute", evalute_func)
    stat = tools.Statistics(key=lambda x: x.fitness.values)
    stat.register('avg', np.mean)
    stat.register('std', np.std)
    stat.register('min', np.min)
    stat.register('max', np.max)
    return toolbox,stat


def doGA():
    toolbox,stat=prepare(evalute_func=evalute)
    pop=toolbox.population(n=50)
    cxpb,mutpb,ngen=0.8,0.01,50

    fitness=map(toolbox.evalute,pop)
    for ind,fit in zip(pop,fitness):
        ind.fitness.values=fit

    for g in range(ngen):
        offspring=toolbox.select(pop,len(pop))
        offspring=list(map(toolbox.clone,offspring))
        for child1,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random()<cxpb:
                toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values

        for mutant in offspring:
            if random.random()<mutpb:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        invild_ind=[ind for ind in offspring if not ind.fitness.valid]
        fitness=map(toolbox.evalute,invild_ind)
        for ind,fit in zip(invild_ind,fitness):
            ind.fitness.values=fit

        pop[:]=offspring
        log=stat.compile(pop)
        print(log)
    return pop

def prepare2(evalute_func):
    creator.create("FitnessMax", base.Fitness, weights=(1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMax)
    IND_SIZE = 8
    toolbox = base.Toolbox()
    toolbox.register("attribute", number_generate)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attribute, n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register("mate", tools.cxOnePoint)
    toolbox.register("mutate", tools.mutFlipBit, indpb=1)
    toolbox.register("select", tools.selRoulette)
    toolbox.register("evaluate", evalute_func)

    stat = tools.Statistics(key=lambda x: x.fitness.values)
    stat.register('avg', np.mean)
    stat.register('std', np.std)
    stat.register('min', np.min)
    stat.register('max', np.max)
    return toolbox, stat

def simpleGA():
    toolbox, stat = prepare2(evalute)
    pop = toolbox.population(n=50)
    p, logbook = algorithms.eaSimple(pop, toolbox, 0.8, 0.01, 100, stats=stat, verbose=False)
    print(logbook)


if __name__=='__main__':
    doGA()
