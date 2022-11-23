import numpy as np
import matplotlib.pyplot as plt

from population import *
from gray2real import *
from fitness import *
from selection import *
from crossover import *
from mutation import *
from newindiv import *

def main():
    #create initial population
    n = 32   #num. of individuals
    c_len = 32 #length of chromosome
    g_len = 8  #length of genes
    pop = population(n,c_len)
    #print("initial pop. ", pop)
    #######################################
    print("* Genetic Algorithm *")
    print("Population size:\t",n)
    print("Chromosome length:\t",c_len)
    bestfits_g = []
    maxgen = int(input("number of generations: ")) #int(input("Number of generations: \t"))
    for g in range(maxgen):
        fit = []
        for indiv in pop:
            fit.append(fitness(gray2real(indiv)))

        #print("pop. fitness", fit)
        #print("min. fitness", np.min(fit))
        #print("max. fitness", np.max(fit))
        #print("mean fitness", np.mean(fit))
        #print("std_dev fitness", np.std(fit))
        
        
        fit_index = selection(fit)
        parent0 = pop[fit_index]
        #print(fit_index)
        #print("par0: ",parent0)
        
        fit_index = selection(fit)
        parent1 = pop[fit_index]
        
        while parent1 == parent0:
            fit_index = selection(fit)
            parent1 = pop[fit_index]
        
        #print(fit_index)
        #print("Par1: ",parent1)
        
        offspring0, offspring1= crossover(parent0, parent1)
        
        offspring0 = mutation(offspring0)
        offspring1 = mutation(offspring1)
    
    #print("off0: ",offspring0)
    #print("off1: ",offspring1)

        fitp0 = fitness(gray2real(parent0))
        fitp1 = fitness(gray2real(parent1))
        fito0 = fitness(gray2real(offspring0))
        fito1 = fitness(gray2real(offspring1))
        
    
        newpop= []
    
        if fito0 >= fitp0 or fito0 >= fitp1:
            newpop.append(offspring0)
        if fito1 >= fitp0 or fito1 >= fitp1:
            newpop.append(offspring1)
        if fitp0 >= fito0 and fitp0 >= fito1:
            newpop .append(parent0)
        if fitp1 >= fito0 and fitp1 >= fito1:
            newpop.append(parent1)
    
        bestfit = max(fit)
        
        #print(bestfit)
        bestindex = fit.index(bestfit)
        bestfits_g.append(1/bestfit)
        newpop.append(pop[bestindex])
        meanfit = np.mean(fit)
        stddevfit = np.std(fit)
        for i in range (len(fit)):
            if fit[i] > meanfit + stddevfit:
                newpop.append(pop[i])
    
        while(len(newpop)<n):
            newpop.append(newindiv(c_len))
    
        pop = newpop

    bestfit = max(fit)
    bestindex = fit.index(bestfit)
    sol = gray2real(pop[bestindex])
    print(f"W: {round(sol[0],1)}μm L: {round(sol[1],1)}μm  m: {sol[2]} n: {sol[3]}")
    nd = (sol[3]+1)/2
    #print(25*((sol[2]*nd)+(nd-1)-((1/3)*(nd-1)*2)))
    plt.figure(1)
    plt.plot(bestfits_g)
    plt.show()


main()