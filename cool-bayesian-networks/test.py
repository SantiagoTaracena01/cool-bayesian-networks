from bayesian_network import BayesianNetwork

INPUT_PATH = "./input/red_1.txt"

network = BayesianNetwork(
    nodes=["B", "E", "A", "J", "M"],
    edges=[("B", "A"), ("E", "A"), ("A", "J"), ("A", "M")],
    probabilities=INPUT_PATH
)

# network.info()
