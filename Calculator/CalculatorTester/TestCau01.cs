using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;
using System.Text;
using Calculator;

namespace CalculatorTester
{
    /// <summary>
    /// Summary description for TestCau01
    /// </summary>
    [TestClass]
    public class TestCau01
    {
     
        public TestContext TestContext { get; set; }

        [TestMethod]
        [DataSource("Microsoft.VisualStudio.TestTools.DataSource.CSV",
           @".\Data\PowerTestData.csv", "PowerTestData#csv", DataAccessMethod.Sequential)]
        public void TestPower()
        {
            int n;
            double x, expected, actual;
            n = int.Parse(TestContext.DataRow[1].ToString());
            x = double.Parse(TestContext.DataRow[0].ToString());
            expected = double.Parse(TestContext.DataRow[2].ToString());
            actual = Calculation.Power(x, n);

            Assert.AreEqual(expected, actual);
        }
    }
}
