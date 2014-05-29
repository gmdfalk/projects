package grundkurs;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.InputMismatchException;

import org.apache.commons.lang3.StringUtils;

public class FlowControl {
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

	public static int n = 37; // FlowControl.n

	public static void main(String[] args) {
		// scope();
		// System.out.println(n);
		// switchy(5);
		// loopy();
		// weWereOnABreak();
		// algo();
		// board();
		// fixMe();
		// max(1.0, 2.0, 3.0, 4.0);
		// maxFixed(1.0, 2.0, 3.0, 4.0);
		// stars();
		// crossSum(123456789);
		// toGalacticTime("25.11.2011, 11.11 Uhr");
		// toEarthTime("328825.465");
		// numToText(12345);
		// multiply(10);
		// compoundInterest(100, 0.06, 4);
		// guessingGame();
		// System.out.println(changeBase((short) 1234, (byte) 2));
		// christmasTree();
		// friendlyNumbers((short) 10744, (short) 10856);
		System.out.println(weekDay(1, 04, 2013));
		easterDay(1994);
	}

	private static void easterDay(int year) {
		// 4.36
		int a, b, c, d, e, m, s, n, day, month;
		a = year % 19;
		b = year % 4;
		c = year % 7;
		m = (8 * (year / 100) + 13) / 25 - 2;
		s = year / 100 - year / 400 - 2;
		n = (6 + s) % 7;
		m = (15 + s - m) % 30;
		d = (m + 19 * a) % 30;
		if (d == 29) {
			d = 28;
		} else if (d == 28 && a >= 11) {
			d = 27;
		}
		e = (2 * b + 4 * c + 6 * d + n) % 7;
		day = 21 + d + e + 1;
		if (day > 31) {
			day %= 31;
			month = 4;
		} else {
			month = 3;
		}
		String easterDate = String.format("%02d", day) + "."
				+ String.format("%02d", month) + ".";
		System.out.println("In the year " + year + " Easter Day was the "
				+ easterDate);
	}

	private static String weekDay(int day, int month, int year) {
		// 4. 35
		int century, decade, dayInt;
		String[] days = { "Sunday", "Monday", "Tuesday", "Wednesday",
				"Thursday", "Friday", "Saturday" };
		if (month <= 2) {
			month += 10;
			year -= 1;
		} else {
			month -= 2;
		}
		century = year / 100;
		decade = year % 100;
		dayInt = (((26 * month - 2) / 10) + day + year + year / 4 + century / 4 - 2 * century) % 7;
		if (dayInt < 0)
			dayInt += 7;
		else
			dayInt -= 1;
		return days[dayInt];
	}

	private static ArrayList<Short> getFactors(short num) {
		ArrayList<Short> factors = new ArrayList<Short>();
		for (short i = 1; i < num; i++) {
			if (num % i == 0)
				factors.add(i);
		}
		return factors;
	}

	private static short getFactorSum(short num) {
		short factorSum = 0;
		for (short i = 1; i < num; i++) {
			if (num % i == 0)
				factorSum += i;
		}
		return factorSum;
	}

	private static void friendlyNumbers(short a, short b) {
		// 4.34
		short aFactorSum = getFactorSum(a);
		short bFactorSum = getFactorSum(b);
		ArrayList aFactors = getFactors(a);
		ArrayList bFactors = getFactors(b);
		// for (Object o : aFactors)
		// System.out.println(o);
		System.out.println(aFactors + " " + aFactorSum);
		System.out.println(bFactors + " " + bFactorSum);
		if (bFactorSum == a && aFactorSum == b) {
			System.out.println(a + " and " + b + " are friendly numbers!");
		} else {
			System.out.println("Nope, not friendly.");
		}
	}

	private static void christmasTree() {
		// 4.33
		int spaces = 5;
		String leftSpaces, stars;
		for (int i = 1; i < 10; i += 2) {
			spaces -= 1;
			leftSpaces = buildString1(" ", spaces);
			stars = buildString1("*", i);
			System.out.println(leftSpaces + stars);
		}
		System.out.println(buildString1(" ", 4) + "I");
	}

	private static long changeBase(short decimal, byte base) {
		// 4.32
		long converted = 0;
		if (base > 9 || base < 2)
			return converted;
		long multiplier = 1;
		while (decimal > 0) {
			converted += (decimal % base) * multiplier;
			decimal /= base;
			multiplier *= 10;
			// System.out.println("converted: " + converted + ", decimal: "
			// + decimal + " multiplier: " + multiplier);
		}
		return converted;
	}

	private static void guessingGame() {
		// 4.31
		int winner = (int) (99 * Math.random() + 1);
		int guess = -1;
		int counter = 0;
		Scanner in = new Scanner(System.in);
		System.out.println(winner);
		System.out.println("Guess the number (between 0 and 100)");
		while (guess != winner) {
			try {
				guess = in.nextInt();
				counter += 1;
				if (guess > winner)
					System.out.println("Smaller!");
				else if (guess < winner)
					System.out.println("Bigger!");
			} catch (InputMismatchException e) {
				System.out.println("Invalid input!");
				in.next();
			}
		}
		System.out.println("Yay! You've won! It took you " + counter
				+ " tries!");
	}

	private static void compoundInterest(double amount, double interest,
			double runtime) {
		// 4.30
		String label;
		for (int i = 1; i <= runtime; i++) {
			amount *= (interest + 1.0);
			if (i == 1) {
				label = " year: ";
			} else {
				label = " years: ";
			}
			System.out.println("After " + i + label + amount);
		}
	}

	private static void multiply(int n) {
		// 4.29
		for (int i = 1; i <= 10; i++) {
			System.out.print(i * n + " ");
		}
		System.out.println("");
	}

	private static void numToText(int n) {
		// 4.28
		Map<Integer, String> toText = new HashMap<Integer, String>();
		toText.put(1, "one");
		toText.put(2, "two");
		toText.put(3, "three");
		toText.put(4, "four");
		toText.put(5, "five");
		toText.put(6, "six");
		toText.put(7, "seven");
		toText.put(8, "eight");
		toText.put(9, "nine");
		toText.put(0, "zero");
		ArrayList<String> textList = new ArrayList<String>();
		while (n > 0) {
			int lastDigit = n % 10;
			n /= 10;
			String asText = toText.get(lastDigit);
			textList.add(asText);
			// System.out.print(asText + " ");
		}
		System.out.println(textList);
		Collections.reverse(textList);
		System.out.println(textList);
	}

	private static void toEarthTime(String timeString) {
		// 4.27
		String[] timeParts = timeString.split("\\.");
		int gDays = Integer.parseInt(timeParts[0]);
		int gTime = Integer.parseInt(timeParts[1]);
		int year, day, month, rest;
		year = 1111 + (gDays / 365);
		rest = gDays % 365;
		month = (rest / 30) + 1 == 13 ? 12 : (rest / 30) + 1;
		day = rest % 30 == 0 ? 30 : rest % 30;
		double hour = (double) gTime / 1000.0 * 24.0;
		double minutes = (hour - Math.floor(hour)) * 60;
		String time = String.format("%02d", (int) hour) + ":"
				+ String.format("%02d", (int) minutes);
		String date = String.format("%02d", day) + "."
				+ String.format("%02d", month) + "." + year;
		System.out.println(date + ", " + time + " o'clock.");
	}

	private static void toGalacticTime(String timeString) {
		// 4.27
		// Validate input string.
		if (!timeString
				.matches("^\\d{1,2}\\.\\d{1,2}\\.\\d{4}.*\\d{1,2}\\.\\d{1,2}.*")) {
			System.out.println("Invalid input. Valid: 30.1.1984 13.08 o'clock");
			return;
		}
		// Force the input into a more managable form.
		timeString = timeString.replaceAll("(?!\\.|\\s)\\D", "");
		String[] timeParts = timeString.split(" ");
		String[] date = timeParts[0].split("\\.");
		String[] time = timeParts[1].split("\\.");
		int year = (Integer.parseInt(date[2]) - 1111) * 365;
		int month = (Integer.parseInt(date[1]) - 1) * 30;
		int day = Integer.parseInt(date[0]);
		double hour = Double.parseDouble(time[0]);
		double minute = Double.parseDouble(time[1]);
		int galacticYear = year + month + day;
		double galacticTime = (hour + (minute / 60)) * 1000.0 / 24.0;
		System.out.println(galacticYear + "." + (int) galacticTime);
	}

	private static String buildString1(String s, int multiplier) {
		return StringUtils.repeat(s, multiplier);
	}

	private static String buildString2(String s, int multiplier) {
		StringBuffer buffer = new StringBuffer(s);
		for (int i = 1; i < multiplier; i++) {
			buffer.append(s);
		}
		return buffer.toString();
	}

	private static void crossSum(int n) {
		// 4.26
		int sum = 0;
		while (n > 0) {
			int digit = n % 10;
			n /= 10;
			sum += digit;
			if (n > 0) {
				System.out.print(digit + " + ");
			} else {
				System.out.print(digit + " = ");
			}
		}
		System.out.println(sum);
	}

	private static void stars() {
		// 4.25
		Scanner in = new Scanner(System.in);
		System.out.print("Enter the number of lines to print: ");
		int lines = in.nextInt();
		String s = "*";
		for (int i = 1; i <= lines; i++) {
			// System.out.println(buildString2(s, i));
			if (i > 1)
				s += "*";
			System.out.println(s);
		}
	}

	private static void loopy() {
		for (int i = 10; i >= 0; i--) {
			System.out.println(i);
		}
		int i = 0;
		while (i < 10) {
			i++;
			if (i % 2 != 0)
				continue;
			System.out.println(i);
		}
		do {
			i--;
			System.out.println(i);
		} while (i > 0);

	}

	private static void weWereOnABreak() {
		dieda: for (int k = 0; k < 5; k++) {
			for (int i = 0; i < 5; i++) {
				System.out.println("i-Schleife i = " + i);
				if (k == 3)
					break dieda;
				else
					break;
			}
			System.out.println("k-Schleife k = " + k);
		}
		System.out.println("Done.");
		for (int i = 0; i < 100; i++) {
			if (i == 74)
				break;
			if (i % 9 != 0)
				continue;
			System.out.println(i);
		}
		int i = 0;
		while (true) {
			// infinite loop?
			i++;
			int j = i * 30;
			if (j == 1260)
				break;
			if (i % 10 != 0)
				continue;
			System.out.println(i);
		}
	}

	public static void algo() {
		// Read integer n, set int i to 3.
		// Until i < 2n:
		// Increment i by 1.
		// Print i/(2i+1)
		int n, i;
		n = 6;
		i = 3;
		while (i < 2 * n) {
			i++;
			System.out.println(1.0 / (2.0 * i + 1.0));
		}
		for (int a = 3; a < 2 * n;) {
			a += 1;
			System.out.println(1.0 / (2.0 * a + 1.0));
		}
		i = 3;
		do {
			i += 1;
			System.out.println(1.0 / (2.0 * i + 1.0));
		} while (i < 2 * n);
	}

	public static void board() {
		// 4.21
		for (int i = 0; i < 8; i++) {
			for (int a = i + 1; a < (9 + i); a++)
				System.out.print(a + " ");
			System.out.println("");
		}
	}

	public static void fixMe() {
		// 4.23
		int x = 0, y = 4;
		if (x < 5) {
			if (x < 0)
				System.out.println("x < 0");
		} else {
			System.out.println("x >= 5");
		}
		if (x > 0) {
			System.out.println("ok! x > 0");
			System.out.println("1/x = " + (1 / x));
		}
		if (y > x) {
			int temp = x;
			x = y;
			y = temp;
			System.out.println(x + " " + y);
		}
	}

	public static void max(double a, double b, double c, double d) {
		// 4.24
		double e;
		if (b > a)
			if (c > b)
				if (d > c)
					e = d;
				else
					e = c;
			else if (d > b)
				e = d;
			else
				e = b;
		else if (c > a)
			if (d > c)
				e = d;
			else
				e = c;
		else if (d > a)
			e = d;
		else
			e = a;
		System.out.println("e = " + e);
	}

	public static void maxFixed(double a, double b, double c, double d) {
		double[] anArray = { a, b, c, d };
		Arrays.sort(anArray);
		double max1 = anArray[anArray.length - 1];

		double max2 = anArray[0];
		for (double i : anArray)
			if (i > max2)
				max2 = i;
		System.out.println(max1 + " " + max2);
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
