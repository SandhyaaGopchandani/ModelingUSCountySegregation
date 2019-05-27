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

