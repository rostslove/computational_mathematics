public interface F {

    String getString();

    Double solve(double x);

    default Double derivative(double x) {
        return (solve(x+0.00000001)-solve(x))/0.00000001;
    }
}
