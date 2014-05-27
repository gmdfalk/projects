package grundkurs;

import grundkurs.tools.IOTools;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

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
	} // fmltest

	public static void main(String[] args) {
		// toolsInput();
		input();
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
