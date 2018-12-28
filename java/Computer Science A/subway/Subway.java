package subway;
public class Subway {
	private int lineNumber;
	private int length;
	private int stationNumber;
	private int interchangeNumber;
	private double crowdIndex;
	private int startYear;
	public int getLineNumber() {
		return lineNumber;
	}
	public void setLineNumber(int lineNumber) {
		this.lineNumber = lineNumber;
	}
	public int getLength() {
		return length;
	}
	public void setLength(int length) {
		this.length = length;
	}
	public int getStationNumber() {
		return stationNumber;
	}
	public void setStationNumber(int stationNumber) {
		this.stationNumber = stationNumber;
	}
	public int getInterchangeNumber() {
		return interchangeNumber;
	}
	public void setInterchangeNumber(int interchangeNumber) {
		this.interchangeNumber = interchangeNumber;
	}
	public double getCrowdIndex() {
		return crowdIndex;
	}
	public void setCrowdIndex(double crowdIndex) {
		this.crowdIndex = crowdIndex;
	}
	public int getStartYear() {
		return startYear;
	}
	public void setStartYear(int startYear) {
		this.startYear = startYear;
	}
	public Subway(int lineNumber, int length, int stationNumber, int interchangeNumber, double crowdIndex,
			int startYear) {
		super();
		this.lineNumber = lineNumber;
		this.length = length;
		this.stationNumber = stationNumber;
		this.interchangeNumber = interchangeNumber;
		this.crowdIndex = crowdIndex;
		this.startYear = startYear;
	}
}
