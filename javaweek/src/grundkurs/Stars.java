/**
 * Repeat "*" sequentially 1,3,5,3,1 times.
 * 
 * @author demian
 * @version 0.1
 */

package grundkurs;

public class Stars {
	/**
	 * Repeat a string.
	 * <p>
	 * Takes an integer and a string and returns the string multiplied by count.
	 * <p>
	 * And even more explanations to follow in consecutive paragraphs separated
	 * by HTML paragraph breaks.
	 * 
	 * @param str
	 *            The string to repeat.
	 * @param count
	 *            How many times to repeat the string.
	 * @return the multiplied string.
	 */
	public static String repeat(int count, String str) {
		return new String(new char[count]).replace("\0", str);
	}

	public static void main(String[] args) {
		for (int i = 1; i < 27; i += 2) {
			System.out.println(i % 8 > 5 ? repeat(i % 8 / 2, "*") : repeat(
					i % 8, "*"));
		}
	}
}
