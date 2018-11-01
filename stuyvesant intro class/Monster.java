public class Monster {
    private int health;
    private int strength;
    private int defense;
    private double attackr;
    
    public Monster() {
        strength = 20+(int)(Math.random()*45);
        health = 150;
        defense = 1;
        attackr = 1;
    }
    public boolean isAlive() {
        return health > 0;
    }
    
    public int getDefense() {
        return defense;
    }
    
    public void lowerHP(int dmg) {
        health -= dmg;
    }
    
    public int attack(Warrior w) {
        int damage = (int)(strength*attackr-w.getDefense());
        w.lowerHP(damage);
        return damage;
    }
    
    public static void main(String[] args) {
        
    }
}