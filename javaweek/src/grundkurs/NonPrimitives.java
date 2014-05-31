package grundkurs;

import grundkurs.tools.IOTools;

import java.util.Arrays;
import java.util.Scanner;

public class NonPrimitives {
	public static class Address {
		// 5.6
		public String name;
		public String street;
		public String city;
		public String mail;
		public String comment;
		public int streetNo;
		public int zipcode;
	}

	public static void main(String[] args) {
		// Integer a = 10, b = 20;
		// System.out.println(a * b);
		// createFields();
		// swap();
		// calendar();
		// multiDimensional();
		// fixedLength();
		// loopComparison();
		// derp();
		// alternates();
		// sortNumbers();
		// magicSquare(2);
		Address a = new Address();
		System.out.println(a.name);
		System.out.println(a.streetNo);
	}

	public static void magicSquare(int n) {
		// 5.5
		if (n < 3) {
			System.out.println("Correcting input to 3.");
			n = 3;
		} else if (n > 10) {
			System.out.println("Correcting input to 10.");
			n = 10;
		}
		int col = n / 2 + 1;
		int row = n / 2;
		int[][] square = new int[n][n];
		for (int i = 1; i <= n * n; i++) {
			square[row][col] = i;
			col += 1;
			row -= 1;
			if (row < 0)
				row = n - 1;
			if (col == n)
				col = 0;
			if (square[row][col] != 0) {
				col += 1;
				row += 1;
				if (row == n)
					row = 0;
				if (col == n)
					col = 0;
			}
		}
		for (int i = 0; i < n; i++)
			// System.out.println(square[i]);
			for (int j = 0; j < n; j++) {
				System.out.print(square[i][j] + "\t");
				if (j == n - 1)
					System.out.println("");
			}
	}

	public static void sortNumbers() {
		// 5.4
		Scanner in = new Scanner(System.in);
		int[] list = new int[5];
		for (int i = 0; i < list.length; i++) {
			System.out.println("Enter an integer: ");
			list[i] = in.nextInt();
		}
		for (int i : list)
			System.out.print(i + " ");
		System.out.println("");
		Arrays.sort(list);
		for (int i : list)
			System.out.print(i + " ");
		System.out.println("");
	}

	public static void alternates() {
		// 5.2
		double[] a, c;
		a = new double[5];
		double[] b = { 1.1, 2.2, 3.3, 4.4, 5.5 };
		c = new double[] { 1.1, 2.2, 3.3, 4.4, 5.5 };

		int[][][][] Feld1 = new int[6][10][8][];
		int[][][][] Feld2 = new int[6][][][];
		for (int d1 = 0; d1 < 6; d1++) {
			Feld2[d1] = new int[10][][];
			for (int d2 = 0; d2 < 10; d2++) {
				Feld2[d1][d2] = new int[8][];
			}
		}
		int[][] g = { { 1, 2, 3 }, { 1, 2, 3 }, { 1, 2, 3 } };
		int[][] h = { { 1, 2, 3 }, { 1, 2, 3 }, { 1, 2, 3 } };
		System.out.println(Feld1.length == Feld2.length);
		System.out.println(g == h); // only compares references.
		System.out.println(Arrays.equals(g, h)); // this works for
													// one-dimensional
													// arrays only.
		System.out.println(Arrays.deepEquals(g, h));

	}

	public static int multiply(int a, int b) {
		// JUnit-tested method.
		/**
		 * @param int a.
		 * @param int b.
		 * @returns Product of a and b.
		 */
		return a * b;
	}

	public static void derp() {
		// 5.1
		byte a, b;
		byte[] aReihe, aZeile, bReihe, bZeile;
		byte[][] aMatrix, bMatrix;
	}

	public static void loopComparison() {
		int[] werte = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
		int summe = 0;
		for (int i = 0; i < werte.length; i++)
			summe = summe + werte[i];
		System.out.println("Summe: " + summe);
		summe = 0;
		for (int x : werte)
			summe = summe + x;
		System.out.println("Summe: " + summe);

		// Zweidimensionale Matrix mit Zeilen unterschiedlicher
		// Laenge (hier speziell eine Dreiecksmatrix)
		int[][] matrix = { { 1 }, { 2, 3 }, { 4, 5, 6 }, { 7, 8, 9, 10 } };
		// Summation der Elemente mit traditioneller Schleifen-Notation
		summe = 0;
		for (int i = 0; i < matrix.length; i++)
			for (int j = 0; j < matrix[i].length; j++)
				summe = summe + matrix[i][j];
		System.out.println("Summe: " + summe);
		// Summation der Elemente mit vereinfachter Schleifen-Notation
		summe = 0;
		for (int[] zeile : matrix)
			for (int element : zeile)
				summe = summe + element;
		System.out.println("Summe: " + summe);
	}

	private static void fixedLength() {
		String[][][] appointments = new String[12][][];
		appointments[0] = new String[31][24]; // Jan
		appointments[1] = new String[28][24]; // Feb
		appointments[2] = new String[31][24]; // March
		appointments[3] = new String[30][24]; // April
		appointments[4] = new String[31][24]; // May
		appointments[5] = new String[30][24]; // June
		appointments[6] = new String[31][24]; // July
		appointments[7] = new String[31][24]; // August
		appointments[8] = new String[30][24]; // September
		appointments[9] = new String[31][24]; // October
		appointments[10] = new String[30][24]; // Nov
		appointments[11] = new String[31][24]; // Dec
		for (int i = 0; i < appointments.length; i++)
			for (int j = 0; j < appointments[i].length; j++)
				for (int k = 0; k < appointments[i][j].length; k++)
					appointments[i][j][k] = "";
	}

	private static void multiDimensional() {
		String[][] appointments;
		appointments = new String[31][];
		for (int i = 0; i < appointments.length; i++) {
			appointments[i] = new String[24];
			for (int j = 0; j < appointments[i].length; j++)
				appointments[i][j] = "";
		}
		boolean done = false;
		Scanner in = new Scanner(System.in);
		while (!done) {
			System.out.println("1 = New Entry");
			System.out.println("2 = Show appointment");
			System.out.println("3 = Quit");
			int choice = in.nextInt();
			switch (choice) {
			case 1:
				System.out.println("What day?");
				int day = in.nextInt();
				if (day < 0 | day > 31) {
					System.out.println("Is that day really on your calendar?");
					break;
				}
				System.out.println("What hour?");
				int hour = in.nextInt();
				if (hour < 0 | hour > 23) {
					System.out.println("Is that hour really on your clock?");
					break;
				}
				System.out.println("What is your entry?");
				String entry = in.next();
				appointments[day][hour] = entry;
				break;
			case 2:
				System.out.println("What day?");
				int printDay = in.nextInt();
				for (int i = 0; i < 24; i++)
					System.out
							.println(i + " Uhr: " + appointments[printDay][i]);
				break;
			case 3:
				done = true;
				break;
			default:
				System.out.println("Invalid choice.");
			}
		}
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
