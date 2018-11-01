//Haiyao Liu
//APCS1 pd3
//HW23 -- Karmacomma
//2016-10-27

//worked with Holden in class

public class Commafy {
    /*------------------------------------------------------------
    RECURSIVE commafy
    
    parameters: int n
    expected return: str (n with commas added every three digits)
    
    let d(n) = number of digits of n
    1 - the base case occurs when n<1000, or d(n) < 4
    2 - concatenate the three terminating digits to the return of
        commafy(the rest of the number);
    
    (d(n) < 4)?
        true {return n}
        false {return commafy(rest of the number)
    ------------------------------------------------------------*/
    public static String commafyR(int n) {
        String ns = Integer.toString(n);
        
        //base case
        if (n < 1000) {
            return ns;
        }
        
        //otherwise, commafy(leading digits except last 3) + "inserted comma" + last 3 digits
        return commafyR(n/1000) + "," + ns.substring(ns.length()-3);
    }
    
    /*------------------------------------------------------------
    ITERATIVE commafy
    
    parameters: int n
    expected return: str (n with commas added every three digits)
    
    convert n tostr to allow for comma addition
    
    commas are added every third digit counting from the right,
    (terminating end) so
    1 - str.length() > 3 to start adding commas
    2 - we iterate from str.length() to index 0, right to left
    3 - the counter is decreased by 3 each time to skip 3 digits
    4 - to add the actual comma, we splice the str using substring
        into d(n)-3 digits and 3 digits and add the comma in btwn
    ------------------------------------------------------------*/
    public static String commafyF(int n) {
        //convert n tostr to allow for comma addition
        String ns = Integer.toString(n);
        
        //if d(n)>3, we add commas every third digit
        for(int i = ns.length(); i > 3; i-=3) {
            
            //first d(n)-3 digits, comma, last 3 digits
            ns = ns.substring(0,i-3) + "," + ns.substring(i-3);
        }
        return ns;
    }
    public static void main(String[] args) {
        //block of test cases:
    /*  System.out.println(commafyR(1));
        System.out.println(commafyR(10));
        System.out.println(commafyR(101));
        System.out.println(commafyR(1000));
        System.out.println(commafyR(12345));
        System.out.println(commafyR(123450));
        System.out.println(commafyR(1230000));
        System.out.println(commafyF(45678900));
        System.out.println(commafyF(1));
        System.out.println(commafyF(10));
        System.out.println(commafyF(101));
        System.out.println(commafyF(1000));
        System.out.println(commafyF(12345));
        System.out.println(commafyF(123450));
        System.out.println(commafyF(1230000));
        System.out.println(commafyF(45678900)); */
        for (String str: args) {
            pl(commafyR(Integer.parseInt(str)));
        }
    }
    public static void pl(String s) {
        System.out.println(s);
    }
}