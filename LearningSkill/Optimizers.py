import numpy as np

class SGD:
    def __init__(self, lr = 0.01):
        self.lr = lr

    def update(self, params, grads):
        for key in params.key():
            params[key] -= self.lr * grads[key]


class Momentum:
    def __init__(self, lr = 0.01, momentum = 0.9):
        '''
        :param lr: learning rate
        :param momentum: 书中式6.3的α
        '''
        self.lr = lr
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v is None:
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.key():
            self.v[key] += self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]

