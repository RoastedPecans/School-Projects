/* Program Name: SemiPrime Calculator
Program Purpose: Figure out what prime numbers can create entered number.
Date Written: 11/2/15
Programmer: Connor Thompson
*/
package semiprimecalcv1;
import java.util.Scanner;
import java.util.ArrayList;

public class SemiPrimeCalcV1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number that you want to calculate: ");
        int semiPrimeNumber = scanner.nextInt();
        
        ArrayList<Integer> numbers = new ArrayList<>();  // Use array list for infinite length
        
        //Create list of odd numbers
        for (int i = 3; i < semiPrimeNumber; i = i + 2) { //create for loop that skips even numbers
            numbers.add(i);
        }
        System.out.println("Odd Number List Created");
        //Calculate prime numbers and remove non-primes from ArrayList numbers
        for (int n = 0; n < numbers.size(); n++) { //Use n to iterate through vaules in n
            int arrayDigit = numbers.get(n); //set arrayDigit to number located at index n
            for (int j = 2; j < numbers.size(); j++) { //start j at 2 because anything divided by 2 will be true
                int arrayContains = arrayDigit * j; //multiply n by 2,3,4... 
                if (numbers.contains(arrayContains)) { //If the array contains arrayContains
                    int arrayLocation = numbers.indexOf(arrayContains); //Get index of number matching arrayContains
                    numbers.remove(arrayLocation); //remove it
                }
            }
        }
        int x = 1;
        numbers.add(0, x);
        x = 2;
        numbers.add(1, x);
        System.out.println("Primes up to entered number: " + numbers);
        
        ArrayList<Integer> numbers2 = new ArrayList<>();
        numbers2 = numbers;
        
        for (int i =0; i< numbers.size(); i++) {
            int firstPrime = numbers.get(i);
            for (int j = 0; j < numbers2.size(); j++) {
                int secondPrime = numbers.get(j);
                if (firstPrime * secondPrime == semiPrimeNumber) {
                    System.out.println("Solution Found! Answer is: " + firstPrime + ", " + secondPrime);
                    break;
                }
            }
        }
      
    }
}
