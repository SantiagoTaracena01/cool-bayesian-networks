# Laboratorio 2
# Inteligencia Artificial

# YongBum Park 20117
# Santiago Taracena 20017
# Pedro Arriola 20188
# Oscar López 20679

from bayesian_construct import *

bayesian = Bayesian()

bayesian.bayesian_network_construction([('A', 'C'), ('B', 'C')])

cpd_a = bayesian.asign_values('A', 2, [[0.3], [0.7]])
cpd_b = bayesian.asign_values('B', 2, [[0.23], [0.77]])
cpd_c = bayesian.asign_values('C', 2, [[0.20, 0.77, 0.10, 0.5], [0.80, 0.23, 0.90, 0.5]], ['A', 'B'], [2, 2])

bayesian.show_values(cpd_c)
bayesian.asign_to_model([cpd_a, cpd_b, cpd_c])
print(bayesian.check_model())
bayesian.check_edges()
bayesian.check_nodes()
bayesian.show_model_construction('C')
result = bayesian.calculate_probability(['C'], { 'A': 0, 'B': 1 })
print(result)
