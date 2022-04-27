using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using Calculator;

namespace CalculatorTester
{
    [TestClass]
    public class TestCau02
    {
        public TestContext TestContext { get; set; }

        // test du lieu khoi tao khong chinh xac 
        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void TestInvalidData()
        {
            int n;
            List<int> a;

            n = 3;
            a = new List<int>() { 1, 2, 3 };

            Polynomial polynomial = new Polynomial(n, a);
        }

        // test du lieu khoi tao nhap chinh xac
        [TestMethod]
        public void TestValidData()
        {
            int n;
            List<int> a;

            n = 3;
            a = new List<int>() { 1, 2, 3, 4 };

            Polynomial polynomial = new Polynomial(n, a);
        }


        // test cal
        [TestMethod]
        public void TestCal()
        {
            int n, x, actual, expected;
            List<int> a;
            Polynomial polynomial;

            n = 3;
            x = 1;
            a = new List<int>() { 1, 2, 3, 4 };
            polynomial = new Polynomial(n, a);
            expected = 10;

            actual = polynomial.Cal(x);

            Assert.AreEqual(expected, actual);
        }

        // test cal voi data
        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
            @".\Data\TestDataCau2.csv", "TestDataCau2#csv", DataAccessMethod.Sequential)]
        public void TestCalWithDataSource()
        {
            int n, a, b, c, d, x, actual, expected;
            List<int> arr;
            Polynomial polynomial;

            n = int.Parse(TestContext.DataRow[0].ToString());
            a = int.Parse(TestContext.DataRow[1].ToString());
            b = int.Parse(TestContext.DataRow[2].ToString());
            c = int.Parse(TestContext.DataRow[3].ToString()); 
            d = int.Parse(TestContext.DataRow[4].ToString());
            x = int.Parse(TestContext.DataRow[5].ToString());
            expected = int.Parse(TestContext.DataRow[6].ToString());

            arr = new List<int>() { a, b, c, d };
            polynomial = new Polynomial(n, arr);

            actual = polynomial.Cal(x);

            Assert.AreEqual(expected, actual);
        }
    }
}
