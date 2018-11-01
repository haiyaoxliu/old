public class Warrior {
    private String name;
    private int health;
    private int strength;
    private int defense;
    private double attackr;
    
    public Warrior(String n) {
        name = n;
        health = 125;
        strength = 100;
        defense = 40;
        attackr = 0.4;
    }
    
    public boolean isAlive() {
        return health > 0;
    }
    
    public int getDefense() {
        return defense;
    }
    
    public String getName() {
        return name;
    }
    
    public void lowerHP(int dmg) {
        health -= dmg;
    }
    
    public int attack(Monster m) {
        int damage = (int)(strength*attackr-m.getDefense());
        m.lowerHP(damage);
        return damage;
    }
    
    public void specialize() {
        defense -= (int)(strength/10);
        attackr += (int)(strength/100);
    }
    
    public void normalize() {
        defense += (int)(strength/10);
        attackr -= (int)(strength/100);
    }
    
    public static void main(String[] args) {
        
    }
}