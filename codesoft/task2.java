import java.util.Scanner;

public class task2student {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of subjects: ");
        int numberOfSubjects = scanner.nextInt();
        double totalMarks = 0;
        for (int i = 1; i <= numberOfSubjects; i++) {
            System.out.print("Enter the marks for subject " + i + ": ");
            double marks = scanner.nextDouble();
            totalMarks += marks;
        }
        double average = totalMarks / numberOfSubjects;
        char grade;
        if (average >= 90) {
            grade = 'A';
        } else if (average >= 80) {
            grade = 'B';
        } else if (average >= 70) {
            grade = 'C';
        } else if (average >= 60) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        System.out.println("total Marks:"+totalMarks);
        System.out.println("Average Marks: " + average);
        System.out.println("Grade: " + grade);
        scanner.close();
    }
}
 
