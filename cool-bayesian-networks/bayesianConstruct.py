from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD 
from pgmpy.inference import VariableElimination

class Bayesian:
    def __init__(self):
        self.model = None
        self.infer = None

    # Creación del modelo bayesiano
    def BayesionNetworkConstruct(self,construct):
        self.model = BayesianNetwork(construct)

    # Definición de las probabilidades condicionales
    def AsignValues(self,name,amount,probabilities,evidences = None ,evidences_card = None):
        return TabularCPD(variable=name, variable_card=amount, 
                   values=probabilities,
                   evidence=evidences, evidence_card=evidences_card)
                   
    # Mostrar los factores de la misma
    def showValues(self,cpd):
        print(cpd.values)


    # Adición de las CPDs al modelo
    def AsignToModel(self,values):
        for value in values:
            self.model.add_cpds(value)
    
    # Verificación del modelo
    def checkModel(self):
        check = self.model.check_model()
        if check:
            print("Esta esta completamente descrita")
        else:
            print("Esta no esta completamente descrita")
    
    # Verificación de los nodos
    def checkNodes(self):
        print("Nodes\n",self.model.nodes())

    # Verificación de los edges
    def checkEdges(self):
        print("Edges\n",self.model.edges())

    # mostrar la construccion que tiene
    def showModelConstruct(self,value):
        print("Model\n",self.model.get_cpds(value))        

    # Calcular probabilidad dado elemento
    def calculateProbability(self,variables,evidenced=None):
        self.infer = VariableElimination(self.model)
        query = self.infer.query(variables=variables, evidence=evidenced)
        return query
