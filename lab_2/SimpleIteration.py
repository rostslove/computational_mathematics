class SimpleIteration:
    def __init__(self, f, a, b, eps):
        self.f = f
        self.a = a
        self.b = b
        self.eps = eps

    def is_ok_status(self):
        a = self.a
        b = self.b
        f = self.f
        lam = -1 / max(self.derivative(f, a), self.derivative(f, b))
        fi = lambda x: x + lam * f(x)
        q = max(abs(self.derivative(fi, a)), abs(self.derivative(fi, b)))
        if self.eps <= 0:
            return 1
        if f(a) * f(b) > 0:
            return 2
        if a >= b or b - a >= 10:
            return 3
        if q > 1:
            return 4

    def derivative(self, func, x_0):
        return (func(x_0 + 0.000001) - func(x_0)) / 0.000001

    def solve(self):
        a = self.a
        b = self.b
        f = self.f
        lam = -1 / max(self.derivative(f, a), self.derivative(f, b))
        fi = lambda x: x + lam * f(x)
        print((self.derivative(fi, a), self.derivative(fi, b)))
        q = max(abs(self.derivative(fi, a)), abs(self.derivative(fi, b)))
        x = a
        iterations = 0
        if q > 0.5:
            acc = (1 - q) / q * self.eps
        else:
            acc = self.eps
        while True:
            iterations += 1
            x_new = fi(x)
            if abs(x - x_new) <= acc:
                break
            x = x_new
        return x_new, self.f(x_new), iterations

