from bayesian_node import BayesianNode
import utils

class BayesianNetwork(object):

    def __init__(self, nodes, edges, probabilities):

        self.__nodes = nodes
        self.__edges = edges
        self.__parents = self.__get_parents()
        self.__children = self.__get_children()
        self.__middle_children = list(set(self.__parents) & set(self.__children))

        for node in self.__middle_children:
            self.__parents.remove(node)
            self.__children.remove(node)

        self.__probabilities = self.__process_probabilities(probabilities)
        self.__bayesian_nodes = self.__create_bayesian_nodes()

    def __get_parents(self):
        parents = []
        for node in self.__nodes:
            for edge in self.__edges:
                if (node == edge[0]):
                    parents.append(node)
                    break
        return parents

    def __get_children(self):
        children = []
        for node in self.__nodes:
            for edge in self.__edges:
                if (node == edge[1]):
                    children.append(node)
                    break
        return children

    def __process_probabilities(self, probabilities):

        probabilities_struct = []

        with open(probabilities, "r") as file:
            probabilities = file.readlines()

        for line in probabilities:
            probability_dict = utils.get_probability_dict(line)
            probabilities_struct.append(probability_dict)

        return probabilities_struct

    def __create_bayesian_nodes(self):
        bayesian_nodes = []
        for node in self.__nodes:
            if (node in self.__parents):
                probability_values = [[0, 0]]
                new_node = utils.get_parent_node(
                    node=node,
                    probabilities=self.__probabilities,
                    probability_values=probability_values,
                    children=self.__get_personal_children(node),
                )
                bayesian_nodes.append(new_node)
            # elif (node in self.__children):
            #     parents = self.__get_personal_parents(node)
            #     probability_values = [[0, 0] for _ in range(2 ** len(parents))]
            #     new_node = utils.get_child_node(
            #         node=node,
            #         probabilities=self.__probabilities,
            #         probability_values=probability_values,
            #         parents=parents,
            #     )
            #     bayesian_nodes.append(new_node)
        return bayesian_nodes

    def __get_personal_parents(self, node):
        personal_parents = []
        for edge in self.__edges:
            if (node == edge[1]):
                personal_parents.append(edge[0])
        return personal_parents

    def __get_personal_children(self, node):
        personal_children = []
        for edge in self.__edges:
            if (node == edge[0]):
                personal_children.append(edge[1])
        return personal_children

    def info(self):
        for edge in self.__edges:
            print(f"{edge[0]} -> {edge[1]}")
        for node in self.__bayesian_nodes:
            print(node)
