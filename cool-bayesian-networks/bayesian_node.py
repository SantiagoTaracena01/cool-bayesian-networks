class BayesianNode(object):
    
    def __init__(self, label, probability_values, parents, children):
        self.__label = label
        self.__probability_values = probability_values
        self.__parents = parents
        self.__children = children
        print(label, probability_values, parents, children)
