package grundkurs;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class NonPrimitivesTest {

	// @BeforeClass - executed once, before starting the test suite.
	@Before
	// executed before every test.
	public void setUp() throws Exception {
	}

	// @AfterClass - executed once, when the test suite is finished.
	@After
	// executed after every test
	public void tearDown() throws Exception {
	}

	// @Ignore - Ignore the following test.
	// @Test(expected = Exception.class) - Fail if exception is not thrown.
	@Test(timeout = 100)
	// fail if execution takes >100ms
	public void multiplyTest() {
		// fail("Not yet implemented");
		// NonPrimitives tester = new NonPrimitives();
		assertEquals("10 x 20 must be 200", 200, NonPrimitives.multiply(10, 20));
	}

}
