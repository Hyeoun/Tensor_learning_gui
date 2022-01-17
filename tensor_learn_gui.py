import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic # ui를 클래스로 바꿔준다.
import numpy as np
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import *
from tensorflow.keras.callbacks import EarlyStopping

form_window = uic.loadUiType('./learn_model_win.ui')[0]

class Exam(QMainWindow, form_window):
    def __init__(self): # 버튼 누르는 함수 처리해 주는 곳
        super().__init__()
        self.setupUi(self)
        self.btn_call_model.clicked.connect(self.Call_model)
        self.btn_target_data.clicked.connect(self.Call_data)
        self.path = ('', '')

    def Call_model(self):
        old_path = self.path
        self.path = QFileDialog.getOpenFileName(self, 'Open file', '','model Files(*.h5);;All Files(*.*)')
        if self.path != '':
            self.model = load_model(self.path[0])
            self.lbl_model_link.setText(self.path[0])
        else:
            self.path = old_path

    def Call_data(self):
        old_path = self.path
        self.path = QFileDialog.getOpenFileName(self, 'Open file', '', 'data Files(*.npy);;All Files(*.*)')
        if self.path != '':
            self.X_train, self.X_test, self.Y_train, self.Y_test = np.load(self.path[0], allow_pickle=True)
            self.lbl_target_link.setText(self.path[0])
        else:
            self.path = old_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = Exam()
    mainWindow.show()
    sys.exit(app.exec_())