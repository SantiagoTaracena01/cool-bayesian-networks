from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Creación del modelo bayesiano
model = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definición de las probabilidades condicionales
cpd_a = TabularCPD(variable='A', variable_card=2, values=[[0.3], [0.7]])
cpd_b = TabularCPD(variable='B', variable_card=2, values=[[0.23], [0.77]])
cpd_c = TabularCPD(variable='C', variable_card=2, 
                   values=[[0.20, 0.77, 0.10, 0.5],[0.80, 0.23, 0.90, 0.5]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Adición de las CPDs al modelo
model.add_cpds(cpd_a, cpd_b, cpd_c)

# Verificación del modelo
print(model.check_model())
# Verificación del modelo
print(model.nodes())
print(model.edges())
print(model.get_cpds('C'))

# Creación del objeto de inferencia
infer = VariableElimination(model)

# Inferencia de una probabilidad
query = infer.query(variables=['C'], evidence={'A': 0, 'B': 1})
print(query)

# Inferencia de varias probabilidades
query = infer.query(variables=['C'], evidence={'A': 1, 'B': 1})
print(query)

# P(A) = 0.30
# P(B) = 0.23
# P(C|A, B) = 0.20
# P(C|!A, B) = 0.10
# P(C|A, !B) = 0.77
# P(C|!A, !B) = 0.5