from probability4e import *

T, F = True, False

class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    def __init__(self):
        self.nodes = ["Asia", "Smoking", "TB", "Lung cancer", "TB or Cancer", "X-ray result", "Dyspnea"]


    def diagnose (self, asia, smoking, xray, dyspnea):
        # To be implemented by the student

        # return either CASE SENSITIVE TB, Cancer, Bronchitis
        # return prob 0-1
        diseaseResult = "test"
        diseaseProbability = 0.5
        return [f"{diseaseResult}", diseaseProbability] # placeholder return value, to be replaced by the student
