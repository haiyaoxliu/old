public class Tests {
    
    public static void main(String args[]) {
        
        //test all combinations of ints and doubles that have integer/noninteger means
        //parameters, expect result
        
        //mean--------------------------------------------------
        
        //int int, 3 passed
        System.out.println(oct6hSTATS.mean(3,4));
        
        //int int, 4 passed
        System.out.println(oct6hSTATS.mean(3,5));
        
        //dbl int, 3.5 pass
        System.out.println(oct6hSTATS.mean(3.0,4));
        
        //dbl int, 4.0 pass
        System.out.println(oct6hSTATS.mean(3.0,5));
        
        //dbl dbl, 3.5 pass
        System.out.println(oct6hSTATS.mean(3.0,4.0));
        
        //dbl dbl, 4.0 pass
        System.out.println(oct6hSTATS.mean(3.0,5.0));
        
        //max---------------------------------------------------
        
        //int int, 12 passed
        System.out.println(oct6hSTATS.max(5,12));
        
        //int int, 13 passed
        System.out.println(oct6hSTATS.max(5,13));
        
        //dbl int, 12.0 pass
        System.out.println(oct6hSTATS.max(5.0,12));
        
        //dbl int, 13.0 pass
        System.out.println(oct6hSTATS.max(5.0,13));
        
        //dbl dbl, 12.0 pass
        System.out.println(oct6hSTATS.max(5.0,12.0));
        
        //dbl dbl, 13.0 pass
        System.out.println(oct6hSTATS.max(5.0,13.0));
        
        //geomean-----------------------------------------------
        
        //int int, 2 passed
        System.out.println(oct6hSTATS.geoMean(1,4));
        
        //int int, 3 passed
        System.out.println(oct6hSTATS.geoMean(1,9));
        
        //dbl int, 4.0 pass
        System.out.println(oct6hSTATS.geoMean(1.0,16));
        
        //dbl int, 5.0 pass
        System.out.println(oct6hSTATS.geoMean(1.0,25));
        
        //dbl dbl, 6.0 pass
        System.out.println(oct6hSTATS.geoMean(1.0,36.0));
        
        //dbl dbl, 7.0 pass
        System.out.println(oct6hSTATS.geoMean(1.0,49.0));
        
    }
}