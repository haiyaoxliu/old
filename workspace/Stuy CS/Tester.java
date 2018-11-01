public class Tester {
    static BankAccount test = new BankAccount();
    static BankAccount hy = new BankAccount("haiyao", 0, (short)0000, "securepassword", 1234567890);
    public static void main(String[] args) {
        test.getInfo();
        hy.getInfo();
    }
}