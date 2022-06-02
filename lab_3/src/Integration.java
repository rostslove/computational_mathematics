import java.util.ArrayList;

public class Integration {

    public String answer = "";
    public final ArrayList<F> functions = new ArrayList<>();
    public final ArrayList<Method> methods = new ArrayList<>();

    public ArrayList<LineSegment> splitLineSegment(double a, double b, F f) {
        ArrayList<LineSegment> LineSegment = new ArrayList<>();
        double eps = 0.00000001;
        double new_left = f.solve(a).isNaN() || f.solve(a).isInfinite() ? a+eps : a;
        for (double i = a + 0.00001; i < b; i += 0.00001) {
            if (f.solve(i).isNaN() || f.solve(i).isInfinite()) {
                LineSegment.add(new LineSegment(new_left, i-eps));
                new_left = i + eps;
            }
        }
        double new_end = f.solve(b).isNaN() || f.solve(b).isInfinite() ? b-eps : b;
        LineSegment.add(new LineSegment(new_left, new_end));
        return LineSegment;
    }

    public String solve(int chosenF, int chosenMethod, double a, double b, double eps) {
        int counter = 0;
        int n = 4;
        F f = functions.get(chosenF);
        Method m = methods.get(chosenMethod);
        ArrayList<LineSegment> LineSegment = splitLineSegment(a, b, f);
        double s1 = 0;
        for (LineSegment lineSegment : LineSegment) {
            s1 = m.solve(f, lineSegment.left, lineSegment.right, n);
        }
        double s;
        do {
            s = s1;
            n *= 2;
            if (n > 10000000) {
                throw new RuntimeException("Интеграл не существует");
            }
            for (LineSegment lineSegment : LineSegment) {
                s1 = m.solve(f, lineSegment.left, lineSegment.right, n);
            }
            counter++;
        } while (Math.abs(s1 - s) > eps);
        if (Double.isInfinite(s1) || Double.isNaN(s1) || s1 == -0.0) {
            throw new RuntimeException("Интеграл не существует");
        }
        answer += "Приближенное значение интеграла: " + s1 + "\n" + "Число разбиений интервала интегрирования: " + n;
        return answer;
    }

    public void setFunctions() {
        functions.add(new F() {
            @Override
            public String getString() {
                return "3 * x^3 - 4 * x^2 + 5 * x - 16";
            }

            @Override
            public Double solve(double x) {
                return 3 * Math.pow(x,3) - 4 * Math.pow(x,2) + 5 * x - 16;
            }
        });

        functions.add(new F() {
            @Override
            public String getString() {
                return "e^x * sin(x^3 + 0.67 * x)";
            }

            @Override
            public Double solve(double x) {
                return Math.exp(x) * Math.sin(Math.pow(x, 3) + 0.67 * x);
            }
        });

        functions.add(new F() {
            @Override
            public String getString() {
                return "1/sqrt(1 - x^2)";
            }

            @Override
            public Double solve(double x) {
                return 1/Math.sqrt(1-Math.pow(x, 2));
            }
        });

        functions.add(new F() {
            @Override
            public String getString() {
                return "sin(x)/x";
            }

            @Override
            public Double solve(double x) {
                return Math.sin(x)/x;
            }
        });
    }

    public void setMethods() {
        methods.add(new Method() {
            @Override
            public String getName() {
                return "Метод левых прямоугольников";
            }

            @Override
            public Double solve(F f, double a, double b, int n) {
                double h = (b-a)/n;
                double sum = 0;
                for (double i = a; i < b; i += h) {
                    sum += f.solve(i);
                }
                return sum*h;
            }
        });

        methods.add(new Method() {
            @Override
            public String getName() {
                return "Метод правых прямоугольников";
            }

            @Override
            public Double solve(F f, double a, double b, int n) {
                double h = (b-a)/n;
                double sum = 0;
                for (double i = a + h; i <= b; i += h) {
                    sum += f.solve(i);
                }
                return sum*h;
            }
        });

        methods.add(new Method() {
            @Override
            public String getName() {
                return "Метод средних прямоугольников";
            }

            @Override
            public Double solve(F f, double a, double b, int n) {
                double h = (b-a)/n;
                double sum = 0;
                for (double i = a + 0.5 * h; i < b; i += h) {
                    sum += f.solve(i);
                }
                return h*sum;
            }
        });

        methods.add(new Method() {
            @Override
            public String getName() {
                return "Метод трапеций";
            }

            @Override
            public Double solve(F f, double a, double b, int n) {
                double h = (b-a)/n;
                double sum = (f.solve(a) + f.solve(b)) / 2;
                for (int i = 1; i < n; i++) {
                    sum += f.solve(a + i*h);
                }
                return h*sum;
            }
        });

        methods.add(new Method() {
            @Override
            public String getName() {
                return "Метод Симпсона";
            }

            @Override
            public Double solve(F f, double a, double b, int n) {
                double h = (b-a)/n;
                double sum = f.solve(a) + f.solve(b);
                for (int i = 1; i < n; i++) {
                    if (i % 2 == 0) {
                        sum += 2 * f.solve(a + i*h);
                    } else {
                        sum += 4 * f.solve(a + i*h);
                    }
                }
                return h / 3 * sum;
            }
        });
    }

    public ArrayList<F> getfunctions() {
        return functions;
    }

    public ArrayList<Method> getMethods() {
        return methods;
    }

}
