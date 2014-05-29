package grundkurs;

public class NonPrimitives {
	public static void main(String[] args) {
		Integer a = 10, b = 20;
		System.out.println(a * b);
		createFields();
	}

	private static void createFields() {
		int[] field1 = new int[5];
		double[] field2 = new double[2];
		String[] field3 = new String[4];
		int[] field4 = { 0, 1 };
		field1[4] = 1;
		field2[0] = 3.14;
		System.out.println(field2[0]);
		field4[0] = 1;
		System.out.println(field4[0]);
	}
}
