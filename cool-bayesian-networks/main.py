from bayesianConstruct import *

bayesian = Bayesian()

bayesian.BayesionNetworkConstruct([('A', 'C'), ('B', 'C')])

cpd_a = bayesian.AsignValues('A',2,[[0.3], [0.7]])
cpd_b = bayesian.AsignValues('B',2,[[0.23], [0.77]])
cpd_c = bayesian.AsignValues('C',2,[[0.20, 0.77, 0.10, 0.5],[0.80, 0.23, 0.90, 0.5]],['A', 'B'],[2, 2])

bayesian.showValues(cpd_c)
bayesian.AsignToModel([cpd_a,cpd_b,cpd_c])
bayesian.checkModel()
bayesian.checkEdges()
bayesian.checkNodes()
bayesian.showModelConstruct('C')
result = bayesian.calculateProbability(['C'],{'A': 0, 'B': 1})
print(result)