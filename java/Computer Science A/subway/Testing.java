package subway;
public class Testing {
	public static void main(String[] args) {
		BeijingSubway bj=new BeijingSubway(21,600,200,50,0.8,1971,4);
		bj.getCrowdIndex();
		ShanghaiMetro sh=new ShanghaiMetro(18,600,200,50,0.75,1986,4);
		sh.getMostInterchange();
		HongKongMTR hk=new HongKongMTR(11,400,100,40,0.7,1986,130);
		hk.getCrowdIndex();
	}
}
