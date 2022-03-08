# Integration of Renewable Energy Sources in Smart Grids by Means of Evolutionary Optimization Algorithms In Python

# Developing and executing Genetic Algorithm in Python

Description:

Governments encourage consumers to generate power at low scale. This type of generation is called Distributed Generation (DG). One of the most critical factors that overwhelm power system network is Reactive Power Management. Flexible AC Transmission Systems is one of the reactive power energy resources that has been proposed to compensate the reactive power shortage. Many solutions have been proposed consisting of DG placement, increasing voltage stability, improving voltage profile, minimizing cost. For reducing losses in network, Genetic Algorithm method is used. By taking into account DG optimal placement with respect to maintaining maximum penetration level the optimization problem changes to multi-objective optimization problem.

Genetic Algorithm:

Genetic algorithm is a high-level procedure inspired heavily from natural selection. Natural selection is the concept of survival and reproduction of the species. It also acts as a key mechanism of evolution. Genetic Algorithm usually gives high-quality solutions to the optimization problem. It also involves operations like selection, crossover and mutation which are heavily bio-inspired. The genetic information is added to the chromosome of the individual. The three genes correspond to Bus location, Reactive power injected, Loadability factor.

Initial Population:
The initial population is randomly generated. An individual is described by a couple of parameters called as genes. A string called Chromosome is formed by linking of genes. In our case, we have five chromosomes with three genes. The three genes are loadability, Reactive power injected and location of the bus. A random function which is in-built is used to generate random numbers.

Evaluation:
The function is evaluated for all the individuals in the initial population. The individual with bigger function value is considered as the best individual in the population. It shows the estimated survival probability in the next generation. And they are sorted and ranked from higher to lower values.

Selection:
It is a process of genetic algorithm where the individuals are selected for breeding afterwards. The group of parents are obtained after selection process. The first four parents in the sorted list are selected as parents who are going to participate in the crossover process. The last one is reserved for mutation process.

Crossover:
A couple of parents are selected for performing the crossover operation. A random point is also selected to implement the crossover operation. Let us consider an example with four parents with each of them having five genes. The process starts with the first couple. A crossover point is selected between genes 2 and 3. So, new offspring would be created by copying genes 1 and 2 from the first parent and the remaining three genes from the second parent.

Mutation:
The reserved and remaining individuals takes place in the mutation process. Mutation rate has been set to 0.5. A random number ‘r’ from 0 to 1 is generated and compared with the mutation rate. If the random number is lesser than mutation rate, all genes of the participant would get mutated. As a result, a new offspring will be born.

New Population:
After the process of crossover and mutation, a new population is formed. The new population comprises of off springs from crossover and mutation process. It also comprises of individuals selected from elitism operator. Elitism is the process of retaining the best individuals of current generation unaltered in the subsequent generation. For example, if there are five individuals, two offspring are obtained from crossover between two couples (four individuals). One offspring is obtained as a result of mutation. And two individuals with the top function values are obtained from elitist operator to carry it with subsequent generations.

Final Population:
These entire operations are carried on for number of generations. The evolution process is implemented continuously until a stop parameter is satisfied. The most prevalent stop condition is to reach the maximum permissible generations. By this way, an optimal or best individual is obtained by genetic algorithm after the maximum permissible generation. The best individual has desired genes comprising Bus location, Reactive power injected, Loadability factor. 
