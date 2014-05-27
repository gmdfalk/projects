package grundkurs;

import grundkurs.tools.IOTools;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.InputMismatchException;

public class InputOutput {
	public static void random() {
		char ab, xy;
		int a = 0x1;
		double c = 1e2;
	}

	public static void input() {
		try {
			BufferedReader stdIn = new BufferedReader(new InputStreamReader(
					System.in));
			System.out.print("Enter your name: ");
			String userName = stdIn.readLine();
			System.out.print("Enter your age in years: ");
			String userAge = stdIn.readLine();
			int days = Integer.parseInt(userAge) * 365;
			System.out.println("Hello " + userName + ", you are " + days
					+ " days old.");
		} catch (IOException ie) {
			ie.printStackTrace();
		}
	}

	public static void inputAlt() {
		int zip = 0;
		double num = 0;
		String city, flavor, output;
		Scanner keyboard = new Scanner(System.in);
		System.out.println("What city do you live in? ");
		city = keyboard.next();
		System.out.println("Whats your zipcode? ");
		if (keyboard.hasNextInt()) {
			zip = keyboard.nextInt();
		}
		keyboard.next();
		System.out.println("A number between 0 and 1? ");
		if (keyboard.hasNextDouble() && keyboard.nextDouble() <= 1.0) {
			num = keyboard.nextDouble();
		}
		keyboard.next();
		System.out.println("Your favorite ice cream flavor? ");
		flavor = keyboard.next();
		output = "Hey, you are from %s (%s), the number was %s and your favorite ice cream is %s!";
		System.out.println(String.format(output, city, zip, num, flavor));
		keyboard.close();
	}

	public static void nums() {
		int a = 1, b = 2, c = 3, d = 4;
		System.out.println(++a); // 2
		System.out.println(a); // 2
		System.out.println(b++); // 2
		System.out.println(b); // 3
		System.out.println((++c) + (++c)); // 9
		System.out.println(c); // 5
		System.out.println((d++) + (d++)); // 9
		System.out.println(d); // 6
	}

	public static double add() {
		double x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6;
		x1 = 1e10;
		x2 = 1223;
		x3 = 1e18;
		x4 = 1e15;
		x5 = 3;
		x6 = -1e12;
		y1 = 1e20;
		y2 = 2;
		y3 = -1e22;
		y4 = 1e13;
		y5 = 2111;
		y6 = 1e16;
		return x1 * y1 + x2 * y2 + x3 * y3 + x4 * y4 + x5 * y5 + x6 * y6;
	}

	public static double paren() {
		double x = 192119201;
		double y = 35675640;
		double x2 = x * x;
		double y2 = y * y;
		double s = (1682 * x * y2 * y2 + 3 * x2 * x + 29 * x * y2 - 2 * x2 * x2
				* x + 832);
		return s * (1.0 / 107751.0);
	}

	public static void main(String[] args) {
		// toolsInput();
		// input();
		// inputAlt();
		// nums();
		System.out.println(add());
		System.out.println(paren());
	}

	private static void toolsInput() {
		int i, j, k;
		double d;
		char c;
		boolean b;
		i = IOTools.readInteger();
		System.out.print("j = ");
		j = IOTools.readInteger();
		k = IOTools.readInteger("k = ");
		d = IOTools.readDouble("d = ");
		c = IOTools.readChar("c = ");
		b = IOTools.readBoolean("b = ");
		System.out.println("i = " + i);
		System.out.println("j = " + j);
		System.out.println("k = " + k);
		System.out.println("d = " + d);
		System.out.println("c = " + c);
		System.out.println("b = " + b);
	}
}
