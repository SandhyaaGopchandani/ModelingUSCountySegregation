# Python code to implement segregation model
# modeling complex systems
# Final Project
# Author: Sandhya and Atena
# Last Edit: 12/11/2018

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx
import random
import matplotlib.colors as mcolors
from matplotlib import pyplot
import math
from collections import Counter


def neighborhood(G, node, r):
    """
    :param G: Graph object
    :param node: node of which we want neighbors for
    :param r: radius of the neighborhood
    :return: list of neighbors
    """
    path_lengths = nx.single_source_dijkstra_path_length(G, node)
    return [node for node, length in path_lengths.items()
            if (0 < length <= r)]


def random_pop(N):
    """returns a grid of NxN random values"""
    return np.random.choice([1, 2, 3], N, p=[0.5, 0.3, 0.2])


def node_attributes(G, N):
    """
    :param G: Graph objects
    :param N: Total population in county
    :return: updated Graph object with node properties
    """
    nodes = G.nodes()
    d = {}
    for n in nodes:
        pop = random_pop(N)
        if n not in d.items():
            d[n] = {'population': pop, 'avg_rank': np.mean(pop), 'std': np.std(pop, ddof=1), 'pop_count': len(pop)}
        else:
            continue
    nx.set_node_attributes(G, d)
    return G


def get_least_happy_individual(county_population, county_avg_rank):
    """
    :param county_population:
    :param county_avg_rank:
    :return: the list of unhappy individuals in county

    """
    county_population = np.array(county_population)
    diff = abs(county_avg_rank - county_population)
    least_happy_ppl = []

    if len(list(diff)) != 0:
        max_val = max(list(diff))
        # print(max_val)
        for i, val in enumerate(diff):
            if val == max_val:
                least_happy_ppl.append(county_population[i])

    return least_happy_ppl


def get_desired_county(county, person, neighbors):
    """
    :param person: person (rank) we want to move (1,2 or 3)
    :param neighbors: neighbors of person based on rank
    :return: desired county
    """
    # desired county is a county that is in given radius from person and is closest to person's rank

    rank_diff = []
    desired_counties = []
    desired_county = county
    print('current county rank', G.nodes[county]['avg_rank'])
    for neighbor in neighbors:
        print('neighbor ranks', neighbor, G.nodes[neighbor]['avg_rank'])
        rank_diff.append(abs(person - G.nodes[neighbor]['avg_rank']))

    # diff = abs(person - np.array(rank_diff))
    rank_diff = [3 if math.isnan(x) else x for x in rank_diff]

    # print(diff)
    if len(rank_diff) != 0:
        min_dist = min(rank_diff)

        for i, val in enumerate(rank_diff):
            if val == min_dist:
                desired_counties.append(neighbors[i])

        desired_county = random.choice(desired_counties)
        print('desired counties', desired_counties)

    return desired_county


def get_desired_county_updated(county, person, neighbors):
    """
    :param person: person (rank) we want to move (1,2 or 3)
    :param neighbors: neighbors of person based on rank
    :return: desired county
    """
    # desired county is a county that is in given radius from person and is closest to person's rank

    desired_counties = []
    desired_county = county
    # print('current county rank', G.nodes[county]['avg_rank'])
    if person == 1:
        for neighbor in neighbors:
            if G.nodes[neighbor]['avg_rank'] <= G.nodes[county]['avg_rank']:
                desired_counties.append(neighbor)
            if len(desired_counties) != 0:
                desired_county = random.choice(desired_counties)

    if person == 2:
        desired_county = random.choice(neighbors)

    if person == 3:
        for neighbor in neighbors:
            if G.nodes[neighbor]['avg_rank'] >= G.nodes[county]['avg_rank']:
                desired_counties.append(neighbor)

            if len(desired_counties) != 0:
                desired_county = random.choice(desired_counties)

    return desired_county


def dissatisfaction(G):
    """calculate the dissatisfaction of each household in each county in graph G"""
    person2dissatisfaction = {}
    for n in list(G.nodes()):
        population = G.nodes[n]['population']
        for person in population:
            if person not in person2dissatisfaction:
                person2dissatisfaction[person] = [abs(G.nodes[n]['avg_rank'] - person)]
            else:
                person2dissatisfaction[person].append(abs(G.nodes[n]['avg_rank'] - person))
    return person2dissatisfaction


def update(G, MAX_TIME):
    """the main method with update rules"""
    county_list = list(G.nodes())
    for t in range(MAX_TIME):
        county = random.choice(county_list)
        least_happy_ppl = get_least_happy_individual(G.nodes[county]['population'], G.nodes[county]['avg_rank'])
        # print(least_happy_ppl)
        magnitude = 5
        if len(least_happy_ppl) != 0:
            for person in least_happy_ppl:
                # print('chosen person', person)
                if person == 3:
                    neighbors = neighborhood(G, county, (person + 2) * magnitude)
                else:
                    neighbors = neighborhood(G, county, person * magnitude)

                # print('neighbours', county, neighbors)
                desired_county = get_desired_county_updated(county, person, neighbors)
                # print("desired_county", desired_county, G.nodes[desired_county]['avg_rank'])

                desired_county_pop = list(G.node[desired_county]['population'])
                desired_county_pop.append(person)

                G.node[desired_county]['population'] = desired_county_pop
                G.node[desired_county]['avg_rank'] = np.mean(desired_county_pop)
                G.node[desired_county]['std'] = np.std(desired_county_pop, ddof=1)
                G.node[desired_county]['pop_count'] = len(desired_county_pop)

                # print("After: desired_county", desired_county, G.nodes[desired_county]['avg_rank'])
                county_pop = list(G.node[county]['population'])
                county_pop.remove(person)
                # print("length", len(county_pop))

                G.node[county]['population'] = county_pop
                G.node[county]['avg_rank'] = np.mean(county_pop)
                G.node[county]['std'] = np.std(county_pop, ddof=1)
                G.node[county]['pop_count'] = len(county_pop)

    return G


def plot(G):
    """Plotting measurement of segregation and dominance in network structure """
    np.random.seed(0)
    node_std = {}
    node_size = {}
    node_avg = {}
    for n in list(G.nodes()):
        node_std[n] = G.nodes[n]['std']
        node_size[n] = G.nodes[n]['pop_count'] // 2
        node_avg[n] = G.nodes[n]['avg_rank']

    # degrees = G.degree()  # Dict with Node ID, Degree
    fig, ax = plt.subplots()

    nodes = G.nodes()
    n_color_std = np.asarray([node_std[n] for n in nodes])
    n_color_avg = np.asarray([node_avg[n] for n in nodes])
    n_size = np.asarray([node_size[n] for n in nodes])

    # Turn off tick labels
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    plt.title("Standard Deviation as measure of segregation")
    sc = nx.draw_networkx_nodes(G, pos=nx.kamada_kawai_layout(G), nodelist=nodes, node_color=n_color_std,
                                cmap='viridis', with_labels=False, ax=ax, node_size=n_size, alpha=0.8)

    # plt.title("Average rank")
    # sc = nx.draw_networkx_nodes(G, pos=nx.kamada_kawai_layout(G), nodelist=nodes, node_color=n_color_avg, cmap='plasma',with_labels=False, ax=ax, node_size=n_size, alpha=0.8)
    fig.colorbar(sc)
    plt.show()


def segregation_entropy_index(G):
    """Measuring segregation with entropy index
    """
    n_ij = []
    hi = 0
    for county in list(G.nodes()):
        if math.isnan(G.nodes[county]['avg_rank']):
            continue
        else:
            n_ij.append(int(round(G.nodes[county]['avg_rank'])))

    c = Counter(n_ij)

    for i in c:
        pij = i, c[i] / len(n_ij)
        ln_pij = np.log(pij[1])
        print(pij[0])
        print((pij[1] * ln_pij))
        hi = hi + (pij[1] * ln_pij)

    print("entropy", hi * -1)


def calc_pop_density(G):
    """
    :param G: Graph
    :return: historgam of population density
    """
    pop_density = []
    for county in list (G.nodes()):
        pop_density.append(G.nodes[county]['pop_count'])
    #print(pop_density)
    pyplot.title("Population density overtime")
    plt.hist(pop_density, bins=10)
    plt.show()


# extra code start
def update_2(G):
    """a different method with a cellular automata style updates"""
    MAX_DS = 2
    MAX_RANK = 3
    magnitude = 10
    for county in list(G.nodes()):
        for rank in G.nodes[county]['population']:
            ds = abs(G.nodes[county]['avg_rank'] - rank)
            move_prob = (ds/MAX_DS) * (rank/MAX_RANK)
            if random.random() <= move_prob:
                neighbors = neighborhood(G, county, (rank * magnitude))
                move(county, rank, neighbors)


def move(county, rank, neighbors):
    pass

# extra code end


# call main
if __name__ == '__main__':
    POP_COUNT = 50
    G = nx.read_edgelist("CountyNetworkEdgeList.dat", nodetype=str)
    G = node_attributes(G, POP_COUNT)
    # plot(G)

    # In order to update the network, comment these lines in. These are commented out because this part takes
    # longer time to run

    # g_updated = update(G, 3000)
    # plot(g_updated)
    # diss_dict = dissatisfaction(g_updated)

    # line_colors = ['r', 'g', 'b']
    # dis_keys = [3, 1, 2]
    # i = 0
    # for key in dis_keys:
    #     pyplot.hist(diss_dict[key], bins='auto', alpha=0.8, color=line_colors[i], label="Rank:" + str(key))
    #     pyplot.title("Dissatisfaction distribution")
    #     pyplot.legend(loc='upper right')
    #     pyplot.xlabel("dissatisfaction")
    #     pyplot.ylabel("frequency")
    #
    #     i += 1
    # pyplot.show()

    # segregation_entropy_index(g_updated)
    # calc_pop_density (g_updated)


