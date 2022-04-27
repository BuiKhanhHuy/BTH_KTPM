using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        private Calculation cal;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void btnCong_Click(object sender, EventArgs e)
        {
            int soThuNhat, soThuHai;
            soThuNhat = int.Parse(txtSoThuNhat.Text);
            soThuHai = int.Parse(txtSoThuHai.Text);
            cal = new Calculation(soThuNhat, soThuHai);

            lblKetQua.Text = cal.Execute("+").ToString();
        }

        private void btnTru_Click(object sender, EventArgs e)
        {
            int soThuNhat, soThuHai;
            soThuNhat = int.Parse(txtSoThuNhat.Text);
            soThuHai = int.Parse(txtSoThuHai.Text);

            cal = new Calculation(soThuNhat, soThuHai);
            lblKetQua.Text = cal.Execute("-").ToString();
        }

        private void btnNhan_Click(object sender, EventArgs e)
        {
            int soThuNhat, soThuHai;
            soThuNhat = int.Parse(txtSoThuNhat.Text);
            soThuHai = int.Parse(txtSoThuHai.Text);

            cal = new Calculation(soThuNhat, soThuHai);
            lblKetQua.Text = cal.Execute("*").ToString();
        }

        private void btnChia_Click(object sender, EventArgs e)
        {
            int soThuNhat, soThuHai;
            soThuNhat = int.Parse(txtSoThuNhat.Text);
            soThuHai = int.Parse(txtSoThuHai.Text);

            cal = new Calculation(soThuNhat, soThuHai);
            lblKetQua.Text = cal.Execute("/").ToString();
        }
    }
}
