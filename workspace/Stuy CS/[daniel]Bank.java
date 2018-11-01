//Daniel Ju, Group Make it Rain, (Daniel, Haiyao, Judy)
//APCS1 pd3
//HW10 -- CMYM
//2016-09-27

public class Bank {
    private String Name;   //Account holder full name
    private String PWord;  //Account password
    private short PIN;  //4-digit PIN
    private int AccNum; //9-digit account number
    private float Balance;  //Account balance
    public Bank() {  //Default constructor to set everything to 0
	Balance = 0.0;
	PWord = "";
	PIN = 0000;
	AccNum = 123456789;
	Name = "";
    }
    public Bank(String name, String pword, short pin, int accnum, float balance) { //loaded constructor for setting everything
	Balance = balance;
	PWord = pword;
	PIN = pin;
	AccNum = accnum;
	Name = name;
    }
    public void PrintAccInfo() { // Can be later modified to take a password / PIN and then only printing everything except password and PIN but that would require if statements.
	System.out.println("Owner: " + Name);
        System.out.println("Password: " + PWord);    
        System.out.println("PIN: " + PIN);          
        System.out.println("Account Number: " + AccNum);
        System.out.println("Account Balance: " + Balance);
    }
    
}
