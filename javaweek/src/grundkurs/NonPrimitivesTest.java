package grundkurs;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class NonPrimitivesTest {

	@Before
	public void setUp() throws Exception {
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void multiplyTest() {
		// fail("Not yet implemented");
		// NonPrimitives tester = new NonPrimitives();
		assertEquals("10 x 20 must be 200", 200, NonPrimitives.multiply(10, 20));
	}

}
