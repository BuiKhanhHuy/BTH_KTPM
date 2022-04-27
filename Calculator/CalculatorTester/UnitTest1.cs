using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using Calculator;

namespace CalculatorTester
{
    [TestClass]
    public class UnitTest1
    {
        Calculation cal;

        public TestContext TestContext { set; get; }

        [TestInitialize]
        public void SetUp()
        {
            cal = new Calculation(10, 5);
        }

        [TestMethod]
        public void TestAddOperator()
        {
            int expected, actual;
            expected = 15;

            actual = cal.Execute("+");
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void TestSubOperator()
        {
            int expected, actual;
            expected = 5;

            actual = cal.Execute("-");
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void TestMulOperator()
        {
            int expected, actual;
            expected = 50;

            actual = cal.Execute("*");

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void TestDivOperator()
        {
            int expected, actual;
            expected = 2;

            actual = cal.Execute("/");

            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        [ExpectedException(typeof(DivideByZeroException))]
        public void TestDivByZero()
        {
            cal = new Calculation(10, 0);
            cal.Execute("/");
        }

        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
            @".\Data\TestData.csv", "TestData#csv",
            DataAccessMethod.Sequential)]
        [TestMethod]
        public void TestWithDataSource()
        {
            int a, b, expected, actual;

            a = int.Parse(TestContext.DataRow[0].ToString());
            b = int.Parse(TestContext.DataRow[1].ToString());
            expected = int.Parse(TestContext.DataRow[2].ToString());

            Calculation cal = new Calculation(a, b);
            actual = cal.Execute("+");

            Assert.AreEqual(expected, actual);
        }

        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
           @".\Data\TestData1.csv", "TestData1#csv",
           DataAccessMethod.Sequential)]
        [TestMethod]
        public void TestWithDataSourceNumberTwo()
        {
            int a, b, expected, actual;
            string pheptinh;

            a = int.Parse(TestContext.DataRow[0].ToString());
            b = int.Parse(TestContext.DataRow[1].ToString());
            pheptinh = TestContext.DataRow[2].ToString();
            pheptinh = pheptinh.Substring(1);
            expected = int.Parse(TestContext.DataRow[3].ToString());

            Calculation cal = new Calculation(a, b);
            actual = cal.Execute(pheptinh);

            Assert.AreEqual(expected, actual);
        }


    }
}
