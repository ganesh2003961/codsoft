import java.util.Random;
import java.util.Scanner;
public class task3 {
    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);
        int min = 1;
        int max = 100;
        int randomNumber = random.nextInt((max - min) + 1) + min;
        int maxAttempts = 5;
        
        int userGuess = 0; 
        int attempts = 0;   
        
        System.out.println("Guess a number between " + min + " and " + max + ":");
        System.out.println("You have " + maxAttempts + " attempts to guess the number.");
        while (attempts < maxAttempts) {
            userGuess = scanner.nextInt();
            attempts++;  
            if (userGuess < randomNumber) {
                System.out.println("Too low! Try again:");
            } else if (userGuess > randomNumber) {
                System.out.println("Too high! Try again:");
            } else {
                System.out.println("Congratulations! You guessed the correct number: " + randomNumber);
                break;
            }
            if (attempts == maxAttempts) {
                System.out.println("Sorry! You've run out of attempts. The correct number was: " + randomNumber);
            }
        }
        scanner.close();
    }
}
