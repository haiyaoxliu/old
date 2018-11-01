//Haiyao Liu
//APCS1 pd3
//HW26 -- I Demand Arrays!
//2016-11-02

public class ArrayUtils {
    public static int[] fillr(int[] ints) {
        //foreach does not allow reassignment of array elements
        for (int i = 0; i < ints.length; i++) {
            //reassign int to a random number in [0,100)
            ints[i] = (int)(Math.random() * 100);
        }
        return ints;
    }
    public static String space(int[] ints) {
        String str = "";
        for (int i: ints) {
            //add next int and a space
            str += i + " ";
        }
        //return
        return str;
    }
    public static String space(String[] strs) {
        String str = "";
        for (String i: strs) {
            //add next int and a space
            str += i + " ";
        }
        //return
        return str;
    }
    public static void main(String[] args) {
        int[] a = new int[5];
        System.out.println(space(fillr(a)));
    }
}