from probability4e import *

T, F = True, False

class Diagnostics:
    """ Use a Bayesian network to diagnose between three lung diseases """

    def __init__(self):
        self.network = BayesNet([
            # (names, parents, prob)
            ('Asia', '', 0.01),
            ('Smoking', '', 0.5),
            ('TB', 'Asia', {T: 0.05, F: 0.01}),
            ('LungCancer', 'Smoking', {T: 0.6, F: 0.3}),
            ('Bronchitis', 'Smoking', {T: 0.6, F: 0.3}),
            ('TBorCancer', ['TB', 'LungCancer'], 
            {(T, T): 1.0, (T, F): 1.0, (F, T): 1.0, (F, F): 0.0}),
            ('XRay Result', 'TBorCancer', {T: 0.99, F: 0.05}),
            ('Dyspnea', ['TBorCancer', 'Bronchitis'], 
            {(T, T): 0.9, (T, F): 0.7, (F, T): 0.8, (F, F): 0.1})
        ])

    def diagnose (self, visit_to_asia, smoking, xray_result, dyspnea):
        # To be implemented by the student
        # return either CASE SENSITIVE TB, Cancer, Bronchitis
        # return prob 0-1
        diseaseResult = "test"
        diseaseProbability = 0.5
        return [f"{diseaseResult}", diseaseProbability] # placeholder return value, to be replaced by the student
