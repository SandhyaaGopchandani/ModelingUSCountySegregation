# Project: Modeling Economical Segregation in US County Network Structure
______________________________________________________________________________________________________

Social Segregation model by Thomas C. Schelling is a simple mathematical model to understand how local rules can produce macro-behaviors. In this report, we have used the idea of Schelling model in network structure of US counties to understand the economical segregation on a micro as well as a macro level.

This project, though inspired by the Schelling model, has a fundamentally diﬀerent and more robust structure to study the economical segregation in communities. Our model is a network of counties as opposed to square grid of households. The rules of relocation are based on ﬁnancial status rather than race which we think play an even more signiﬁcant role in decision making. The model we developed also considers the interaction between three groups rather than two in order to simulate a more realistic system. Our main goal in this project is to study the dynamics of residential interactions in 3140 counties of United States. The idea behind this project is to simulate the segregation dynamics of counties in United States, based on the level of income of households. We decided to use the basic principles of Schelling model and develop a model simulating how diﬀerent classes of a society based on their income level would make various choices in terms of the neighborhood they want to live in, how they decide to move and what choices of destination they have. Finally we want to show the interactions involved in this dynamic until each individual gets to the point that they are satisﬁed with their relocation.

Doing this project there are some questions we would like to ﬁnd answers to:

1. Is the system going to show segregation patterns after T interactions governed by deﬁned rules?

2. If there is any segregation, how would the system look like at both Micro-level (counties) and Macro level (whole network)?

3. How is the population density in the network going to change as a function of time?


We have a real network data set of USA counties where each node is a county and an edge deﬁnes a border between two given counties. We also have a separate data points of each county like education index, level of income, unemployment rate, life expectancy, and also index of obesity but we are not using that information for this project for simplicity sake.

## Model Setup
Our model is stochastic model that follows the dynamics of Voter Model in the network structure. The way we have setup this project is as follows: We deﬁned population of each county (Node) where each household in the population belongs to one of the three groups: The Poor (1), The Middle class (2) and The Rich (3). The numbers 1, 2 and 3 also represents the rank of the household. Each node has speciﬁc properties deﬁning the state of county (node) at each time step t. These properties include an array of population comprising of P elements that we here know as households in each county. This array with the length of P at the beginning includes households of class 1, 2 or 3 randomly distributed. The second property for each node is the average rank for the node. This rank is determined by the average of the all P ranks of households in each node.

For each household, the distance from the average rank of the county it is in, shows the level of unhappiness/dissatisfaction. The higher this number is, the unhappier and more dissatisﬁed the household is and more likely to move to a new county that has a rank closer to its own rank. The rank of household also deﬁnes the number of resources available to them. For instance, a household with income rank of 1 does not have as much resources for relocating as someone from the level 3. To reﬂect this condition in the model, we decided to use how many edges away can a household move to, based on its rank. A household of class one can only move to the counties that have closer average rank but are only ﬁve edges away. This number for classes 2 and 3 is ten and twenty ﬁve edges away respectively. This is where the number of neighbor property of each node comes to a great use. By this deﬁnition it is expected that for each household there is a diﬀerent radius through which they they can relocate. This range is the largest for the Rich.

### Model Vocabulary

![Model Vocabulary](https://github.com/SandhyaaGopchandani/ModelingUSCountySegregation/blob/master/model_vocab.png)

### Algorithm

![Model Algorithm](https://github.com/SandhyaaGopchandani/ModelingUSCountySegregation/blob/master/model_algorithm.png)


## Results

In this section we will show the results that we got from running the model for 3000 time steps. The ﬁgures are setup in a way that the top three plots within an image display the initial state of the system and bottom three pictures display the state of system after 3000 time-steps and with population count of 50 households in each county. The Only diﬀerence in these three ﬁgures is the initial population distribution of the nodes which seems to play an important role in reaching macro and micro level segregation.

Plots a,b,c in the ﬁgures 4,5,6 are the measure of segregation, Dominance and dissatisfaction respectively at the initial state of the system, Plots d,e and f in these ﬁgures are the same measures after running the model for 3000 time-steps.

- Measure of Segregation

standard deviation is one of the values that we have used to measure the segregation in micro level (county) and macro level (overall network). s standard deviation closer to 0 means that all of the households in the node have the same rank in it implying the county is segregated at micro level and the standard deviation closer to 1 means a county has households of all ranks uniformly distributed, implying that there is no segregation. The plots (a&d) show the measure of segregation. The darker the color is, the segregated the counties are.

- Measure of Dominance

Measure of segregation although capable of demonstrating whether all households in the county have the same rank or not, it does not give any information about what rank is dominant in the county. So, we deﬁned measure of dominance as an indicator of the average rank of a county. The idea is if there are more households with rank 3 then average rank of the county should be closer to 3 and the same for 1 and 2. The plots (b&e) show the measures of dominance.

- Measure of Dissatisfaction

To measure how the dissatisfaction level of households with diﬀerent ranks changes as the model runs we introduced this parameter. Dissatisfaction for a household deﬁnes as the diﬀerence between a household’s rank and the average rank of the county it is in. The bigger the diﬀerence, the more dissatisﬁed a household is. The maximum value of dissatisfaction is 2 while the minimum value is 0. In a complete equilibrium and fair system, the dissatisfaction measure for households of all ranks should be closer to 0 after MAX TIME T but in reality, households with higher rank have higher resources so they should be less dissatisﬁed with other two on average. The plots (c&f) show the dissatisfaction distribution for three diﬀerent ranks.

![Model Algorithm](https://github.com/SandhyaaGopchandani/ModelingUSCountySegregation/blob/master/model_result.png)

shows the results of the model when households with diﬀerent levels of income were uniformly distributed in counties.

Figure above shows the results of the model when households with diﬀerent levels of income are non-uniformly distributed in counties. Population of diﬀerent classes is distributed in a way that there are 50% of household with rank 3, 30% of households with rank 2 and 20% of household with rank 1. Initially, the model exhibits a behavior as it should: there is no apparent segregation (a), the overall average rank of model seems to lean towards lighter colors implying the overall network rank is higher (b) and households with rank 1 are most dissatisﬁed (c) that’s because most counties have higher rank than that closer to rank 1.

The plots (d,e,f) show the changes in the network after 3000 time-steps. We can see the signs of segregation at the county level (d): counties with standard deviation closer to 0 and ones in darker in color. The overall rank of counties in network seem to go up to being closer to 3 (e). It is interesting to note that the counties with lower average rank are surrounded by the counties with higher average rank. We wonder if it is because there is higher number of high ranked households in the model or it is showing the underlying mechanism. Moreover, we can also see that dissatisfaction level for all ranks has seen a decrease implying that relocation based on ﬁnancial status might be a good indicator.

![Model Algorithm](https://github.com/SandhyaaGopchandani/ModelingUSCountySegregation/blob/master/population_density.png)

Figure above shows the population density in the network after 3000 time-steps. We can see how population density is changed in the network after relocation of household. A similar distribution takes place regardless of population distribution at the start. We can see that about 1000 counties have population count as 50 implying that 3000 time-steps might not be enough iterations. We think that running the simulation for longer time-steps would result in interesting results.


