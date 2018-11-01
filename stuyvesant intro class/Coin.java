//Haiyao Liu
//APCS1 pd3
//HW16 -- Wayne's World
//2016-10-13


public class Coin {
    
    //instance variables
    private double value; //float
    private String upFace;
    private String name;
    private int flipCtr;
    private int headsCtr;
    private int tailsCtr;
    private double bias; //float
    
    //constructors
    public Coin() {
        value = 0.0;
        upFace = "EDGE";                            //unflipped state. could be useful
        name = "infinity";                          //unnamed coin. value 0
        flipCtr = 0;                                //flipcounts all init at 0
        headsCtr = 0;
        tailsCtr = 0;
        bias = 0.6;                                 //weighted coin
    }
    public Coin(String d) {
        this();
        setName(d);
    }
    public Coin(String d, String f) {
        this(d);
        setFace(f);
    }
    
    //methods, sets and gets
    public void setName(String d) {
        name = d;
    }
    public void setFace(String f) {
        upFace = f;
    }
    public String getFace() {
        //System.out.println(upFace);       cut because printing will be handled elsewhere
        return upFace;
    }
    public String getName() {
        return name;
    }
    public int getFlip() {
        return flipCtr;
    }
    public int getHeads() {
        return headsCtr;
    }
    public int getTails() {
        return tailsCtr;
    }
    public boolean isHeads() {
        return upFace == "heads";
    }
    public boolean isTails() {
        return upFace == "tails";
    }
    
    //methods, class specific
    public void assignValue() {
        if (name == "penny") {
            value = 0.01;
        } else if (name == "nickel") {
            value = 0.05;
        } else if (name == "dime") {
            value = 0.10;
        } else if (name == "quarter") {
            value = 0.25;
        } else if (name == "dollar") {
            value = 1.00;
        } else {
            value = 0.00;                           //sub-optimal value assignment method - then again, the names don't have any logical relation to the values that a computer can utilize
        }
    }
    public String flip() {
        flipCtr += 1;                               //+1 flip() invoke count
        if (Math.random() < bias) {
            headsCtr += 1;                          //+1 heads
            upFace = "heads";
            return upFace;
        }
        tailsCtr += 1;                              //+1 tails
        upFace = "tails";
        return upFace;
        
    }
    
    //methods, overwrites and overloads
    public String toString() {
        return "\t" + name + ":\t" + upFace;
    }
    public boolean equals(Coin coin) {
        //it would be convenient in this case if you could reference the variable name that points to the memory holding a certain object from a method within that method.
        //but only here. can't think of any other applications.
        //String str = "yours: " + getName() + getFace();
        //str += "\ntheirs" + coin.getName() + coin.getFace();
        //System.out.println(str);
        return this.getFace() == coin.getFace();
    }
}