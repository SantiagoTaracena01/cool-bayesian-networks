from bayesian_network import BayesianNetwork

# NODES = ["B", "E", "A", "J", "M"]
# EDGES = [("B", "A"), ("E", "A"), ("A", "J"), ("A", "M")]

NODES = ["A", "B", "C"]
EDGES = [("A", "C"), ("B", "C")]
INPUT_PATH = "./input/mi_red.txt"

network = BayesianNetwork(
    nodes=NODES,
    edges=EDGES,
    probabilities=INPUT_PATH
)

network.info()
