package grundkurs;

public class FlowControl {
	public static void main(String[] args) {
		// scope();
		switchy(3);
	}

	public static void scope() {
		// Default scope is package-private.
		int x = 5;
		// Deklarationsanweisung und Zuweisung
		x++;
		// Postfix-Inkrement-Anweisung
		{
			// Anfang des ersten inneren Blocks
			long y;
			// Deklarationsanweisung
			y = x + 123456789;
			// Zuweisung
			System.out.println(y);
			// Ausgabeanweisung/Methodenaufruf
			;
			// Leere Anweisung
		}
		System.out.println(x); // Ausgabeanweisung/Methodenaufruf
		{
			// Anfang des zweiten inneren Blocks
			double d;
			// Deklarationsanweisung
			d = x + 1.5;
			// Zuweisung
			System.out.println(d);
			// Ausgabeanweisung/Methodenaufruf
		}
	}

	public static void switchy(int n) {
		switch (n) {
		case 1:
			System.out.println(1);
			break;
		case 2:
			System.out.println(2);
			break;
		case 3:
			System.out.println(3);
			// fallout.
		case 4:
			System.out.println(4);
			break;
		default:
			System.out.println("Not caught");
		}
	}
}
