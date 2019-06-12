package test;
import java.util.ArrayList;
public class TestResults {
	private ArrayList<StudentAnswerSheet> sheets;
	public String highestScoringStudent (ArrayList<String> key) {
		double highScore=Double.MIN_VALUE;
		int highScorePosition=Integer.MIN_VALUE;
		for (int i=0; i<sheets.size(); i++) {
			if (sheets.get(i).getScore(key)>highScore) {
				highScore=sheets.get(i).getScore(key);
				highScorePosition=i;
			}
		}
		return sheets.get(highScorePosition).getName();
	}
}
