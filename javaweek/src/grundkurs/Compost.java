package grundkurs;

public class Compost {

	public int wert;
	public Compost ref;

	public static void main(String[] args) {
		Referenzen r = new Referenzen();
		r.main(args);
	}

}

class Referenzen {
	public static void main(String[] args) {
		int matrNr = 123456;
		Compost p, q;
		int i;
		p = new Compost();
		p.ref = null;
		p.wert = matrNr % 10;
		matrNr = matrNr / 10;
		for (i = 2; i <= 3; i++) {
			q = new Compost();
			q.ref = p;
			p = q;
			p.wert = matrNr % 10;
			matrNr = matrNr / 10;
		}
		for (i = 1; i <= 3; i++) {
			System.out.print(p.wert);
			p = p.ref;
		}
		System.out.println("1");
	}
}