using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculator
{
    public class Calculation
    {
        private int a;
        private int b;

        public Calculation(int a, int b)
        {
            this.a = a;
            this.b = b;
        }

        public int Execute(string CalSymbol)
        {
            int result = 0;
            switch (CalSymbol)
            {
                case "+":
                    result = this.a + this.b;
                    break;
                case "-":
                    result = this.a - this.b;
                    break;
                case "*":
                    result = this.a * this.b;
                    break;
                case "/":
                    result = this.a / this.b;
                    break;
            }
            return result;
        }
        public static double Power(double x, int n)
        {
            if (n == 0)
                return 1.0;
            else if (n > 0)
                return n * Power(x, n - 1);
            else
                return Power(x, n + 1) / x;
        }

    }

}
