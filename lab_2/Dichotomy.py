class Dichotomy:
    def __init__(self, f, a, b, eps):
        self.f = f
        self.a = a
        self.b = b
        self.eps = eps

    def is_ok_status(self):
        if self.eps <= 0:
            return 1
        if self.f(self.a) * self.f(self.b) > 0:
            return 2
        if self.a >= self.b or self.b - self.a >= 10:
            return 3

    def solve(self):
        a = self.a
        b = self.b
        eps = self.eps
        x = (a + b) / 2
        iterations = 0
        while True:
            if abs(a - b) <= eps and abs(self.f(x)) <= eps:
                break
            iterations += 1
            y = self.f(x)
            if y * a > 0:
                a = x
            else:
                b = x
            x = (a + b) / 2
        return x, self.f(x), iterations