import java.util.Scanner;

public class task3atm {

    private static double balance = 1000.00;  
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int choice;
        do {
            System.out.println("\n===== ATM Interface =====");
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit Money");
            System.out.println("3. Withdraw Money");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    checkBalance();
                    break;
                case 2:
                    depositMoney(scanner);
                    break;
                case 3:
                    withdrawMoney(scanner);
                    break;
                case 4:
                    System.out.println("Thank you for using the ATM. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please select again.");
            }
        } while (choice != 4);
        
        scanner.close();
    }
    public static void checkBalance() {
        System.out.println("Your current balance is: $" + balance);
    }
    public static void depositMoney(Scanner scanner) {
        System.out.print("Enter the amount to deposit: $");
        double depositAmount = scanner.nextDouble();
        
        if (depositAmount > 0) {
            balance += depositAmount;
            System.out.println("You've successfully deposited $" + depositAmount);
            System.out.println("Your new balance is: $" + balance);
        } else {
            System.out.println("Invalid deposit amount.");
        }
    }
    public static void withdrawMoney(Scanner scanner) {
        System.out.print("Enter the amount to withdraw: $");
        double withdrawAmount = scanner.nextDouble();
        
        if (withdrawAmount > 0 && withdrawAmount <= balance) {
            balance -= withdrawAmount;
            System.out.println("You've successfully withdrawn $" + withdrawAmount);
            System.out.println("Your new balance is: $" + balance);
        } else if (withdrawAmount > balance) {
            System.out.println("Insufficient balance.");
        } else {
            System.out.println("Invalid withdrawal amount.");
        }
    }
}


