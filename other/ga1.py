import random
from deap import base,tools,creator
from functools import partial
import numpy as np

def _generate_pe(max:int):
    return random.randint(0,max-1)


def _fitness(ind,graph):
    pass


def dosimpleGA(graph,pe_size,pop_size,cxpb,mutpb,ngen,select_factor):
    creator.create('FitnessMin',base.Fitness,weight=(-1.0,))
    creator.create('Individual',list,fitness=creator.FitnessMin)
    IND_SIZE=pe_size
    toolbox=base.Toolbox()
    toolbox.register('attribute',partial(_generate_pe,max=IND_SIZE))
    toolbox.register('individual',tools.initRepeat,creator.Individual,toolbox.attribute,n=IND_SIZE)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    toolbox.register('mate',tools.cxTwoPoint)
    toolbox.register('mutate',tools.mutUniformInt,low=0,up=IND_SIZE-1,indpb=1)
    toolbox.register('select',tools.selRoulette)
    toolbox.register('evalute',partial(_fitness,graph=graph))

    stat=tools.Statistics(key=lambda x:x.fitness.values)
    stat.register('avg',np.mean)
    stat.register('min',np.min)
    stat.register('max',np.max)

    pop=toolbox.population(n=pop_size)
    fitness=map(_fitness,pop)
    for ind,fit in zip(pop,fitness):
        ind.fitness.values=fit

    for g in range(ngen):
        offspring=toolbox.select(pop,int(len(pop)*select_factor))
        offspring=list(map(toolbox.clone,offspring))
        for child1,child2 in zip(offspring[::2],offspring[1::2]):
            if random.random()<cxpb:
                toolbox.mate(child1,child2)
                del child1.fitness.values
                del child2.fitness.values

        for mut in offspring:
            if random.random()<mutpb:
                toolbox.mutate(mut)
                del mut.fitness.values

        invild_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitness = map(toolbox.evalute, invild_ind)
        for ind, fit in zip(invild_ind, fitness):
            ind.fitness.values = fit

        pop[:] = offspring
        log=stat.compile(pop)
        print('Gen %d:   min:%.4f  max:%.4f  avg:%.4f' % (g,log['min'],log['max'],log['avg']))

    return pop


