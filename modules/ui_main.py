import os
import cv2
import time
import subprocess

from . resources_rc import *
from ultralytics import YOLO

from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *

import os
import telegram
import asyncio

TOKEN = '6759448306:AAFN-MXzB4-o5xC-91_ffa0ZQJro0-xazEs'
group_chat_id = -1002057373856
video_path = 'output.mp4'

async def send(chat_id, token):
    try:
        bot = telegram.Bot(token=token)
        await bot.sendMessage(chat_id, text=msg)
        await bot.sendVideo(chat_id, video_path)
        print('message sent')
            
    except BaseException as e:
        print(e)

def generate_rtsp_url(file_path = 'datos.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            username_line = lines[0].strip().split(': ')
            password_line = lines[1].strip().split(': ')
            ip_address_line = lines[2].strip().split(': ')
            port_line = lines[3].strip().split(': ')
            channel_line = lines[4].strip().split(': ')
            stream_type_line = lines[5].strip().split(': ')
            
            username = username_line[1]
            password = password_line[1]
            ip_address = ip_address_line[1]
            port = "" if len(port_line) == 1 else port_line[-1]
            channel = channel_line[1]
            stream_type = stream_type_line[1]
            if port == "":
                rtsp_url = f"rtsp://{username}:{password}@{ip_address}/cam/realmonitor?channel={channel}&subtype={stream_type}"    
            else:
                rtsp_url = f"rtsp://{username}:{password}@{ip_address}:{port}/cam/realmonitor?channel={channel}&subtype={stream_type}"
            return rtsp_url
    except Exception as e:
        print(f"Error: {e}")
        return None

class NotificationDialog(QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowTitle("Notification")
        self.setStyleSheet("background-color: #f0f0f0;")  # Set background color
        self.setFixedWidth(300)  # Set a fixed width for the dialog

        # Message label
        message_label = QLabel(message, self)
        message_label.setAlignment(Qt.AlignCenter)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        self.setLayout(layout)

        # Set up a timer to close the dialog after 2 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close)
        self.timer.start(3000)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(940, 560))

        # Create a main container widget (styleSheet)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        
        # Create a vertical layout for the main container widget
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)

        # Create a background frame (bgApp) within the main container
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the background frame
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Create a content frame (contentBox) within the background frame
        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the content frame
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Create a top background frame (contentTopBg) within the content frame
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the top background frame
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)

        # Create a left box frame (leftBox) within the top background frame
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the left box frame
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        # Create a title label (titleRightInfo) within the left box frame
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_3.addWidget(self.titleRightInfo)

        # Add the left box and right buttons frame to the top background frame
        self.horizontalLayout.addWidget(self.leftBox)

        # Create a right buttons frame (rightButtons) within the top background frame
        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the right buttons frame
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        # Create button settingsTopBtn
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))
        # Add button to the horizontal layout of right buttons frame
        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        # Create button minimizeAppBtn within the right buttons frame
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))
        # Add button to the horizontal layout of right buttons frame
        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        # Create button maximizeRestoreAppBtn within the right buttons frame
        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))
        # Add button to the horizontal layout of right buttons frame
        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        # Create button closeAppBtn within the right buttons frame
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))
        # Add button to the horizontal layout of right buttons frame
        self.horizontalLayout_2.addWidget(self.closeAppBtn)
        
        # Add the right buttons frame to the top background frame
        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)

        # Add the top background frame to the vertical layout of content frame
        self.verticalLayout_2.addWidget(self.contentTopBg)

        # Create a bottom content frame (contentBottom) within the content frame
        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the bottom content frame
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        # Create a content frame (content) within the bottom content frame
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the content frame
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        # Create a pages container frame (pagesContainer) within the content frame
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the pages container frame
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)

        # Create a stacked widget (stackedWidget) within the pages container frame
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")

        # Create home and widgets pages within the stacked widget
        self.home = QWidget()
        self.home.setObjectName(u"home")

        self.verticalLayout_3 = QVBoxLayout(self.home)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        # Insert video
        self.video_label = QLabel()
        self.video_label.setObjectName(u"video_label")
        #
        self.video = Video()
        # self.video.start()
        self.video.ImageUpdate.connect(self.ImageUpdateSlot)
        self.video.NotificationSignal.connect(self.show_notification)
        #
        self.verticalLayout_3.addWidget(self.video_label)
        self.stackedWidget.addWidget(self.home)
        
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)

        self.stackedWidget.addWidget(self.widgets)

        # Add the stacked widget to the vertical layout of the pages container frame
        self.verticalLayout_15.addWidget(self.stackedWidget)

        # Add the pages container to the horizontal layout of the content frame
        self.horizontalLayout_4.addWidget(self.pagesContainer)

        # Create an extra right box frame (extraRightBox) within the content frame
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the extra right box frame
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        # Create a theme settings top detail frame (themeSettingsTopDetail) within the extra right box frame
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        # Add the theme settings top detail frame to the vertical layout of extra right box frame
        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        # Create a content settings frame (contentSettings) within the extra right box frame
        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the content settings frame
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        # Create a top menus frame (topMenus) within the content settings frame
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)

        # Create a vertical layout for the top menus frame
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)

        # Add an input box (QLineEdit) to the vertical layout
        self.usernameInput = QLineEdit(self.topMenus)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setPlaceholderText('Username')
        sizePolicy.setHeightForWidth(self.usernameInput.sizePolicy().hasHeightForWidth())
        self.usernameInput.setSizePolicy(sizePolicy)
        self.usernameInput.setMinimumSize(QSize(0, 45))
        self.usernameInput.setFont(font)
        self.verticalLayout_14.addWidget(self.usernameInput)

        # Add an input box (QLineEdit) to the vertical layout
        self.passwordInput = QLineEdit(self.topMenus)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setPlaceholderText('Password')
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        self.passwordInput.setMinimumSize(QSize(0, 45))
        self.passwordInput.setFont(font)
        self.verticalLayout_14.addWidget(self.passwordInput)

        # Add an input box (QLineEdit) to the vertical layout
        self.ipInput = QLineEdit(self.topMenus)
        self.ipInput.setObjectName(u"ipInput")
        self.ipInput.setPlaceholderText('IP Address')
        sizePolicy.setHeightForWidth(self.ipInput.sizePolicy().hasHeightForWidth())
        self.ipInput.setSizePolicy(sizePolicy)
        self.ipInput.setMinimumSize(QSize(0, 45))
        self.ipInput.setFont(font)
        self.verticalLayout_14.addWidget(self.ipInput)

        # Add an input box (QLineEdit) to the vertical layout
        self.portInput = QLineEdit(self.topMenus)
        self.portInput.setObjectName(u"portInput")
        self.portInput.setPlaceholderText('Port')
        sizePolicy.setHeightForWidth(self.portInput.sizePolicy().hasHeightForWidth())
        self.portInput.setSizePolicy(sizePolicy)
        self.portInput.setMinimumSize(QSize(0, 45))
        self.portInput.setFont(font)
        self.verticalLayout_14.addWidget(self.portInput)

        # Add an input box (QLineEdit) to the vertical layout
        self.channelInput = QLineEdit(self.topMenus)
        self.channelInput.setObjectName(u"channelInput")
        self.channelInput.setPlaceholderText('Channel')
        sizePolicy.setHeightForWidth(self.portInput.sizePolicy().hasHeightForWidth())
        self.channelInput.setSizePolicy(sizePolicy)
        self.channelInput.setMinimumSize(QSize(0, 45))
        self.channelInput.setFont(font)
        self.verticalLayout_14.addWidget(self.channelInput)

        # Add an input box (QLineEdit) to the vertical layout
        self.streamInput = QLineEdit(self.topMenus)
        self.streamInput.setObjectName(u"streamInput")
        self.streamInput.setPlaceholderText('Stream Type')
        sizePolicy.setHeightForWidth(self.portInput.sizePolicy().hasHeightForWidth())
        self.streamInput.setSizePolicy(sizePolicy)
        self.streamInput.setMinimumSize(QSize(0, 45))
        self.streamInput.setFont(font)
        self.verticalLayout_14.addWidget(self.streamInput)

        # Add a connect button (QPushButton) to the vertical layout
        self.btn_connect = QPushButton(self.topMenus)
        self.btn_connect.setObjectName(u"btn_connect")
        sizePolicy.setHeightForWidth(self.btn_connect.sizePolicy().hasHeightForWidth())
        self.btn_connect.setSizePolicy(sizePolicy)
        self.btn_connect.setMinimumSize(QSize(0, 45))
        self.btn_connect.setFont(font)
        self.btn_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_connect.setLayoutDirection(Qt.LeftToRight)
        self.btn_connect.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")
        self.btn_connect.clicked.connect(self.update_rtsp)

        self.verticalLayout_14.addWidget(self.btn_connect)
        
        # Add the top menus frame to the vertical layout of content settings frame
        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)

        # Add the content settings frame to the vertical layout of extra right box frame
        self.verticalLayout_7.addWidget(self.contentSettings)

        # Add the extra right box frame to the horizontal layout of the content frame
        self.horizontalLayout_4.addWidget(self.extraRightBox)

        # Add the content frame to the vertical layout of bottom content frame
        self.verticalLayout_6.addWidget(self.content)

        # Create a bottom bar frame (bottomBar) within the bottom content frame
        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)

        # Create a horizontal layout for the bottom bar frame
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        # Create a size grip frame (frame_size_grip) within the bottom bar frame
        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        # Add the size grip frame to the horizontal layout of bottom bar frame
        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        # Add the bottom bar frame to the vertical layout of bottom content frame
        self.verticalLayout_6.addWidget(self.bottomBar)

        # Add the bottom content frame to the vertical layout of content box frame
        self.verticalLayout_2.addWidget(self.contentBottom)

        # Add the content box frame to the horizontal layout of background frame
        self.appLayout.addWidget(self.contentBox)

        # Add the background frame to the vertical layout of the main container widget
        self.appMargins.addWidget(self.bgApp)

        # Set the central widget of the main window to the style sheet
        MainWindow.setCentralWidget(self.styleSheet)

        # Call the retranslateUi method to set the text for UI components
        self.retranslateUi(MainWindow)

        # Set the current index of the stacked widget
        self.stackedWidget.setCurrentIndex(2)

        # Connect slots for signals and slots mechanism
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"ENDIM APP", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))

    def ImageUpdateSlot(self, Image) -> None:
        self.video_label.setPixmap(QPixmap.fromImage(Image))
    
    def show_notification(self, message):
        notification = NotificationDialog(message)
        notification.exec_()

    def update_rtsp(self):
        if self.usernameInput.text() == "" or self.passwordInput.text() == "" or self.ipInput.text() == "" or self.portInput.text() == "" or self.channelInput.text() == "" or self.streamInput.text() == "":
            self.video.start()
        else:
            self.video.stop()
            file_content = [f"Username: {self.usernameInput.text()}\n",
                            f"Password: {self.passwordInput.text()}\n",
                            f"IP Address: {self.ipInput.text()}\n",
                            f"Port: {self.portInput.text()}\n",
                            f"Channel: {self.channelInput.text()}\n",
                            f"Stream Type: {self.streamInput.text()}"]
            # Specify the file path
            file_path = 'datos.txt'

            # Write the content to the file
            with open(file_path, 'w') as file:
                for l in file_content:
                    file.write(l)
            self.video.start()


class PoseDetector:
    def __init__(self):
        self.radius = 3
        self.color = (255, 0, 0)
        self.thickness = 2
        self.color_line = (40, 150, 208)
        self.capture_duration = 20

    def delete_video(self, output_file):
        if os.path.exists(output_file):
            os.remove(output_file)
            print(f"Video '{output_file}' deleted.")
        else:
            print(f"Video '{output_file}' not found.")

    def check_existing_video(self, output_file):
        return os.path.isfile(output_file)

    def distancia_euclidiana(self, p1, p2):
        d = ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
        return d

    def load_model(self, model_path='yolov8n-pose.pt'):
        try:
            model = YOLO(model_path)
            return model
        except Exception as e:
            print(f"Error loading YOLOv8 model: {e}")
            raise
    
class Video(QThread):
    ImageUpdate = Signal(QImage)
    NotificationSignal = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.active_thread = False

    def run(self) -> None:
        try:
            self.video = generate_rtsp_url()
            print(self.video)
        except Exception as e:
            notification = NotificationDialog(f'Error al conectar con protocolo RTSP: {e}')
            notification.exec_()
        self.active_thread = True
        cap = cv2.VideoCapture(self.video)
        pose_detector = PoseDetector()
        model = pose_detector.load_model()
        output_file = "output.mp4"
        start = False
        sending = False
        start_time2 = 0
        skip_frames = 15
        frame_count = 0

        while self.active_thread:

            success, frame = cap.read()
            if success:
                frame_count += 1
                # Skip frames
                frameWidth, frameHeight, frameRate = map(int, [cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FPS)])
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')

                if start:
                    if time.time() - start_time2 < 2.25:
                        print(time.time() - start_time2)
                        out.write(frame)
                        continue
                    else:
                        out.release()
                        start = False
                        print("final de archivo" + output_file)
                        sending = True
                
                if sending:
                    # Emit signal for notification
                    self.NotificationSignal.emit("Alerta") 
                    sending = False
                    if pose_detector.check_existing_video(output_file):
                        asyncio.run(send(group_chat_id, TOKEN))
                        pose_detector.delete_video(output_file)
                
                if frame_count % skip_frames != 0:
                    continue

                results = model(frame, conf=0.5)
                if results is None or len(results) == 0 or 'keypoints' not in results[0].__dict__:
                    print("Error: Missing or unexpected structure in results. Skipping frame.")
                    continue

                # Rest of the processing logic
                for person in results:
                    keypoints = person.keypoints.cpu().numpy()
                    if len(keypoints.xy) < 1 or len(keypoints.xy[0]) < 11:
                        print("Error: Missing or unexpected keypoints. Skipping person.")
                        continue
                    mouth = (int(keypoints.xy[0][0][0]), int(keypoints.xy[0][0][1]))
                    right_hand = (int(keypoints.xy[0][9][0]), int(keypoints.xy[0][9][1]))
                    left_hand = (int(keypoints.xy[0][10][0]), int(keypoints.xy[0][10][1]))
                    cv2.circle(frame, mouth, pose_detector.radius, pose_detector.color, pose_detector.thickness)
                    cv2.circle(frame, right_hand, pose_detector.radius, pose_detector.color, pose_detector.thickness)
                    cv2.circle(frame, left_hand, pose_detector.radius, pose_detector.color, pose_detector.thickness)
                    cv2.line(frame, mouth, right_hand, pose_detector.color_line, pose_detector.thickness)
                    cv2.line(frame, mouth, left_hand, pose_detector.color_line, pose_detector.thickness)
                    cv2.putText(frame, f"Distancia(Mano Derecha):{pose_detector.distancia_euclidiana(mouth, right_hand):.2f}", (600, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)
                    cv2.putText(frame, f"Distancia(Mano Izquierda):{pose_detector.distancia_euclidiana(mouth, left_hand):.2f}", (1200, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2, cv2.LINE_AA)

                    if start == False:
                        if int(pose_detector.distancia_euclidiana(mouth, right_hand)) < 37 or int(pose_detector.distancia_euclidiana(mouth, left_hand)) < 37:
                            if pose_detector.check_existing_video(output_file):
                                pose_detector.delete_video(output_file)
                            start = True
                            out = cv2.VideoWriter(output_file, fourcc, frameRate, (frameWidth, frameHeight))
                            start_time2 = time.time()

                annotated_frame = results[0].plot()
                Image = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB) if annotated_frame is not None else frame
                ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(1015, 1015, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)
            else:
                break

        cap.release()
        self.stop()
        print("finished video")

    def stop(self) -> None:
        self.active_thread = False
        self.quit()
