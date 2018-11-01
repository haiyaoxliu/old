//Haiyao Liu
//APCS1 pd3
//HW14 -- stAtistically sPeaking
//

public class Stats {
    
    //methods written under the assumption that the correct datatypes will be used to achieve
    //results with higher precision (double rather than int), and that int mean, for example,
    //will only be as precise as the numerical input types and the / operator allows it to be
    
    public static int mean(int a, int b) {
        return (a + b) / 2;
    }
    
    public static double mean(double a, double b) {
        return (a + b) / 2;
    }
    
    public static int max(int a, int b) {
        if (a > b) {
            return a;
        } else { //return b;
            return b;
        }
    }
    
    public static double max(double a, double b) {
        if (a > b) {
            return a;
        } else { //return b;
            return b;
        }
    }
    
    public static int geoMean(int a, int b) {
        return (int) Math.sqrt(a*b);
    }
    
    public static double geoMean(double a, double b) {
        return Math.sqrt(a*b);
    }
    
    public static void main(String args[]) {
        //none
    }
}