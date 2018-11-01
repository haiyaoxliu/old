/*
Haiyao Liu
APCS1 pd3
HW10 -- CMYM
2016-09-27
Team Make it Rain: Judy Liu, Daniel Ju, Haiyao Liu

==========================================================================================================

                __                                                                      __
              _/  |_  INSECURE BANKING                                                _/  |_
             / $$   \  RELEASE: v -∞                                                 / $$   \
            /$$$$$$  |  Hide your monies with the latest version developed by:      /$$$$$$  |
            $$ \__$$/  Team MAKE IT RAIN                                            $$ \__$$/
            $$      \                                                               $$      \
             $$$$$$  |  DOCUMENTATION: githubs.coms/makeitrain/lotsofgreendollars    $$$$$$  |
            /  \__$$ |  team MIR: Judy Liu, Daniel Ju, Haiyao Liu                   /  \__$$ |
            $$    $$/                                    (myself)                   $$    $$/
             $$$$$$/  ©27.09.2016                                                    $$$$$$/
               $$/                                                                     $$/

$$\      $$\           $$\                       $$$$$$\ $$\           $$$$$$$\            $$\           
$$$\    $$$ |          $$ |                      \_$$  _|$$ |          $$  __$$\           \__|          
$$$$\  $$$$ | $$$$$$\  $$ |  $$\  $$$$$$\          $$ |$$$$$$\         $$ |  $$ | $$$$$$\  $$\ $$$$$$$\  
$$\$$\$$ $$ | \____$$\ $$ | $$  |$$  __$$\         $$ |\_$$  _|        $$$$$$$  | \____$$\ $$ |$$  __$$\ 
$$ \$$$  $$ | $$$$$$$ |$$$$$$  / $$$$$$$$ |        $$ |  $$ |          $$  __$$<  $$$$$$$ |$$ |$$ |  $$ |
$$ |\$  /$$ |$$  __$$ |$$  _$$<  $$   ____|        $$ |  $$ |$$\       $$ |  $$ |$$  __$$ |$$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$$ |$$ | \$$\ \$$$$$$$\       $$$$$$\ \$$$$  |      $$ |  $$ |\$$$$$$$ |$$ |$$ |  $$ |
\__|     \__| \_______|\__|  \__| \_______|      \______| \____/       \__|  \__| \_______|\__|\__|  \__|

==========================================================================================================

-cred to TAAG

*/

public class BankAccount {
    private String name;    //owner name is a string
    private String pwd;     //password is a string
    private int pin;      // 4 digit pin number only requires 4 decimal places so a int can cover that, (changed: avoid typecasting)
    private int accnum;     // 9 digit account number can't be a int so int covers it
    private double accbal;   //account balance might be small, like, small loan of a million dollars small, so double is needed.
    
  //constructors
  
    //default
    public BankAccount() {
        //testing account
        name = "crooked hillary";
        pwd = "interest rate is 100% but 100% of 0 is still 0 rip";
        pin = 0000;
        accnum = 123456789;
        accbal = 694000000.99;  //says his company made this much. but h-where is your tax return?
    }
    
    //variable setting constructor
      //assigns value all variables. though this would be changed in the future
      //to split it into functions to handle cases with less parameters
    public BankAccount(String owner, int num, int pn, String pass, double bal) {  //ideally this would only accept either name or num, and pin or pass.
        if (pn < 9999 && pn > 999 && num < 999999999 && num > 100000000) {
            pin = pn;
            accnum = num;
            name = owner;
            pwd = pass;
            accbal = bal;
        } else {
            System.out.println("Invalid pin or account number: pin must be a 4 digit number from 1000-9998, account number must be a 9 digit number from 100000000-999999998.");
        }
    }
    
  //methods
    //print out all info. can be modified later to split and print out only certain info
    public void getInfo() {
        System.out.println("Owner: " + name);
        System.out.println("Password: " + pwd);     //this is evidently a very bad thing but printing all info is a good test
        System.out.println("PIN: " + pin);          //similar case for this line
        System.out.println("Account Number: " + accnum);
        System.out.println("Account Balance: " + accbal);
    }
  /*
    returning this information can be an alternative method.
    public String retInfo() {
        String ret;
        ret = "Owner: " + name + 
            "\nPassword: " + pwd +          //this is evidently a very bad thing but returning all info is a good test
            "\nPIN: " + pin +               //similar case for this line
            "\nAccount Number: " + accnum +
            "\nAccount Balance: " + accbal;
        return ret;
    }
  */
    //depositing and withdrawing money are essentially both the same (addition to accbal, whether it be positive or negative)
    //however, we have not reviewed any conditionals yet so writing out both would suffice:
    
    public void deposit(double dollars) {
        accbal += dollars;                  //add to balance
    }
    public boolean withdraw(double dollars) {
        if (dollars > accbal) {
            System.out.println("Your account does not have that much money.");
            return false;
        }
        accbal -= dollars;                  //subtract from balance
        return true;
    }
    public boolean auth(String nm, String ps) {
        if (name == nm && pwd == ps) {
            return true;
        }
        return false;
    }
  //main method
    public static void main(String[] args) {
        BankAccount test = new BankAccount("Daniel", 999999988, 1111, "password", 4.5);
    	test.getInfo();
	}
}