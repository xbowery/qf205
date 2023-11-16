import sys
from PyQt5.QtWidgets import (
   QApplication,
   QWidget,
   QVBoxLayout,
   QFormLayout,
   QLineEdit,
   QLabel,
   QPushButton,
   QComboBox,
   QGridLayout,
)
from PyQt5.QtCore import Qt
import math


class TVMCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TVM Calculator')
        self.setGeometry(0, 0, 700, 500)
        self.setStyleSheet("background-color: #8fd3fe;")

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 10, 20, 10)

        title_label = QLabel(
            "Welcome to the TVM Calculator!\n"
            "Enter the relevant values and choose what to calculate using the dropdown menu.\n"
            "Click 'Calculate' to get the result or 'Reset' to clear the inputs.\n\n"
            "Instructions")

        instructions_label = QLabel(
            "1. Enter the number of years (N), interest rate (r), present value (PV),\n"
            "   payment per period (PMT), and future value (FV).\n"
            "2. Choose what to calculate using the dropdown menu:\n"
            "   - N: Number of years\n"
            "   - r: Interest rate\n"
            "   - PV: Present value\n"
            "   - PMT: Payment per period\n"
            "   - FV: Future value\n"
            "3. Select the type of annuity (Annuity Due or Ordinary Annuity).\n"
            "4. Click 'Calculate' to see the result.\n"
            "5. Use 'Reset' to clear all fields and start a new calculation.\n\n"
            "Note: Ensure you have valid input values before clicking 'Calculate'.\n"
            "Annuity Due means payments at the beginning of each period.")

        # Center-align the text
        title_label.setAlignment(Qt.AlignCenter)  
        title_label_style = "color:black; font-family: Times New Roman; font-size: 22px"
        title_label.setStyleSheet(title_label_style)

        instructions_label.setAlignment(Qt.AlignLeft)  # Center-align the text
        instructions_label_style = "color:black; font-family: Times New Roman; font-size: 20px"
        instructions_label.setStyleSheet(instructions_label_style)

        layout.addWidget(title_label)
        layout.addWidget(instructions_label)

        form_layout = QFormLayout()
        form_layout.setContentsMargins(20, 20, 20, 10)
        form_layout.setSpacing(10)

        self.n_input = QLineEdit()
        self.n_input.setPlaceholderText('No. of years e.g., 5')
        self.r_input = QLineEdit()
        self.r_input.setPlaceholderText('Interest Rate e.g., 10')
        self.pv_input = QLineEdit()
        self.pv_input.setPlaceholderText('Present Value e.g., 1000')
        self.pmt_input = QLineEdit()
        self.pmt_input.setPlaceholderText('Payment per period e.g., 50')
        self.fv_input = QLineEdit()
        self.fv_input.setPlaceholderText('Future Value e.g., 1500')

        # Set styles for input fields
        input_style = "background-color: white; border: 1px solid #d0d0d0;\
                    padding: 5px; font-family: Times New Roman; font-size: 18px;"

        self.n_input.setStyleSheet(input_style)
        self.r_input.setStyleSheet(input_style)
        self.pv_input.setStyleSheet(input_style)
        self.pmt_input.setStyleSheet(input_style)
        self.fv_input.setStyleSheet(input_style)

        # Labels style
        label_style = "color: black; font-family: Times New Roman; font-size: 20px;"

        # input boxes and labels
        form_layout.addRow(QLabel('N (Years):', styleSheet=label_style), self.n_input)
        form_layout.addRow(QLabel('r (%):', styleSheet=label_style), self.r_input)
        form_layout.addRow(QLabel('PV ($):', styleSheet=label_style), self.pv_input)
        form_layout.addRow(QLabel('PMT ($):', styleSheet=label_style), self.pmt_input)
        form_layout.addRow(QLabel('FV ($):', styleSheet=label_style), self.fv_input)

        # calculate button
        calculate_button = QPushButton('Calculate')
        calculate_button.clicked.connect(self.calculate)
        button_style = "background-color: white; color:black; font-family: Times New Roman; font-size: 20px"
        calculate_button.setStyleSheet(button_style)

        # reset button
        reset_button = QPushButton('Reset')
        reset_button.clicked.connect(self.reset)
        reset_button.setStyleSheet(button_style)

        # Adjusted layout using QGridLayout
        button_layout = QGridLayout()
        button_layout.setContentsMargins(20, 10, 20, 10)
        button_layout.addWidget(reset_button, 0, 0, 1, 1)
        button_layout.addWidget(calculate_button, 0, 1, 1, 1)

        # what to calculate dropdown
        dropdown_layout = QVBoxLayout()
        dropdown_layout.setContentsMargins(20, 10, 20, 10)
        dropdown_layout.setSpacing(10)

        combobox_style = "QComboBox { background-color: white; border: 1px solid #d0d0d0; \
                 font-family: Times New Roman; padding: 5px 0 5px 5px; font-size: 20px; } \
                 QComboBox QAbstractItemView { border: 1px solid #d0d0d0; background-color: white; padding: 0; } \
                 QComboBox::down-arrow { padding-left: 0; }"

        self.calculate_dropdown = QComboBox()
        self.calculate_dropdown.addItems(['N', 'r', 'PV', 'PMT', 'FV'])
        self.calculate_dropdown.setCurrentText('PV')
        self.calculate_dropdown.setStyleSheet(combobox_style)
        dropdown_layout.addWidget(QLabel('Choose what to calculate:', styleSheet=label_style))
        dropdown_layout.addWidget(self.calculate_dropdown)

        # Dropdown to choose ORDINARY ANNUITY or ANNUITY DUE
        self.end_dropdown = QComboBox()
        self.end_dropdown.addItems(['Annuity Due', 'Ordinary Annuity'])
        self.end_dropdown.setCurrentText('Ordinary Annuity')
        self.end_dropdown.setStyleSheet(combobox_style)
        dropdown_layout.addWidget(QLabel('Choose Annuity Due or Ordinary Annuity:', styleSheet=label_style))
        dropdown_layout.addWidget(self.end_dropdown)

        # widget to display calulcated result
        self.result_label = QLabel()
        result_label_style = "padding-left: 20px; font-family: Times New Roman; font-size: 20px"

        self.result_label.setStyleSheet(result_label_style)

        layout.addLayout(form_layout)
        layout.addLayout(dropdown_layout)
        layout.addLayout(button_layout) 
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self):
        N = float(self.n_input.text()) if self.n_input.text() else 0
        r = float(self.r_input.text()) / 100 if self.r_input.text() else 0
        PV = float(self.pv_input.text()) if self.pv_input.text() else 0
        PMT = float(self.pmt_input.text()) if self.pmt_input.text() else 0
        FV = float(self.fv_input.text()) if self.fv_input.text() else 0
        to_calculate = self.calculate_dropdown.currentText()

        # For simplicity, we used the boolean 'END' to represent the calculation for ordinary annuity
        END = self.end_dropdown.currentText() == 'Ordinary Annuity'

        if END == True:
            calc = Calculation(N, r, PV, PMT, FV)
        elif END == False:
            calc = Calculation(N, r, PV, PMT, FV, END)

        if to_calculate == "N":
            result = calc.calculate_N()
        elif to_calculate == "r":
            result = calc.calculate_r()
        elif to_calculate == "PV":
            result = calc.calculate_PV()
        elif to_calculate == "PMT":
            result = calc.calculate_PMT()
        elif to_calculate == "FV":
            result = calc.calculate_FV()

        if type(result) == float:
            result = round(result, 2)
            self.result_label.setText('Result: ' + str(result))  # Display the result in the label
        else:
            self.result_label.setText('Result: ' + str(result))

    def reset(self):
        self.n_input.setText(self.n_input.setPlaceholderText('No. of years e.g., 5'))
        self.r_input.setText(self.r_input.setPlaceholderText('Interest Rate e.g., 10'))
        self.pv_input.setText(self.pv_input.setPlaceholderText('Present Value e.g., 1000'))
        self.pmt_input.setText(self.pmt_input.setPlaceholderText('Payment per period e.g., 50'))
        self.fv_input.setText(self.fv_input.setPlaceholderText('Future Value e.g., 1500'))
        self.calculate_dropdown.setCurrentText('PV')
        self.end_dropdown.setCurrentText('Ordinary Annuity')
        self.result_label.setText("")


class Calculation:
    def __init__(self, N, r, PV, PMT, FV, END=True):
        self.N = N
        self.r = r
        self.PV = PV
        self.PMT = PMT
        self.FV = FV
        self.END = END

    def calculate_N(self): #all calcs checked
        PV = self.PV
        FV = self.FV
        r = self.r
        PMT = self.PMT
        END = self.END

        try:
            if PV == FV:
                return "Invalid. When calulcating N, PV cannot be equal to FV"
            elif r == 0:
                return -(PV - FV) / PMT
            elif PMT == 0:
                return (math.log(abs(FV / PV))) / math.log(1 + r)
            elif PV == 0:
                # Annuity DUE
                if not END:
                    return math.log(1 + (FV * r) / (PMT * (1 + r))) / math.log(1 + r)

                # Ordinary Annuity
                return math.log(1 + (FV * r) / PMT) / math.log(1 + r)
            elif FV == 0:
                # Annuity DUE
                if not END:
                    gi = 1 + r
                    return math.log(((PMT * gi) - FV) / ((PMT * gi) + (PV * r))) / math.log(1 + r)

                # Ordinary Annuity
                return math.log(PMT / (PMT + (PV * r))) / math.log(1+r)
            else:
                gi = 1 + r
                if END:
                    gi = 1
                return math.log((FV / gi + PMT / r) / (PV / gi + PMT / r)) / math.log(1 + r)

        except Exception as e:
            return e

    def calculate_r(self):
        PV = self.PV
        FV = self.FV
        N = self.N
        PMT = self.PMT
        END = self.END

        try:
            if N == 0:
                return 'Invalid. When calculating r, N cannot be 0' #return ERROR 1 on calc
            elif PMT == 0:
                return ((FV / PV) ** (1 / N) - 1) * 100
            elif PV == 0:
                return 'Invalid. When calculating r, PV cannot be 0'
            elif FV == 0:
                return 'Invalid. When calculating r, FV cannot be 0'
            else:
                return self.cal_rate_all() * 100

        except Exception as e:
            return e

    def calculate_PV(self): #all calcs checked
        N = self.N
        FV = self.FV
        r = self.r
        PMT = self.PMT
        END = self.END
   
        try:
            if N == 0:
                return FV
            elif r == 0:
                return FV - N * PMT
            elif PMT == 0:
                return FV / (1 + r) ** N
            else:
                if not END:
                    return ((FV / ((1 + r) ** (N + 1)) - PMT / r * (1 - 1 / (1 + r) ** N))) * (1 + r)
                return FV / (1 + r) ** N - (PMT / r) * (1 - 1 / (1 + r) ** N)

        except Exception as e:
            return e

    def calculate_PMT(self): #all calcs checked
        N = self.N
        FV = self.FV
        r = self.r
        PV = self.PV
        END = self.END

        try:
            if N == 0:
                return 'Invalid. When calculating PV, N cannot be 0' #return ERROR 1 on calc
            elif r == 0:
                return (FV - PV) / N
            elif PV == 0:
                if not END:
                    return (FV * r) / ((1 + r) * ((1 + r) ** N - 1))
                return (FV * r) / ((1 + r) ** N - 1)
            else:
                if not END:
                    return (r * (FV / ((1 + r) ** (N + 1)) - PV / (1 + r))) / (1 - 1 / (1 + r) ** N)
                return (r * (FV - PV * (1 + r) ** N)) / ((1 + r) ** N - 1)

        except Exception as e:
            return e

    def calculate_FV(self): #all calcs checked
        N = self.N
        PV = self.PV
        r = self.r
        PMT = self.PMT
        END = self.END

        try:
            if N == 0:
                return PV
            elif r == 0:
                return PV + N * PMT
            elif PMT == 0:
                return PV  * (1 + r) ** N
            elif PV == 0:
                if not END:
                    return (PMT * ((1 + r) ** N - 1) / r) * (1 + r)
                return PMT * ((1 + r) ** N - 1) / r
            else:
                if not END:
                    return (((PV / (1 + r)) * (1 + r) ** N) + PMT * (((1 + r) ** N - 1) / r)) * (1 + r)
                return (PV * (1 + r) ** N) + PMT * (((1 + r) ** N - 1) / r)

        except Exception as e:
            return e

    def cal_rate_all(self):
        N = self.N
        FV = self.FV * -1
        PMT = self.PMT
        PV = self.PV
        END = self.END

        iteration_max = 1000
        iteration = 0
        adjustment = 0.5
        solver = 0
        sum_all = 0
        find_the_answer = False
        inverse = False

        if PV > 0 and FV < 0:
            inverse = True
        elif PV > 0 and FV > 0:
            print('Either PV or FV should be negative')
            return
        elif PV < 0 and FV < 0:
            print('Either PV or FV should be positive')
            return

        if END:
            while iteration < iteration_max:
                sum_all = 0
                rate = solver + 1

                for i in range(1, int(N) + 1):
                    sum_all += PMT / rate**i

                sum_all += PV
                sum_all += FV / rate ** N

                if abs(sum_all) < 0.000001:
                    find_the_answer = True
                    break
                elif sum_all > 0:
                    if not inverse:
                        solver += adjustment
                    else:
                        solver -= adjustment
                else:
                    if not inverse:
                        solver -= adjustment
                    else:
                        solver += adjustment
                adjustment /= 1.5
                iteration += 1
        else:
            while iteration < iteration_max:
                sum_all = 0
                rate = solver + 1

                for i in range(0, int(N)):
                    sum_all += PMT / rate**i

                sum_all += PV
                sum_all += FV / rate ** N

                if abs(sum_all) < 0.000001:
                    find_the_answer = True
                    break
                elif sum_all > 0:
                    if not inverse:
                        solver += adjustment
                    else:
                        solver -= adjustment
                else:
                    if not inverse:
                        solver -= adjustment
                    else:
                        solver += adjustment
                adjustment /= 1.5
                iteration += 1

        if find_the_answer:
            rate = rate - 1
            rate *= 100000
            rate = round(rate)
            rate /= 100000
            return rate
        else:
            return 'Unable to find I/Y!'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = TVMCalculator()
    calculator.show()
    sys.exit(app.exec_())
