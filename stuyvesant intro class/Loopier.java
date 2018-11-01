//Haiyao Liu
//APCS1 pd3
//HW27 -- Recurse, Recurse, on Elements Not the First! 
//2016-11-03

//useful array methods found on J7API
import java.util.Arrays;

public class Loopier {
    public static int linSearch( int[] a, int target ) {
        //iterate over array. if current a[index] = target return the index
        for (int i = 0; i < a.length; i++) {
            if (a[i] == target) {
                return i;
            }
        }
        //target never found
        return -1;
    }
    public static int linSearchR( int[] a, int target ) {
        //if first element is what we want, return 0 and we're done
        if ( a[0] == target ) {
            return 0;
        }
        //add 1 to account for index that we just iterated over, continue looking
        return 1 + linSearchR(Arrays.copyOfRange(a,1,a.length), target);
    }
    public static int freq( int[] a, int target ) {
        int count = 0;
        //every time a[index] = target add one to counter
        for (int i = 0; i < a.length; i++) {
            if (a[i] == target) {
                count += 1;
            }
        }
        return count;
    }
    public static int freqRec( int[] a, int target ) {
        //if array is empty return 0
        if ( a.length < 1 ) {
            return 0;
        }
        //if current a[index] = translate, add one to account for current frequency and keep looking
        if ( a[0] == target ) {
            return 1 + freqRec(Arrays.copyOfRange(a,1,a.length), target);
        }
        //if not, keep looking
        return freqRec(Arrays.copyOfRange(a,1,a.length), target);
    }
    public static void main(String[] args) {
        int[] a = {0,1,2,3,4,5,6,7,8,9,9,9,0};
        System.out.println(linSearch(a,4));
        System.out.println(linSearchR(a,6));
        System.out.println(freq(a,0));
        System.out.println(freqRec(a,9));
        //reliant on ArrayUtils, commented out
        //System.out.println(ArrayUtils.commafy(a));
    }
}