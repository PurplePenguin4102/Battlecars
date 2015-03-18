
public class Car {
	
	/** This class is the controller for our cars.
	 *  Cars should be able to accelerate, slow down, change direction
	 *  change gear, activate weapons, 
	 */
	private static Integer speed = 0;
	private static Integer rpm = 0;
	private static Integer tyreForce = 0;
	private static Integer tyrerpm = 0;
	private static Integer rpmMax;
	
	public Car() {
	rpmMax = 6000;
	}
	
	public static void accelPedal (boolean pedal){
		
		if (pedal && rpm < rpmMax) {
			rpm++;
		}
		if (!pedal) {
			rpm--;
		}
		
	}
	
	private static void calcTyreForce(int rpm){
		
		
	}
	
	public static void changeDir (int x){
		
	}
	
	public static void changeGear (int x){
		
	}
	
	public static void useWeapon (int x){
		
	}
	
}
