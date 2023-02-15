# Laboratorio 2
# Inteligencia Artificial
# Authors: YongBum Park 20117, Santiago Taracena 20017, Pedro Arriola 20188, Oscar López 20679

from bayesian_construct import Bayesian

bayesian = Bayesian()

# Network construction
network_structure = [("A", "C"), ("B", "C")]
bayesian.bayesian_network_construction(network_structure)
cpd_a = bayesian.asign_values("A", 2, [[0.3], [0.7]])
cpd_b = bayesian.asign_values("B", 2, [[0.23], [0.77]])
cpd_c = bayesian.asign_values(
    "C", 2, [[0.20, 0.77, 0.10, 0.5], [0.80, 0.23, 0.90, 0.5]], ["A", "B"], [2, 2]
)

def test_bayesian_network_construction():
    assert bayesian.model != None, "The model is not created"

test_bayesian_network_construction()
