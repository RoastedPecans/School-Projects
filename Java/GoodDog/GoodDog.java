/*
Program Name: GoodDog.java
Program Purpose: Demonstrates Data Encapsulation and working with classes and objects.
Date Written: 9/22/15
Programmer: Connor Thompson
*/
package gooddog;

public class GoodDog {
    //Instance Variables - always declared as private
    private int weight;
    
    
    //Getter - setters and getters are always public
    public int getWeight() {
        return weight;
    }
    
    //Setter
    public void setWeight(int w) {
        weight = w;
    }
    
    //bark() method
    void bark() {
        if (weight >= 60) {
            System.out.println("Woof! Woof!");
        }
        else if (weight > 14 && weight < 59) {
            System.out.println("Ruff! Ruff!");
        }
    
        else {
            System.out.println("Yip! Yip!");
        }
}
    public static void main(String[] args) {
        GoodDog one = new GoodDog();
        one.setWeight(75);
        
        GoodDog two = new GoodDog();
        two.setWeight(45);
        
        //Have the system give us the dogs weight
        System.out.println("Dog One: " + one.getWeight());
        System.out.println("Dog Two: " + two.getWeight());
        
        one.bark();
        two.bark();
    }
    
}
