import sys
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QFormLayout, QLineEdit, QComboBox, \
    QMessageBox
from PyQt5.QtGui import QFont, QIntValidator, QRegExpValidator, QPalette, QColor
from genetic import Genetic
from selectionType import SelectionType
from variable_configuration import VariableConfig

class MainGui(QWidget):

    def __init__(self):
        super().__init__()
        self.__title = "Genetic Algorithm"
        self.__create_ui()
        self.__form_layout = QFormLayout()
        self.__add_text()
        self.__add_inputs()
        self.__add_button1()
        self.__add_button2()
        self.__add_button3()
        self.__add_button4()
        self.__add_button5()
        self.setLayout(self.__form_layout)
        self.show()

    def __create_ui(self):
        self.setWindowTitle("Algorytm genetyczny")
        self.setGeometry(500, 100, 600, 600)
        self.setStyleSheet("background-color: darkgray;")
        #self.create_widget()

    def __add_text(self):
        main_text = QLabel()
        main_text.setText("\nAlgorytm genetyczny\n\n")
        main_text.setAlignment(Qt.AlignHCenter)
        self.__form_layout.addWidget(main_text)

    def __add_inputs(self):
        self.__add_algorithm_property_inputs()


    def __add_algorithm_property_inputs(self):
        only_int_validator = QIntValidator()
        prop_double_validator = QRegExpValidator(QRegExp("0(\\.\\d+)?|1\\.0"))
        self.__Np_input = QLineEdit()
        self.__Np_input.setPlaceholderText('Wielkosc populacji')
        self.__Np_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__Np_input)
        self.__Np_input.setStyleSheet("background-color: paleturquoise;")


        self.__n_input = QLineEdit()
        self.__n_input.setPlaceholderText('dlugosc chromosomu (bit length)')
        self.__n_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__n_input)
        self.__n_input.setStyleSheet("background-color: paleturquoise;")

        self.__D_input = QLineEdit()
        self.__D_input.setPlaceholderText('decision variables (liczba x, w przypadku naszej funkcji x1 i x2)')
        self.__D_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__D_input)
        self.__D_input.setStyleSheet("background-color: paleturquoise;")


        self.__xminfun_input = QLineEdit()
        self.__xminfun_input.setPlaceholderText('dolny przedział funkcji')
        self.__form_layout.addRow(self.__xminfun_input)
        self.__xminfun_input.setStyleSheet("background-color: paleturquoise;")

        self.__xmaxfun_input = QLineEdit()
        self.__xmaxfun_input.setPlaceholderText('gorny przedzial funkcji')
        self.__form_layout.addRow(self.__xmaxfun_input)
        self.__xmaxfun_input.setStyleSheet("background-color: paleturquoise;")

        self.__k_input = QLineEdit()
        self.__k_input.setPlaceholderText('tournament size')
        self.__k_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__k_input)
        self.__k_input.setStyleSheet("background-color: paleturquoise;")

        self.__fminormax_input = QLineEdit()
        self.__fminormax_input.setPlaceholderText('szukamy minimum -wpisz min- czy maksimum -wpisz max-')
        self.__form_layout.addRow(self.__fminormax_input)
        self.__fminormax_input.setStyleSheet("background-color: paleturquoise;")

        self.__bestpercent_input = QLineEdit()
        self.__bestpercent_input.setPlaceholderText('procent wybieranych najlepszych')
        self.__bestpercent_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__bestpercent_input)
        self.__bestpercent_input.setStyleSheet("background-color: paleturquoise;")

        self.__pc_input = QLineEdit()
        self.__pc_input.setPlaceholderText('Prawdopodobieństwo wystąpienia crossover')
        self.__pc_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__pc_input)
        self.__pc_input.setStyleSheet("background-color: paleturquoise;")

        self.__whichco_input = QLineEdit()
        self.__whichco_input.setPlaceholderText('jakie crossingover -> jedno, dwu, trzypunktoowe lub jednorodne (odpowiednio 1, 2, 3, 4)')
        self.__whichco_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__whichco_input)
        self.__whichco_input.setStyleSheet("background-color: paleturquoise;")

        self.__pm_input = QLineEdit()
        self.__pm_input.setPlaceholderText('prawdopodobienstwo wystapienia mutacji')
        self.__pm_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__pm_input)
        self.__pm_input.setStyleSheet("background-color: paleturquoise;")

        self.__whichm_input = QLineEdit()
        self.__whichm_input.setPlaceholderText('ktory rodzaj mutacji (1- brzegowa, 2- jednopunktowa 3- dwupunktowa')
        self.__whichm_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__whichm_input)
        self.__whichm_input.setStyleSheet("background-color: paleturquoise;")

        self.__pi_input = QLineEdit()
        self.__pi_input.setPlaceholderText('prawdopodobienstwo wystapienia inwersji')
        self.__pi_input.setValidator(prop_double_validator)
        self.__form_layout.addRow(self.__pi_input)
        self.__pi_input.setStyleSheet("background-color: paleturquoise;")

        self.__T_input = QLineEdit()
        self.__T_input.setPlaceholderText('Liczba epok')
        self.__T_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__T_input)
        self.__T_input.setStyleSheet("background-color: paleturquoise;")

        self.__chooseSel_input = QLineEdit()
        self.__chooseSel_input.setPlaceholderText('Wybierz metodę selekcji (1 - turniej, 2-bestsel 3-ruletka)')
        self.__chooseSel_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__chooseSel_input)
        self.__chooseSel_input.setStyleSheet("background-color: paleturquoise;")

        self.__elitStr_input = QLineEdit()
        self.__elitStr_input.setPlaceholderText('Strategia elitarna- ilość zachowanych najlepszych osobników')
        self.__elitStr_input.setValidator(only_int_validator)
        self.__form_layout.addRow(self.__elitStr_input)
        self.__elitStr_input.setStyleSheet("background-color: paleturquoise;")


    def __add_button1(self):
        self.__button = QPushButton("Start")
        self.__button.setStyleSheet("background-color: lavenderblush;")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed())
        self.__form_layout.addRow(self.__button)


    def __add_button2(self):
        self.__button = QPushButton("Wykres zależności średniej wartości funkcji od epoki")
        self.__button.setStyleSheet("background-color: lavenderblush;")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed2())
        self.__form_layout.addRow(self.__button)

    def __add_button3(self):
        self.__button = QPushButton("Wykres zależności odchylenia standardowego od epoki")
        self.__button.setStyleSheet("background-color: whitesmoke;")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed3())
        self.__form_layout.addRow(self.__button)

    def __add_button4(self):
        self.__button = QPushButton("Wykres zależności wartości funkcji od kolejnej iteracji")
        self.__button.setStyleSheet("background-color: whitesmoke;")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed4())
        self.__form_layout.addRow(self.__button)

    def __add_button5(self):
        self.__button = QPushButton("Zapisz wyniki do pliku")
        self.__button.setStyleSheet("background-color: whitesmoke;")
        self.__button.clicked.connect(lambda: self.__handle_button_pressed5())
        self.__form_layout.addRow(self.__button)
        

    def __handle_button_pressed(self):
        print("clicked")
        algorithm_config = self.__get_variable_configurations()
        self.__genetic = Genetic(algorithm_config)
        self.__print_result(self.__genetic)


    def __handle_button_pressed2(self):
        print("clicked2")
        self.__print_result2(self.__genetic)

    def __handle_button_pressed3(self):
        print("clicked3")
        self.__print_result3(self.__genetic)

    def __handle_button_pressed4(self):
        print("clicked4")
        self.__print_result4(self.__genetic)

    def __handle_button_pressed5(self):
        print("clicked5")
        self.__do_result5(self.__genetic)


    @staticmethod
    def __print_result(genetic):
        msg = QMessageBox()
        msg.setWindowTitle("Czas")
        msg.setText(f"Czas wykonywania {round(genetic.el_time, 6)} sekund\n\n")
        x = msg.exec_()

    @staticmethod
    def __print_result2(genetic):
        msg = QMessageBox()

        msg.setText(f"Srednia {(genetic.tab_mean)} \n\n")


    @staticmethod
    def __print_result3(genetic):
        msg = QMessageBox()
        msg.setText(f"Odchylenie standardowe {(genetic.tab_std)} \n\n")

    @staticmethod
    def __print_result4(genetic):
        msg = QMessageBox()
        msg.setText(f"Wartość funkcji {(genetic.tab_elitary)} \n\n")

    @staticmethod
    def __do_result5(genetic):
        genetic.fileResult()

    def __get_variable_configurations(self):
        print(int(self.__Np_input.text()))
        print(int(self.__n_input.text()))
        print(int(self.__D_input.text()))
        print(float(self.__xminfun_input.text()))
        print(float(self.__xmaxfun_input.text()))
        print(int(self.__k_input.text()))
        print(str(self.__fminormax_input.text()))
        print(int(self.__bestpercent_input.text()))
        print(float(self.__pc_input.text()))
        print(int(self.__whichco_input.text()))
        print(float(self.__pm_input.text()))
        print(int(self.__whichm_input.text()))
        print(float(self.__pi_input.text()))
        print(int(self.__T_input.text()))
        print(int(self.__chooseSel_input.text()))
        print(int(self.__elitStr_input.text()))
        return VariableConfig(
            int(self.__Np_input.text()),
            int(self.__n_input.text()),
            int(self.__D_input.text()),
            float(self.__xminfun_input.text()),
            float(self.__xmaxfun_input.text()),
            int(self.__k_input.text()),
            str(self.__fminormax_input.text()),
            int(self.__bestpercent_input.text()),
            float(self.__pc_input.text()),
            int(self.__whichco_input.text()),
            float(self.__pm_input.text()),
            int(self.__whichm_input.text()),
            float(self.__pi_input.text()),
            int(self.__T_input.text()),
            int(self.__chooseSel_input.text()),
            int(self.__elitStr_input.text()))
