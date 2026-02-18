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
            ('Cancer', 'Smoking', {T: 0.1, F: 0.01}),
            ('Bronchitis', 'Smoking', {T: 0.6, F: 0.3}),
            ('TBorCancer', ['TB', 'Cancer'], 
            {(T, T): 1.0, (T, F): 1.0, (F, T): 1.0, (F, F): 0.0}),
            ('XRayResult', 'TBorCancer', {T: 0.99, F: 0.05}),
            ('Dyspnea', ['TBorCancer', 'Bronchitis'], 
            {(T, T): 0.9, (T, F): 0.7, (F, T): 0.8, (F, F): 0.1})
        ])

    def diagnose (self, visit_to_asia, smoking, xray_result, dyspnea):
        mapping = {
            "Yes": T, "No": F,
            "Abnormal": T, "Normal": F,
            "Present": T, "Absent": F
        }
        
        inputs = {
            'Asia': visit_to_asia,
            'Smoking': smoking,
            'XRayResult': xray_result,
            'Dyspnea': dyspnea
        }

        evidence = {}
        for key, value in inputs.items():
            if value != "NA":
                evidence[key] = mapping[value]

        probTB = enumeration_ask('TB', evidence, self.network)[T]
        probCancer = enumeration_ask('Cancer', evidence, self.network)[T]
        probBronchitis = enumeration_ask('Bronchitis', evidence, self.network)[T]

        results = [
            ("Bronchitis", probBronchitis),
            ("Cancer", probCancer),
            ("TB", probTB)
        ]

        likelyDisease = max(results, key=lambda x: x[1])
        return [likelyDisease[0], likelyDisease[1]]