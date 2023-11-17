# QF205 Project - Time Value of Money Calculator

## Introduction
The time value of money is a concept in which it states that a sum of money is worth more now than the same sum will be at a future date due to its earnings potential in the interim from interest rates. 

There are 5 variables used in the calculations – present value (PV) of money, the number of periods to maturity (N), interest rates (r), payment (PMT), and the future value (FV) of money. Also, we need to take note if the payment is made at the end of the period (ordinary annuity) or at the beginning of the period (annuity due), as this will affect the calculation of the time value of money. The formula is a closed-form expression, each variable (except for r) can be calculated with the inputs from the other 4 variables. 

For the calculation of r, there is no closed-form solution to the formula, hence, we will use Newton’s method, a numerical method, to calculate it.

## Using the application
Please ensure you have minimally Python 3.7 installed in your system. You may download Python from this [link](https://www.python.org/downloads/)

Next, ensure you have the PyQt5 library downloaded. You may download the library by running this command on your command prompt.
```bash
pip install PyQt5
```

To run the application, simply download the application and run the following commands:
```bash
cd <directory>

python TVM_Calculator.py
```

Enjoy using the application!

## Credits
This project was done as part of our QF205 Computing Technology for Finance module.

Team members are:
- Cheah King Yeh
- Goh Wei Han
- Jerald Lim Yinghan
- Juan Sebastian
- Wong Ginn Munn
- Yuen Kah May
