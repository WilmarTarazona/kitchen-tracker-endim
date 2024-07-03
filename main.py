import sys
import os
import platform

from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96"

widgets = None



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        if platform.system() == 'Windows':
            Settings.ENABLE_CUSTOM_TITLE_BAR = True
        else:
            Settings.ENABLE_CUSTOM_TITLE_BAR = False

        title = "ENDIM - Kitchen Tracker"
        self.setWindowTitle(title)

        UIFunctions.uiDefinitions(self)

        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        self.show()

        themeFile = "themes/py_dracula_dark.qss"

        UIFunctions.theme(self, themeFile, True)
        AppFunctions.setThemeHack(self)

        widgets.stackedWidget.setCurrentWidget(widgets.home)

    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
