package grundkurs;

import java.util.Scanner;

import grundkurs.tools.IOTools;

public class NonPrimitives {
	public static void main(String[] args) {
		Integer a = 10, b = 20;
		System.out.println(a * b);
		createFields();
		// swap();
		// calendar();
		multiDimensional();
	}

	private static void multiDimensional() {
		String[][] appointments;
		appointments = new String[31][];
		for (int i = 0; i < appointments.length; i++) {
			appointments[i] = new String[24];
			for (int j = 0; j < appointments[i].length; j++)
				appointments[i][j] = "";
		}
		appointments[13][23] = "test";
		System.out.println(appointments[13][23]);
	}

	private static void calendar() {
		String[] appointments = new String[24];
		for (int i = 0; i < appointments.length; i++)
			appointments[i] = "";
		boolean done = false;
		Scanner in = new Scanner(System.in);
		while (!done) {
			System.out.println("1 = New Entry");
			System.out.println("2 = Show appointment");
			System.out.println("3 = Quit");
			int choice = in.nextInt();
			switch (choice) {
			case 1:
				System.out.println("What hour?");
				int hour = in.nextInt();
				if (hour < 0 | hour > 23) {
					System.out.println("Is that hour really on your clock?");
					break;
				}
				System.out.println("What is your entry?");
				String entry = in.next();
				appointments[hour] = entry;
				break;
			case 2:
				for (int i = 0; i < 24; i++)
					System.out.println(i + " Uhr: " + appointments[i]);
				break;
			case 3:
				done = true;
				break;
			default:
				System.out.println("Invalid choice.");
			}
		}
	}

	private static void createFields() {
		int[] field1 = new int[5];
		double[] field2 = new double[2];
		String[] field3 = new String[4];
		int[] field4 = { 0, 1, 2, 3, 4, 5 };
		field1[4] = 1;
		field2[0] = 3.14;
		int[] field5 = new int[6];
		System.arraycopy(field4, 0, field5, 0, field4.length);
		for (int i : field5)
			System.out.println(i);
	}

	public static void swap() {
		int n = 12;
		int[] werte1 = new int[n];
		// Lese die Werte von der Tastatur ein
		for (int i = 0; i < werte1.length; i++)
			werte1[i] = IOTools.readInteger("Wert Nr. " + i + ": ");
		// Wie viele Werte sollen in Reihe 2 eingelesen werden?
		n = IOTools.readInteger("Wie viele Werte? "); // n wird geaendert!
		// Lege ein Feld an
		int[] werte2 = new int[n];
		// Lese die Werte von der Tastatur ein
		for (int i = 0; i < werte2.length; i++)
			werte2[i] = IOTools.readInteger("Wert Nr. " + i + ": ");
		// Gib die Werte verkehrt herum aus
		System.out.println("Reihe 1 verkehrt herum");
		for (int i = 0; i < werte1.length; i++)
			System.out.println("Wert Nr. " + i + ": "
					+ werte1[werte1.length - 1 - i]);
		System.out.println("Reihe 2 verkehrt herum");
		for (int i = 0; i < werte2.length; i++)
			System.out.println("Wert Nr. " + i + ": "
					+ werte2[werte2.length - 1 - i]);
	}
}
