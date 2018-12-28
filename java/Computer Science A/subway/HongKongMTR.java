package subway;
public class HongKongMTR extends Subway {
	private int maximumSpeed;
	public HongKongMTR(int lineNumber, int length, int stationNumber, int interchangeNumber, double crowdIndex,
			int startYear, int maximumSpeed) {
		super(lineNumber, length, stationNumber, interchangeNumber, crowdIndex, startYear);
		this.setMaximumSpeed(maximumSpeed);
	}
	public int getMaximumSpeed() {
		return maximumSpeed;
	}
	public void setMaximumSpeed(int maximumSpeed) {
		this.maximumSpeed = maximumSpeed;
	}
}
