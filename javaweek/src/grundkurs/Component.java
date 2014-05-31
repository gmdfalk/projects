package grundkurs;

public class Component {
	public int wert;
	public Component ref;

	public void main(String[] args) {
		Referenzen r = new Referenzen();
		r.main(args);
	}

	public class Referenzen {
		public void main(String[] args) {
			int matrNr = 123456; // Hier Ihre Matrikelnummer eintragen!
			Component p, q;
			int i;
			p = new Component();
			p.ref = null;
			p.wert = matrNr % 10;
			matrNr = matrNr / 10;
			for (i = 2; i <= 3; i++) {
				q = new Component();
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
}