from bayesian_node import BayesianNode

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
            line = [self.__replace_all(probability, [" ", "P", "(", ")", "\n"], "") for probability in line]
            line = "".join([char for char in line if (char != "")])
            line = line.split("=")
            line = [*line[0].split("|"), line[1]]
            probability_dict = { "probability_of": line[0], "given": line[1], "equals": line[2] } if (len(line) == 3) else { "probability_of": line[0], "given": "", "equals": line[1] }
            probabilities_struct.append(probability_dict)
        return probabilities_struct

    def __replace_all(self, text, chars, replacement):
        for char in chars:
            text = text.replace(char, replacement)
        return text

    def __create_bayesian_nodes(self):
        bayesian_nodes = []
        for node in self.__nodes:
            if (node in self.__parents):
                probability_values = [[0, 0]]
                for probability in self.__probabilities:
                    if (probability["probability_of"] == node):
                        probability_value = float(probability["equals"])
                        probability_values[0][1] = round(probability_value, 3)
                        probability_values[0][0] = round(1 - probability_value, 3)
                    elif (probability["probability_of"] == f"!{node}"):
                        probability_value = float(probability["equals"])
                        probability_values[0][0] = round(probability_value, 3)
                        probability_values[0][1] = round(1 - probability_value, 3)
                new_node = BayesianNode(
                    label=node,
                    probability_values=probability_values,
                    parents=[],
                    children=self.__get_personal_children(node),
                )
                bayesian_nodes.append(new_node)
            elif (node in self.__children):
                parents = self.__get_personal_parents(node)
                parents_length = len(parents)
                probability_values = [[0, 0] for _ in range(2 ** parents_length)]
                for probability in self.__probabilities:
                    for index, parent in enumerate(parents):
                        if (probability["probability_of"] == node and probability["given"] == parent):
                            probability_value = float(probability["equals"])
                            probability_values[index - 1][1] = round(probability_value, 3)
                            probability_values[index - 1][0] = round(1 - probability_value, 3)
                        elif (probability["probability_of"] == f"!{node}" and probability["given"] == parent):
                            probability_value = float(probability["equals"])
                            probability_values[index - 1][0] = round(probability_value, 3)
                            probability_values[index - 1][1] = round(1 - probability_value, 3)
                        elif (probability["probability_of"] == node and probability["given"] == f"!{parent}"):
                            probability_value = float(probability["equals"]) # 0.05 = [0][1]
                            probability_values[index][1] = round(probability_value, 3)
                            probability_values[index][0] = round(1 - probability_value, 3)
                        elif (probability["probability_of"] == f"!{node}" and probability["given"] == f"!{parent}"):
                            probability_value = float(probability["equals"])
                            probability_values[index][0] = round(probability_value, 3)
                            probability_values[index][1] = round(1 - probability_value, 3)
                new_node = BayesianNode(
                    label=node,
                    probability_values=probability_values,
                    parents=parents,
                    children=[],
                )
                bayesian_nodes.append(new_node)
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
        print("Nodes: ", self.__nodes)
        print("Edges: ", self.__edges)
        print("Parents: ", self.__parents)
        print("Children: ", self.__children)
        print("Middle Child: ", self.__middle_children)
