import numpy as np

class Instance:
    def __init__(self, n, k, seed):
        self.n = n
        self.k = k
        np.random.seed = seed
        self.weights = np.random.randint(1, 100, size=(n, n, k))

        # 'Remove' loops:
        for i in range(n):
            self.weights[i, i, :] = 100000
        self.weights[0, n-1] = 100000
        self.weights[n-1, 0] = 100000

n_nodes = 10
n_scenario = 2
instance = Instance(n_nodes, n_scenario, 1234)