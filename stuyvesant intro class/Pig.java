//Daniel Ju, Judy Liu, Haiyao Liu
//APCS1 pd3
//HW25 -- ? ? ?
//2016-10-31

//Team Brick House FTW

//class Pig
//a Pig Latin translator
//SKELETON from Q&A Forum

/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
           9
     ,--.-'-,--.
     \  /-~-\  /
    / )' a a `( \
   ( (  ,---.  ) )
    \ `(_o_o_)' /
     \   `-'   /
      | |---| |     
      [_]   [_]
      PROTIP: Make this class compilable first, 
      then develop and test one method at a time.
      NEVER STRAY TOO FAR FROM COMPILABILITY/RUNNABILITY!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/

public class Pig {
    //Q: How does this initialization make your life easier?
    //
    private static final String VOWELS = "aeiou";
    private static final String PUNCTS = "!?.,";


    /*=====================================
      boolean hasA(String,String) -- checks for a letter in a String
      pre:  w != null, letter.length() == 1
      post: hasA("cat", "a") → true  
      hasA("cat", "p") → false
      =====================================*/
    public static boolean hasA( String w, String letter ) {
        return w.indexOf(letter) > -1;
    }//end hasA()


    /*=====================================
      boolean isAVowel(String) -- tells whether a letter is a vowel
      precondition: letter.length() == 1
      =====================================*/
    public static boolean isAVowel( String letter ) {
    	return hasA(VOWELS,letter.toLowerCase());
    }


    /*=====================================
      int countVowels(String) -- counts vowels in a String
      pre:  w != null
      post: countVowels("meatball") → 3
      =====================================*/
    public static int countVowels( String w ) {
	    int counter = 0;
	    for (int i = 0; i < w.length(); i++) {
	        if (isAVowel(w.substring(i,i+1))) {
	            counter += 1;
	        }
	    }
	    return counter;
    }


    /*=====================================
      boolean hasAVowel(String) -- tells whether a String has a vowel
      pre:  w != null
      post: hasAVowel("cat") → true
      hasAVowel("zzz") → false
      =====================================*/
    public static boolean hasAVowel( String w ) {
    	for (int i = 0; i < w.length(); i++) {
    	  if (isAVowel(w.substring(i,i+1))) {
    	    return true;
    	  }
    	}
    	return false;
    }


    /*=====================================
      String allVowels(String) -- returns vowels in a String
      pre:  w != null
      post: allVowels("meatball") → "eaa"
      =====================================*/
    public static String allVowels( String w ) {
      String vowels = "";
	    for (int i = 0; i < w.length(); i++) {
    	  if (isAVowel(w.substring(i,i+1))) {
    	    vowels += w.substring(i,i+1);
    	  }
    	}
    	return vowels;
    }


    /*=====================================
      String firstVowel(String) -- returns first vowel in a String
      pre:  w != null
      post: firstVowel("") --> ""
      firstVowel("zzz") --> ""
      firstVowel("meatball") --> "e"
      =====================================*/
    public static String firstVowel( String w ) {
	    for (int i = 0; i < w.length(); i++) {
    	  if (isAVowel(w.substring(i,i+1))) {
    	    return w.substring(i,i+1);
    	  }
    	}
    	return "";
    }

    //return index instead, might be useful
    public static int firstVowelI( String w ) {
	    for (int i = 0; i < w.length(); i++) {
    	  if (isAVowel(w.substring(i,i+1))) {
    	    return i;
    	  }
    	}
    	return -1;
    }

    /*=====================================
      boolean beginsWithVowel(String) -- tells whether a String begins with a vowel
      pre:  w != null and w.length() > 0
      post: beginsWithVowel("apple")  --> true
      beginsWithVowel("strong") --> false
      =====================================*/
    public static boolean beginsWithVowel( String w ) {
	    return isAVowel(w.substring(0,1));
    }
    
    public static int firstPunc( String s ) {
      for (int i = 0; i < s.length(); i++) {
        if (hasA(PUNCTS,s.substring(i,i+1))) {
          return i;
        }
      }
      return -1;
    }


    /*=====================================
      String engToPig(String) -- converts an English word to Pig Latin
      pre:  w.length() > 0
      post: engToPig("apple")  --> "appleway"
      engToPig("strong") --> "ongstray"
      engToPig("java")   --> "avajay"
      =====================================*/
    public static String engToPig( String w ) {
      //remove capitalization and punctuation for conversion
      //only considers first letter capitalizaton and ending punctuation
      boolean caps = w.substring(0,1).equals(w.substring(0,1).toUpperCase());
      w = w.toLowerCase();
      String punc = "";
      if (firstPunc(w) > -1) {
        punc = w.substring(firstPunc(w));
        w = w.substring(0,firstPunc(w));
      }
      
      //conversion part
      
      String pigged = "";
      
      //starting letter is a consonant
      if (!beginsWithVowel(w)) {
        //System.out.println(w.substring(1).indexOf("y"));
        //System.out.println(firstVowelI(w.substring(1)));
        int firstY = w.substring(1).indexOf("y");
        int firstVowel = firstVowelI(w.substring(1));
        
        if ( firstVowel > -1 && firstY > -1 ) {
          int cut = Math.min(firstY,firstVowel) + 1;
          pigged = w.substring(cut) + w.substring(0,cut) + "ay";
        } else if ( firstVowel > -1 || firstY > -1 ) {
          int cut = Math.max(firstY,firstVowel) + 1;
          pigged = w.substring(cut) + w.substring(0,cut) + "ay";
        } else {
          pigged = w + "ay";
        }
      } else {
        //simple case - starting letter is a vowel and we simply add "way"
        pigged = w + "way";
      }
      
      if(caps) {
        return pigged.substring(0,1).toUpperCase() + pigged.substring(1) + punc;
      }
      return pigged + punc;
    }

    public static void p(String s) {
      System.out.println(s);
    }

    public static void main( String[] args ) {

      p(engToPig("yttrium"));
      p(engToPig("Baby"));
      p(engToPig("my!!"));
      p(engToPig("by"));
      p(engToPig("yellow."));
      p(engToPig("Tryst??"));
   /*   
      engToPig("yttrium");
      engToPig("baby");
      engToPig("my");
      engToPig("by");
      engToPig("yellow");
      engToPig("tryst");*/
      
	
    }//end main()

}//end class Pig

