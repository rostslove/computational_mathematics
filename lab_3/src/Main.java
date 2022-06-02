import java.util.Scanner;

public class Main {

    public static void main(String[] xs) {
        Scanner scanner = new Scanner(System.in);
        Integration integration = new Integration();
        integration.setMethods();
        integration.setFunctions();
        System.out.println("Выберите уравнение:");
        for (int i = 0; i < integration.getfunctions().size(); i++) {
            System.out.println((i+1) + ". " + integration.getfunctions().get(i).getString());
        }
        double a;
        double b;
        double eps;
        while (true) {
            String linuxArtefact = scanner.nextLine();
            while (isInteger(linuxArtefact)){
                System.out.println("Введите корректное значение!");
                linuxArtefact = scanner.nextLine();
            }
            int chosenEquation = Integer.parseInt(linuxArtefact);
            if (1 <= chosenEquation && chosenEquation <= integration.getfunctions().size() ) {
                while (true) {
                    System.out.println("Введите левую границу интервала интегрирования:");
                    linuxArtefact = scanner.nextLine();
                    while (isNumeric(linuxArtefact)){
                        System.out.println("Введите корректное значение!");
                        linuxArtefact = scanner.nextLine();
                    }
                    a = Double.parseDouble(linuxArtefact);
                    System.out.println("Введите правую границу интервала интегрирования:");
                    linuxArtefact = scanner.nextLine();
                    while (isNumeric(linuxArtefact)){
                        System.out.println("Введите корректное значение!");
                        linuxArtefact = scanner.nextLine();
                    }
                    b = Double.parseDouble(linuxArtefact);
                    if (a >= b) {
                        System.out.println("Вырожденный интервал");
                        return;
                    }
                    if (a <= -15 || b >= 15) {
                        System.out.println("Интервал слишком велик");
                        continue;
                    }
                    while (true) {
                        System.out.println("Введите погрешность:");
                        linuxArtefact = scanner.nextLine();
                        while (isNumeric(linuxArtefact)){
                            System.out.println("Введите корректное значение!");
                            linuxArtefact = scanner.nextLine();
                        }
                        eps = Double.parseDouble(linuxArtefact);
                        if (eps <= 0 || eps > 1) {
                            System.out.println("Недопустимая погрешность");
                        } else {
                            break;
                        }
                    }
                    break;
                }
                System.out.println("Выберите метод вычисления интеграла:");
                for (int i = 0; i < integration.getMethods().size(); i++) {
                    System.out.println((i+1) + ". " + integration.getMethods().get(i).getName());
                }
                while (true) {
                    int chosenMethod = Integer.parseInt(scanner.nextLine());
                    if (1 <= chosenMethod && chosenMethod <= integration.getMethods().size()) {
                        try {
                            System.out.println(integration.solve(chosenEquation-1, chosenMethod-1, a, b, eps));
                        }
                        catch (RuntimeException e) {
                            System.out.println(e.getMessage());
                        }
                        break;
                    } else {
                        System.out.println("Выберите метод из предложенных, пожалуйста");
                    }
                }
            } else {
                System.out.println("Такого уравнения нет");
                continue;
            }
            break;
        }
    }

    private static boolean  isNumeric(String strNum) {
        if (strNum == null) {
            return true;
        }
        try {
            double d = Double.parseDouble(strNum);
        } catch (NumberFormatException nfe) {
            return true;
        }
        return false;
    }

    private static boolean isInteger(String strNum){
        if (strNum == null) {
            return true;
        }
        try {
            int d = Integer.parseInt(strNum);
        } catch (NumberFormatException nfe) {
            return true;
        }
        return false;
    }

}
