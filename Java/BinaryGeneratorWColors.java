/*
Program Name: RandomRGB
Program Purpose: Create a random set of binary numbers and export as image
Program Purpose ext: Teaches basic I/O, image creation with code, and writing data as files.
Date Written: 8/27/15
Programmer: Connor Thompson
*/

package binarygeneratorwcolors;
//Import needed libraries
import java.awt.image.BufferedImage;
import java.awt.Color;
import java.io.*;
import javax.imageio.ImageIO;
import java.awt.Graphics;
import java.util.Scanner;

public class BinaryGeneratorWColors {

    public static void main(String[] args) {
        
        //Get User Input
        Scanner userInput = new Scanner(System.in);
        System.out.println("What do you want the width of your image to be? (Multiples of 8 work better). ");
        int picWidth = userInput.nextInt();
        System.out.println("What do you want the height of your image to be? (Multiples of 16 work better).");
        int picHeight = userInput.nextInt();
        System.out.println("What do you want the file name to be? (File will be saved in project folder).");
        String fileName = userInput.next();
        
        fileName = fileName + ".png";
        
        //Create variables
        int randomBinary; //Randomly get 1 or 0
        String randomBin; //Use to "paint" onto image
        int red;
        int green;
        int blue;
        
        //Create image + graphics and set font
        BufferedImage img = new BufferedImage(picWidth, picHeight, BufferedImage.TYPE_4BYTE_ABGR); //Create a new blank image with size 512,512
        Graphics g = img.getGraphics();
        g.setPaintMode();
        g.setFont(g.getFont().deriveFont(12f));
        
        int i = 8; //width variable for loop
        int j = 16; //height variable for loop
        
        //Set background to black
        Color black = new Color(0,0,0);
        g.setColor(black);
        g.fillRect(0, 0, picWidth, picHeight);
        
        //create and set color for the 1's and 0's
        //Color myColor = new Color(64,255,0);
        //g.setColor(myColor);
        
        //Loop to iterate through pixels and place binary at each one
        while (i <= picWidth) {
            
            //Get either 0 or 1 randomly
            randomBinary = (int) (Math.random() * 3);
            if (randomBinary == 0) {
                randomBin = "0";
            }
            else if (randomBinary == 2) {
                randomBin = " ";
            }
            else {
                randomBin = "1";
            }
            
            //Set random colors
            green = (int) (Math.random() * 255) + 1;
            red = (int) (Math.random() * 255) + 1;
            blue = (int) (Math.random() * 255) + 1;
            Color myColor = new Color(red, green, blue);
            g.setColor(myColor);
            
            //Draw the string randomBin on the image
            g.drawString(randomBin, i, j);
            i = i + 8; //add eight to i to move "pixel coordinate" to the right eight
            
            if (i == picWidth || i >= picWidth) { //If i is at the last pixel on the image (far right)...
                i = 8; //reset i to starting value (far left)
                j = j + 16; //add one to the height
                if (j >= picHeight) { //if j is at the max height
                    i = picWidth + 1; //make i bigger than width to break loop
                    j = picHeight + 1; //not really neccessary but why not
            }
        }
        }
       
        //save the resulting image as a png
        try {
        File outputfile = new File(fileName);
        ImageIO.write(img, "png", outputfile);
        }
        catch (IOException ex) {
            System.out.println("Error writing file");
        }
        
        System.out.println("Check your project directory!");
    }
}
