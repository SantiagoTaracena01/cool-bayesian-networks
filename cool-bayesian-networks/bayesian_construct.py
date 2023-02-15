# Laboratorio 2
# Inteligencia Artificial

# YongBum Park 20117
# Santiago Taracena 20017
# Pedro Arriola 20188
# Oscar López 20679

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD 
from pgmpy.inference import VariableElimination

class Bayesian(object):

    def __init__(self):
        self.model = None
        self.infer = None

    # Creación del modelo bayesiano
    def bayesian_network_construction(self, construct):
        self.model = BayesianNetwork(construct)

    # Definición de las probabilidades condicionales
    def asign_values(self, name, amount, probabilities, evidences=None, evidences_card=None):
        return TabularCPD(
            variable=name,
            variable_card=amount, 
            values=probabilities,
            evidence=evidences,
            evidence_card=evidences_card,
        )

    # Mostrar los factores de la misma
    def show_values(self, cpd):
        print(cpd.values)

    # Adición de las CPDs al modelo
    def asign_to_model(self, values):
        for value in values:
            self.model.add_cpds(value)
        for ucpd in self.model.get_cpds():
            if not self.model.check_model(ucpd):
                print(f"Error al agregar la CPD {ucpd}")

    # Verificación del modelo
    def check_model(self):
        return self.model.check_model()

    # Verificación de los nodos
    def check_nodes(self):
        print("Nodes\n", self.model.nodes())

    # Verificación de los edges
    def check_edges(self):
        print("Edges\n", self.model.edges())

    # mostrar la construccion que tiene
    def show_model_construction(self, value):
        print("Model\n", self.model.get_cpds(value))        

    # Calcular probabilidad dado elemento
    def calculate_probability(self, variables, evidenced=None):
        self.infer = VariableElimination(self.model)
        query = self.infer.query(variables=variables, evidence=evidenced)
        return query
