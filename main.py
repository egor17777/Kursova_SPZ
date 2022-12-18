import wmi
import os
os.popen('OHD\\OpenHardwareMonitor.exe', 'w')


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(477, 329)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 481, 241))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 211))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 481, 181))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, item)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 481, 181))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, item)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_4 = QtWidgets.QWidget()

        self.tab_4.setObjectName("tab_4")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 0, 481, 181))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setItem(3, 2, item)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(0, 0, 491, 211))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(3, 2, item)
        self.tableWidget_4.verticalHeader().setCascadingSectionResizes(False)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_5.setGeometry(QtCore.QRect(0, 0, 481, 181))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setItem(2, 1, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(0, 220, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.refresh.setFont(font)
        self.refresh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.refresh.setAutoFillBackground(False)
        self.refresh.setObjectName("refresh")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 477, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU Core #1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPU Core #2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPU Core #3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CPU Core #4"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("MainWindow", "C_V_1"))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("MainWindow", "C_MAX_1"))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("MainWindow", "C_MIN_1"))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("MainWindow", "C_V_2"))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("MainWindow", "C_MAX_2"))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("MainWindow", "C_MIN_2"))
        item = self.tableWidget_2.item(2, 0)
        item.setText(_translate("MainWindow", "C_V_3"))
        item = self.tableWidget_2.item(2, 1)
        item.setText(_translate("MainWindow", "C_MAX_3"))
        item = self.tableWidget_2.item(2, 2)
        item.setText(_translate("MainWindow", "C_MIN_3"))
        item = self.tableWidget_2.item(3, 0)
        item.setText(_translate("MainWindow", "C_V_4"))
        item = self.tableWidget_2.item(3, 1)
        item.setText(_translate("MainWindow", "C_MAX_4"))
        item = self.tableWidget_2.item(3, 2)
        item.setText(_translate("MainWindow", "C_MIN_4"))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Temperatures"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU Core #1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPU Core #2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPU Core #3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CPU Core #4"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Load"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "CPU Package"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPU Cores"))
        item = self.tableWidget_6.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "CPU Graphics"))
        item = self.tableWidget_6.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "CPU DRAM"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min"))
        __sortingEnabled = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)
        self.tableWidget_6.setSortingEnabled(__sortingEnabled)
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Powers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "CPU"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Load Core"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Load Memory"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Power"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Min"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "GPU"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Generic Memory"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "SDD Memory"))
        item = self.tableWidget_5.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "HDD Memory"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Value"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Max"))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)
        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Memory"))
        self.refresh.setText(_translate("MainWindow", "Update sensor data"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.action_3.setText(_translate("MainWindow", "Закрити"))
        self.action_4.setText(_translate("MainWindow", "Закрити"))

    def add_func(self):
        self.refresh.clicked.connect(lambda: self.refresh_data())
        self.cpu_temps_max = [0, 0, 0, 0]
        self.cpu_temps_min = [100, 100, 100, 100]
        self.cpu_loads_max = [0, 0, 0, 0]
        self.cpu_loads_min = [100, 100, 100, 100]
        self.cpu_powers_max = [0, 0, 0, 0]
        self.cpu_powers_min = [100, 100, 100, 100]
        self.gpu_info_max = [0, 0, 0, 0]
        self.gpu_info_min = [100, 100, 100, 100]
        self.memory_info_max = [0, 0, 0]

    def refresh_data(self):
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        sensors = w.Sensor()

        cpu_temps = []
        cpu_loads = []
        cpu_powers = []

        gpu_temp = 0
        gpu_load_core = 0
        gpu_load_memory = 0
        gpu_power = 0

        load_memory = 0
        load_used_space = []
        for sensor in sensors:
            if sensor.SensorType == u'Temperature' and 'GPU' in sensor.Name:
                gpu_temp += round(float(sensor.Value), 1)
            if sensor.SensorType == u'Load' and 'GPU Core' in sensor.Name:
                gpu_load_core += round(float(sensor.Value), 1)
            if sensor.SensorType == u'Load' and 'GPU Memory' in sensor.Name:
                gpu_load_memory += round(float(sensor.Value), 1)
            if sensor.SensorType == u'Power' and 'GPU Power' in sensor.Name:
                gpu_power += round(float(sensor.Value), 1)
            if sensor.SensorType == u'Power' and f"CPU" in sensor.Name:
                cpu_powers += [round(float(sensor.Value), 1)]
            if sensor.SensorType == u'Load' and sensor.Name == f"Memory":
                load_memory += round(float(sensor.Value), 1)
            if sensor.SensorType == u'Load' and f"Used Space" in sensor.Name:
                load_used_space += [round(float(sensor.Value), 1)]
            if sensor.SensorType == u'Load' and 'CPU Core #' in sensor.Name:
                cpu_loads += [round(float(sensor.Value), 1)]
            elif sensor.SensorType == u'Temperature' and not 'GPU' in sensor.Name:
                cpu_temps += [float(sensor.Value)]
        gpu_info = [gpu_temp, gpu_load_core, gpu_load_memory, gpu_power]
        memory_info = [load_memory, load_used_space[0], load_used_space[1]]
        cpu_temps.pop(3)

        for i in range(4):
            if cpu_temps[i] >= self.cpu_temps_max[i]:
                self.cpu_temps_max[i] = cpu_temps[i]
            if cpu_temps[i] <= self.cpu_temps_min[i]:
                self.cpu_temps_min[i] = cpu_temps[i]
            if cpu_loads[i] >= self.cpu_loads_max[i]:
                self.cpu_loads_max[i] = cpu_loads[i]
            if cpu_loads[i] <= self.cpu_loads_min[i]:
                self.cpu_loads_min[i] = cpu_loads[i]
            if cpu_powers[i] >= self.cpu_powers_max[i]:
                self.cpu_powers_max[i] = cpu_powers[i]
            if cpu_powers[i] <= self.cpu_powers_min[i]:
                self.cpu_powers_min[i] = cpu_powers[i]
            if gpu_info[i] >= self.gpu_info_max[i]:
                self.gpu_info_max[i] = gpu_info[i]
            if gpu_info[i] <= self.gpu_info_min[i]:
                self.gpu_info_min[i] = gpu_info[i]

        for i in range(3):
            if memory_info[i] >= self.memory_info_max[i]:
                self.memory_info_max[i] = memory_info[i]

        for i in range(3):
            self.tableWidget_5.item(i, 0).setText(str(memory_info[i]) + " %")
            self.tableWidget_5.item(i, 1).setText(str(self.memory_info_max[i]) + " %")

        for i in range(4):
            self.tableWidget_2.item(i, 0).setText(str(cpu_temps[i]) + " C")
            self.tableWidget_2.item(i, 1).setText(str(self.cpu_temps_max[i]) + " C")
            self.tableWidget_2.item(i, 2).setText(str(self.cpu_temps_min[i]) + " C")
            self.tableWidget_3.item(i, 0).setText(str(cpu_loads[i]) + " %")
            self.tableWidget_3.item(i, 1).setText(str(self.cpu_loads_max[i]) + " %")
            self.tableWidget_3.item(i, 2).setText(str(self.cpu_loads_min[i]) + " %")
            self.tableWidget_6.item(i, 0).setText(str(cpu_powers[i]) + " W")
            self.tableWidget_6.item(i, 1).setText(str(self.cpu_powers_max[i]) + " W")
            self.tableWidget_6.item(i, 2).setText(str(self.cpu_powers_min[i]) + " W")

        self.tableWidget_4.item(0, 0).setText(str(gpu_info[0]) + " C")
        self.tableWidget_4.item(1, 0).setText(str(gpu_info[1]) + " %")
        self.tableWidget_4.item(2, 0).setText(str(gpu_info[2]) + " %")
        self.tableWidget_4.item(3, 0).setText(str(gpu_info[3]) + " W")
        self.tableWidget_4.item(0, 1).setText(str(self.gpu_info_max[0]) + " C")
        self.tableWidget_4.item(1, 1).setText(str(self.gpu_info_max[1]) + " %")
        self.tableWidget_4.item(2, 1).setText(str(self.gpu_info_max[2]) + " %")
        self.tableWidget_4.item(3, 1).setText(str(self.gpu_info_max[3]) + " W")
        self.tableWidget_4.item(0, 2).setText(str(self.gpu_info_min[0]) + " C")
        self.tableWidget_4.item(1, 2).setText(str(self.gpu_info_min[1]) + " %")
        self.tableWidget_4.item(2, 2).setText(str(self.gpu_info_min[2]) + " %")
        self.tableWidget_4.item(3, 2).setText(str(self.gpu_info_min[3]) + " W")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
