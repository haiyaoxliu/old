//coin driver

public class CoinDriver{
	public static void main(String[] args) {
		Coin c1 = new Coin("dime","heads");
		Coin c2 = new Coin("quarter", "tails");
		flipHeads(10);
		flipMatch(10);
		flipYear(2000);
	}
	
	public static void flipHeads(int f) {
		int count = 0;
		if (f < 0) {
			System.out.println("Negative number of heads unacceptable");
		}
		Coin c = new Coin();
		System.out.println("Printing coin flips until " + f + " heads:");
		while (f > 0) {
			System.out.println(c.flip());
			if (c.isHeads()) {
				f -= 1;
			}
			count += 1;
		}
		System.out.println("Flipped " + count + " times. " + f + " heads left to flip.\n");
	}
	
	public static void flipMatch(int f) {
		int count = 0;
		if (f < 0) {
			System.out.println("Negative number of matches unacceptable");
		}
		Coin c1 = new Coin();
		Coin c2 = new Coin();
		System.out.println("Printing 2 coin flips until " + f + " matches:");
		while (f > 0) {
			System.out.println(c1.flip() + " " + c2.flip());
			if (c1.equals(c2)) {
				f -= 1;
			}
			count += 1;
		}
		System.out.println("Flipped " + count + " times. " + f + " matches left to flip.\n");
	}

	public static void flipYear(int year) {
		int count = 0;
		if (year < 0) {
			System.out.println("Negative birth year unacceptable");
		}
		Coin c1 = new Coin();
		Coin c2 = new Coin();
		System.out.println("Flipping 2 coins until at least " + 13 + " matches and match number divisible by " + year);
		//int maxFlips = 65536;
		int matches = 0;
		while (matches < 13 || matches % year != 0) { // && maxFlips > 0
			//System.out.println(c1.flip() + " " + c2.flip());
			c1.flip(); c2.flip();
			if (c1.equals(c2)) {
				matches += 1;
			}
			count += 1;
			//maxFlips -= 1;
		}
		System.out.println("Flipped " + count + " times. " + matches + " matches made. Conditions satsified.\n");
	}
}