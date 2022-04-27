using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using Calculator;

namespace CalculatorTester
{

    [TestClass]
    public class TestCau03
    {
        public TestContext TestContext { set; get; }

        [TestMethod]
        public void TestCorrectValue()
        {
            int number;
            Radix radix;
            number = 10;
            radix = new Radix(number);
        }

        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void TestIncorrectValue()
        {
            int number;
            Radix radix;
            number = -1;
            radix = new Radix(number);
        }

        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
            @".\Data\TestDataCau03Radix.csv", "TestDataCau03Radix#csv", DataAccessMethod.Sequential)]
        [ExpectedException(typeof(ArgumentException))]
        public void TestExceptionRadix()
        {
            int number, radix;
            Radix r;

            number = int.Parse(TestContext.DataRow[0].ToString());
            radix = int.Parse(TestContext.DataRow[1].ToString());

            r = new Radix(number);
            r.ConvertDecimalToAnother(radix);
        }

        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
            @".\Data\TestDataCau03Convert.csv", "TestDataCau03Convert#csv", DataAccessMethod.Sequential)]
        public void TestConvertDecimalToAnother()
        {
            int number, radix;
            string expected = "", actual = "";
            Radix r;

            number = int.Parse(TestContext.DataRow[0].ToString());
            radix = int.Parse(TestContext.DataRow[1].ToString());
            expected = TestContext.DataRow[2].ToString();

            r = new Radix(number);

            actual = r.ConvertDecimalToAnother(radix);

            Assert.AreEqual(expected, actual);

        }
    }
}
