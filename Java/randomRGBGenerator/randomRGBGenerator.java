/*
Program Name: RandomRGB
Program Purpose: Create a random color wallpaper where each pixel is random
Date Written: 8/26/15
Programmer: Connor Thompson
*/

package randomrgb;
//Import needed libraries
import java.awt.image.BufferedImage;
import java.awt.Color;
import java.io.*;
import javax.imageio.ImageIO;

public class RandomRGB {

    public static void main(String[] args) {
        
        //Create and print random variables
        float alpha = (float) Math.random();
        int red = (int) (Math.random() * 255) + 1;
        int green = (int) (Math.random() * 255) + 1; 
        int blue = (int) (Math.random() * 255) + 1; 
        //alpha = (float) Math.round(alpha * 100)/100; Allows you to use Alpha if desired
        System.out.println(red + " " + green + " " + blue); //print the random rgb value
        
        BufferedImage img = new BufferedImage(1280, 1024, BufferedImage.TYPE_4BYTE_ABGR); //Create a new blank image with size 512,512

        int width = img.getWidth(); //width of new img
        int height = img.getHeight(); //height of img
        int i = 0; //width variable for loop
        int j = 0; //height variable for loop
        
        //Loop to iterate through pixels and place random rgb color at each one
        while (i <= width) {
            //set random color values again
            red = (int) (Math.random() * 255) + 1;
            green = (int) (Math.random() * 255) + 1; 
            blue = (int) (Math.random() * 255) + 1; 
            
            //create new color. This color will be placed on the current pixel
            Color myColor = new Color(red, green, blue);
            int rgb = myColor.getRGB();
            img.setRGB(i,j,rgb); //make pixel at coordinate i,j color rgb
            
            i = i + 1; //add one to i to move "pixel coordinate" to the right one
            
            if (i == width) { //If i is at the last pixel on the image (far right)...
                i = 0; //reset i to starting value (far left)
                j = j + 1; //add one to the height
                if (j == height) { //if j is at the max height
                    i = width + 1; //make i bigger than width to break loop
                    j = height + 1; //not really neccessary but why not
            }
        }
        }
        
        //save the resulting image as a png
        try {
        File outputfile = new File("RandomRGB.png");
        ImageIO.write(img, "png", outputfile);
        }
        catch (IOException ex) {
            System.out.println("Error writing file");
        }
        
        System.out.println("Check your project directory!")
        
    }
}
