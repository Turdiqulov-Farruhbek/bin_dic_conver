from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton, 
    QListWidget,
    QVBoxLayout,
    QHBoxLayout
)

class Conver(QWidget):
    def __init__(self) -> None:
        super(). __init__()
        self.setWindowTitle('Binary to decimal converter')
        self.setFixedSize(500, 800)
        self.setStyleSheet("""
                        font-size: 25px;
                        background: #F0F0DF;
                        """)

        self.B_head = QLabel("Desimal to Binary converter")
        self.B_head.setFixedHeight(50)
        self.B_head.setStyleSheet("""
                        border-radius: 10px;
                        font-size: 30px;
                        background: #FFF;
                        """)
        ''' 1-bo`lim'''
        self.label_from = QLabel('From')
        self.label_to = QLabel('To')

        self.from_combo = QComboBox(self)
        self.from_combo.setFixedHeight(40)
        self.from_combo.addItem("Decimal")
        self.from_combo.addItem("Binary")
        self.from_combo.setStyleSheet("""
                        color: #000;
                        background: #fff;
                        """)
        self.to_combo = QComboBox(self)
        self.to_combo.setFixedHeight(40)
        self.to_combo.addItem("Binary")
        self.to_combo.addItem("Decimal")
        self.to_combo.setStyleSheet("""
                        color: #000;
                        background: #fff;
                        """)



        ''' 2-bo`lim'''
        self.label_enter = QLabel("Enter binary number")
        self.input_enter = QLineEdit()
        self.input_enter.setFixedHeight(50)
        self.input_enter.setStyleSheet("""
                        background: #fff;
                        """)
        self.input_enter.setPlaceholderText("Enter number...")
        self.conver_btn = QPushButton("Conver")
        self.conver_btn.setFixedSize(120, 50)
        self.conver_btn.setStyleSheet("""
                        border-radius: 5px;
                        background: #62D284;
                        """)
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setFixedSize(120, 50)
        self.reset_btn.setStyleSheet("""
                        border-radius: 5px;
                        background: #7D8A81;
                        """)
        self.swap_btn = QPushButton("Swap")
        self.swap_btn.setFixedSize(100, 50)
        self.swap_btn.setStyleSheet("""
                        border-radius: 5px;
                        background: #9F9F9F;
                        """)

        ''' 3-bo`lim'''
        self.output_4 = QLineEdit(self)
        self.output_4.setFixedHeight(90)
        self.output_4.setStyleSheet("""
                        background: #EEF2F3;
                        """)
        self.output_16 = QLineEdit(self)
        self.output_16.setFixedHeight(90)
        self.output_16.setStyleSheet("""
                        background: #EEF2F3;
                        """)


        self.v_asosiy = QVBoxLayout()
        self.h_label = QHBoxLayout()
        self.h_combo = QHBoxLayout()
        self.h_btn = QHBoxLayout()

        self.v_asosiy.addWidget(self.B_head)
        self.h_label.addWidget(self.label_from)
        self.h_label.addWidget(self.label_to)
        self.h_combo.addWidget(self.from_combo)
        self.h_combo.addWidget(self.to_combo)
        self.h_btn.addWidget(self.conver_btn)
        self.h_btn.addWidget(self.reset_btn)
        self.h_btn.addWidget(self.swap_btn)
        self.h_btn.addStretch()



        self.v_asosiy.addLayout(self.h_label)
        self.v_asosiy.addLayout(self.h_combo)
        self.v_asosiy.addStretch()
        self.v_asosiy.addWidget(self.label_enter)
        self.v_asosiy.addWidget(self.input_enter)
        self.v_asosiy.addLayout(self.h_btn)
        self.v_asosiy.addStretch()
        self.v_asosiy.addWidget(self.output_4)
        self.v_asosiy.addStretch()
        self.v_asosiy.addWidget(self.output_16)
        self.v_asosiy.addStretch()

        
        self.setLayout(self.v_asosiy)
        self.show()

        self.conver_btn.clicked.connect(self.conver)

    def conver(self):
        text = self.input_enter.text()
        f_combo = self.from_combo.currentText()
        t_combo = self.to_combo.currentText()
        self.input_enter.clear()


        if text:
            print(text, type(text))
            if f_combo == 'Decimal' and t_combo == 'Binary':
                print("hello", f_combo, t_combo)
                ikki = bin(int(text))[2:]
                self.output_4.setText(str(ikki))
            
            elif f_combo == 'Binary' and t_combo == 'Decimal':
                onlik = text
                onlik = int(onlik, 2)
                self.output_4.setText(str(onlik))


app = QApplication([])
con = Conver()
app.exec_()





        




        

