package grundkurs;

public class Primitives {

	public static void main(String[] args) {
		System.out.println("main:");
		numbers();
		chars();
		conversion();
		bitwise();
		booleans();
		increment();
	}

	// 15 . instance access
	// 15 [] field access
	// 15 () method call
	// 14 ++,--,+,*,-,~,! unary operators
	// 13 () explicit typecasting
	// 12 *,/,% multiplicative
	// 11 +,- additive
	// 10 <<,>>,>>> shifting
	// 9 <,>,<=,>= comparison
	// 8 ==,!= equality comparison
	// 7 & AND
	// 6 ^ XOR
	// 5 | OR
	// 4 && AND (conditional)
	// 3 || OR (conditional)
	// 2 ?: ternary operator
	// 1 =,+=,-=,... assignments

	private static void increment() {
		int a = 1;
		System.out.println("increment:");
		a += 1; // Binary operator.
		a++; // Unary operator.
		System.out.println(a); // 3
		--a;
		System.out.println(a); // 2
	}

	private static void booleans() {
		boolean a = true;
		boolean b = false;
		System.out.println("booleans:");
		System.out.println(a & b); // AND
		System.out.println(a | b); // OR
		System.out.println(a ^ b); // XOR
		System.out.println(!a == b);
		System.out.println(a || b); // Only proceed to b if a not false.
		System.out.println((10 > 15) && (10 < 20)); // False
		System.out.println(16 > 15 ? "true" : "false");
	}

	private static void bitwise() {
		byte a = 9; // 00001001
		byte b = 3; // 00000011
		System.out.println("bitwise:");
		// ~ negates, << and >> shift, <<< and >>> shift-fill.
		System.out.println(a >> ~b);
		System.out.println(a & b); // AND, 00000001
		System.out.println(a | b); // OR, 00001011
		System.out.println(a ^ b); // XOR, 00001010
	}

	public static void numbers() {
		System.out.println("numbers\n");
		System.out.println(-1.78e4);
		System.out.println(0712); // Oct
		System.out.println(0x9AB); // Hex
		System.out.println((byte) 127);
		System.out.println((short) 32767);
		System.out.println((int) 2147483647);
		System.out.println((long) 9223372036854775807L);
		System.out.println((float) 1.4012984643248171E-045f); // smallest
		// positive
		// float
		System.out.println((float) 3.4028234663852886E+038f); // biggest
		// positive
		// float
		System.out.println((double) 4.9406564584124654E-324d); // smallest
		// positive
		// double
		System.out.println((double) 1.7976931348623157E+308d); // biggest
		// positive
		// double
		System.out.println(0.1 + 0.2); // rounding error
		System.out.println(1 / 10); // floor division
		System.out.println(1.0 / 10.0);
	}

	private static void conversion() {
		int i = (int) 3.14;
		float f = (float) 3;
		short s = 12345;
		System.out.println("conversion:");
		System.out.println(i + ", " + f + ", " + s);
		// IEEE-754 for double: 63 +/-, 52-62 E (Exp, 11), 0-51 M (Mantisse)
		System.out.println(f > 3 ? i : f);
		short a = 1;
		short b = 2;
		// "+" goes double > float > int. Typecast to int otherwise.
		// For Strings the operand "+" automatically converts to String.
		int c = a + b;
		short sh = (short) (a + b); // Type mismatch without (short)
		System.out.println(3 - 5.0 * 10); // double
		System.out.println(2 + 5 - 'a'); // int
		System.out.println("good" + 4 + "you"); // String
	}

	private static void chars() {
		int ord = 'n'; // ordinal number of a char.
		char chr = (char) ord; // char representation of an ordinal number.
		System.out.println("chars:");
		System.out.println(ord + " " + chr);

		int a = 'a';
		int uni = '\u07D0';
		System.out.println(a + " " + (char) a); // Unicode string.
		System.out.println(uni + " " + (char) uni); // Unicode string.
	}

}
