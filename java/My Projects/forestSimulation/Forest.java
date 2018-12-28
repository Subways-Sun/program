package forestSimulation;
public class Forest {
	public static void main(String[] args) {
		int[][] forest= {{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},
				{0,0,0,0,0,0,0,0,0,0},{0,0,0,2,1,2,1,0,0,0},{0,0,0,1,2,1,2,0,0,0},
				{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0}};
		System.out.println("Initial Condition:");
		for (int[] row:forest) {
			for (int column:row) {
				System.out.print(column+" ");
			}
			System.out.println();
		}
		for (int c=0;c<10;c++) {
			System.out.println();
			int[][] temp=new int[forest.length][forest[0].length];
			for (int i=0;i<forest.length;i++) {
				for (int j=0;j<forest[i].length;j++) {
					if (forest[i][j]==0) {
						if (i>0&&forest[i-1][j]==1) temp[i][j]=1;
						else if (i<forest.length-1&&forest[i+1][j]==1) temp[i][j]=1;
						else if (j>0&&forest[i][j-1]==1) temp[i][j]=1;
						else if (j<forest[i].length-1&&forest[i][j+1]==1) temp[i][j]=1;
					}
					else if (forest[i][j]==1) temp[i][j]=2;
					else if (forest[i][j]==2) temp[i][j]=0;
				}
			}
			forest=temp;
			System.out.printf("Year %d:\n",c+1);
			for (int[] row:forest) {
				for (int column:row) {
					System.out.print(column+" ");
				}
				System.out.println();
			}
		}
	}
}
