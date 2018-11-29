package projects;
import java.util.ArrayList;
import java.util.Scanner;
public class FractionCalculationEasy {
	public static void main(String[] args) {
		System.out.print("Please enter the first fraction: ");
		Scanner input1=new Scanner(System.in);
		String in1=input1.next();
		String[] firstfraction=in1.split("/");
		int firstnu=Integer.parseInt(firstfraction[0]);
		int firstde=Integer.parseInt(firstfraction[1]);
		System.out.print("Please enter the second fraction: ");
		Scanner input2=new Scanner(System.in);
		String in2=input2.next();
		String[] secondfraction=in2.split("/");
		int secondnu=Integer.parseInt(secondfraction[0]);
		int secondde=Integer.parseInt(secondfraction[1]);
		System.out.print("Please enter the expression: ");
		Scanner input3=new Scanner(System.in);
		String exp=input3.next();
		int nu=0,de=0;
		if (exp.equals("+")) {
			nu=firstnu*secondde+secondnu*firstde;
			de=firstde*secondde;
		}
		if (exp.equals("-")) {
			nu=firstnu*secondde-secondnu*firstde;
			de=firstde*secondde;
		}
		if (exp.equals("*")) {
			nu=firstnu*secondnu;
			de=firstde*secondde;
		}
		if (exp.equals("/")) {
			nu=firstnu*secondde;
			de=firstde*secondnu;
		}
		int min=0;
		if (nu>=de&&nu>0) min=de;
		else min=nu;
		ArrayList<Integer> commonfactor=new ArrayList<Integer>();
		for (int i=2;i<min;i++) if (nu%i==0&&de%i==0) commonfactor.add(i);
		nu/=commonfactor.get(commonfactor.size()-1);
		de/=commonfactor.get(commonfactor.size()-1);
		System.out.print("The result is: "+nu+"/"+de);
		input1.close();
		input2.close();
		input3.close();
	}
}
