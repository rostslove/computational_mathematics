class Newton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.h = x[1] - x[0]

    def finite_difference(self, index, degree):
        if degree == 0:
            return self.y[index]
        else:
            return self.finite_difference(index + 1, degree - 1) - self.finite_difference(index, degree - 1)

    def forward_compute(self, arg, index):
        t = (arg - self.x[index]) / self.h
        res = self.finite_difference(index, 0)
        coef = t
        for i in range(index + 1, self.n):
            yi = self.finite_difference(index, i - index)
            res += yi * coef
            coef *= (t - (i - index)) / (i + 1 - index)
        return res

    def backward_compute(self, arg, index):
        t = (arg - self.x[index]) / self.h
        res = self.finite_difference(index, 0)
        coef = t
        for i in range(index - 1, 0, -1):
            yi = self.finite_difference(i, index - i)
            res += yi * coef
            coef *= (t + (index - i)) / (index - i + 1)
        return res

    def get_newton_poly(self, arg):
        res = 0
        if arg < self.x[0]:
            res = self.forward_compute(arg, 0)
        elif arg > self.x[self.n - 1]:
            res = self.backward_compute(arg, self.n - 1)
        for i in range(self.n - 1):
            if arg > self.x[i] and self.x[i + 1] > arg:
                if arg > (self.x[self.n - 1] + self.x[0]) / 2:
                    res = self.forward_compute(arg, i + 1)
                else:
                    res = self.backward_compute(arg, i)
        return res