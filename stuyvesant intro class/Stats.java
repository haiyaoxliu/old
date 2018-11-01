//Haiyao Liu
//APCS1 pd3
//HW20 -- GCD Three Ways
//2016-10-18

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
    
    public static int gcd(int a, int b) {
        int div = 1;
        int count = 0;
        while (count <= Math.min(a,b)) {
            if (a % count == 0 && b % count == 0) {
                div = count;
            }
            count += 1;
        }
        return div;
    }
    
    /*
        Euclidean GCD Recursion:
        
    */
    public static int gcdER( int a, int b ) {
        //if ( a < 0 || b < 0 ) { return 0; }
        int t = Math.max(a,b);
        b = Math.min(a,b);
        a = t;
        if (b == 0) {
            return a;
        }
        else {
            return gcdER(b, a % b);
        }
    }
    
    public static void main(String args[]) {
        //tests
        System.out.println(gcdER(5,3));
        System.out.println(gcdER(1071, 462));
        System.out.println(gcdER(464926,44));
    }
}