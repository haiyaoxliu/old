//Haiyao Liu
//APCS1 pd3
//HW21 -- reverseroF
//2016-10-24

public class Foresrever {
	
	//count down from int n, print each count and then an end message
    public static void countDown(int n) {
    	
    	//iterate from n (init) to >0 (test) with a step of -1
		for (int i = n; i > 0; i--) {
			
			//print the counter
			System.out.println(i);
		}
		
		//print ending message
		System.out.println("0");
    }

	//create fence with int n posts of form "|--|--|--..." with n "|"s.
    public static String fenceF(int posts) {
    	
    	//if we're trying to create a degenerate fence, return nothing
    	if (posts < 1) {
    		return "";
    	}
    	
    	//init return str
		String fence = "";
		
		
		//posts-1 iterations, a +1 step counter in the interval [1,posts)
		for (int i = 1; i < posts; i++) {
			
			//add segment to fence
			fence += "|--";
		}
		
		//add ending fencepost (independent of posts-1 loop above)
		fence += "|";
		
		return fence;
    }

	//esrever string with roF loop
    public static String reverseF(String s) {
    	
    	//init return str
		String rev = "";
		
		//for each char in str counting from the end, append that char to return str
		for (int i = s.length(); i > 0; i--) {
			rev += s.charAt(i-1);
		}
		
		return rev;
    }
    
    //esrever string with noisruceR
    public static String reverseR(String s) {
    	
    	//base case: esrever of "" is "";
		if (s.length() == 0) {
			return "";
		}
		
		//esrever(str) = last char of str + esrever(rest of str);
		return s.charAt(s.length()-1) + reverseR(s.substring(0,s.length()-1));
    }

    //tests
    public static void main(String[] args) {
		countDown(5);
		System.out.println(fenceF(0));
		System.out.println(fenceF(1));
		System.out.println(fenceF(2));
		System.out.println(reverseF("1234567890"));
		System.out.println(reverseR("1234567890"));
		System.out.println(reverseF("0"));
		System.out.println(reverseR("0"));
    }
}