package subway;
public class BeijingSubway extends Subway {
	private int companyNum;
	public BeijingSubway(int lineNumber, int length, int stationNumber, int interchangeNumber, double crowdIndex,
			int startYear, int companyNum) {
		super(lineNumber, length, stationNumber, interchangeNumber, crowdIndex, startYear);
		this.setCompanyNum(companyNum);
	}
	public int getCompanyNum() {
		return companyNum;
	}
	public void setCompanyNum(int companyNum) {
		this.companyNum = companyNum;
	}
}
