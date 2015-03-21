
public class Car {
	
	/** This class is the controller for our cars.
	 *  Cars should be able to accelerate, slow down, change direction
	 *  change gear, activate weapons, 
	 */
	
	private Integer speed = 0;
	private Integer rpm = 0;
	private Integer tyreForce = 0;
	private Integer tyrerpm = 0;
	private Integer rpmMax;
	
	public Car() {
	rpmMax = 6000;
	}
	
	public void accelPedal (boolean pedal){
		
		if (pedal && rpm < rpmMax) {
			rpm++;
		}
		if (!pedal) {
			rpm--;
		}
		
	}
	
	private void calcTyreForce(int rpm){

		
	}
	
	public void changeDir (int x){
		
	}
	
	public void changeGear (int x){
		
	}
	
	public void useWeapon (int x){
		
	}
	
}
