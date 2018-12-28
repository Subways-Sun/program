package subway;
public class ShanghaiMetro extends Subway {
	private int mostInterchange;
	public ShanghaiMetro(int lineNumber, int length, int stationNumber, int interchangeNumber, double crowdIndex,
			int startYear, int mostInterchange) {
		super(lineNumber, length, stationNumber, interchangeNumber, crowdIndex, startYear);
		this.setMostInterchange(mostInterchange);
	}
	public int getMostInterchange() {
		return mostInterchange;
	}
	public void setMostInterchange(int mostInterchange) {
		this.mostInterchange = mostInterchange;
	}
}
