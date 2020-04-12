# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'annotator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mainLayout_horizontal = QtWidgets.QHBoxLayout()
        self.mainLayout_horizontal.setObjectName("mainLayout_horizontal")
        self.ImageListWidget = QtWidgets.QVBoxLayout()
        self.ImageListWidget.setObjectName("ImageListWidget")
        self.imageListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.imageListWidget.setObjectName("imageListWidget")
        self.ImageListWidget.addWidget(self.imageListWidget)
        self.importImagesButton = QtWidgets.QPushButton(self.centralwidget)
        self.importImagesButton.setObjectName("importImagesButton")
        self.ImageListWidget.addWidget(self.importImagesButton)
        self.loadImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadImageButton.setObjectName("loadImageButton")
        self.ImageListWidget.addWidget(self.loadImageButton)
        self.removeImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeImageButton.setObjectName("removeImageButton")
        self.ImageListWidget.addWidget(self.removeImageButton)
        self.mainLayout_horizontal.addLayout(self.ImageListWidget)
        self.SlidersWidget = QtWidgets.QWidget(self.centralwidget)
        self.SlidersWidget.setObjectName("SlidersWidget")
        self.slidersLayout_horizontal = QtWidgets.QHBoxLayout(self.SlidersWidget)
        self.slidersLayout_horizontal.setObjectName("slidersLayout_horizontal")
        self.zoomLayout_vertical = QtWidgets.QVBoxLayout()
        self.zoomLayout_vertical.setObjectName("zoomLayout_vertical")
        self.zoom_label = QtWidgets.QLabel(self.SlidersWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoom_label.sizePolicy().hasHeightForWidth())
        self.zoom_label.setSizePolicy(sizePolicy)
        self.zoom_label.setObjectName("zoom_label")
        self.zoomLayout_vertical.addWidget(self.zoom_label)
        self.zoomSlider_vertical = QtWidgets.QSlider(self.SlidersWidget)
        self.zoomSlider_vertical.setOrientation(QtCore.Qt.Vertical)
        self.zoomSlider_vertical.setObjectName("zoomSlider_vertical")
        self.zoomLayout_vertical.addWidget(self.zoomSlider_vertical)
        self.slidersLayout_horizontal.addLayout(self.zoomLayout_vertical)
        self.mainLayout_horizontal.addWidget(self.SlidersWidget)
        self.GraphicWidget = QtWidgets.QVBoxLayout()
        self.GraphicWidget.setObjectName("GraphicWidget")
        self.selectionWidget = QtWidgets.QHBoxLayout()
        self.selectionWidget.setObjectName("selectionWidget")
        self.exportChoices = QtWidgets.QGroupBox(self.centralwidget)
        self.exportChoices.setObjectName("exportChoices")
        self.gridLayout = QtWidgets.QGridLayout(self.exportChoices)
        self.gridLayout.setObjectName("gridLayout")
        self.exportRegionRbutton = QtWidgets.QRadioButton(self.exportChoices)
        self.exportRegionRbutton.setObjectName("exportRegionRbutton")
        self.gridLayout.addWidget(self.exportRegionRbutton, 0, 0, 1, 1)
        self.exportColumnRbutton = QtWidgets.QRadioButton(self.exportChoices)
        self.exportColumnRbutton.setObjectName("exportColumnRbutton")
        self.gridLayout.addWidget(self.exportColumnRbutton, 1, 0, 1, 1)
        self.exportLineRbutton = QtWidgets.QRadioButton(self.exportChoices)
        self.exportLineRbutton.setObjectName("exportLineRbutton")
        self.gridLayout.addWidget(self.exportLineRbutton, 0, 1, 1, 1)
        self.exportCharRbutton = QtWidgets.QRadioButton(self.exportChoices)
        self.exportCharRbutton.setObjectName("exportCharRbutton")
        self.gridLayout.addWidget(self.exportCharRbutton, 1, 1, 1, 1)
        self.selectionWidget.addWidget(self.exportChoices)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.SelectorColorWidget = QtWidgets.QGroupBox(self.centralwidget)
        self.SelectorColorWidget.setObjectName("SelectorColorWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SelectorColorWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ColorRedBoxLayout = QtWidgets.QVBoxLayout()
        self.ColorRedBoxLayout.setObjectName("ColorRedBoxLayout")
        self.ColorRedLabel = QtWidgets.QLabel(self.SelectorColorWidget)
        self.ColorRedLabel.setObjectName("ColorRedLabel")
        self.ColorRedBoxLayout.addWidget(self.ColorRedLabel)
        self.ColorRedSBox = QtWidgets.QSpinBox(self.SelectorColorWidget)
        self.ColorRedSBox.setMaximum(255)
        self.ColorRedSBox.setObjectName("ColorRedSBox")
        self.ColorRedBoxLayout.addWidget(self.ColorRedSBox)
        self.horizontalLayout_4.addLayout(self.ColorRedBoxLayout)
        self.ColorBlueLayout = QtWidgets.QVBoxLayout()
        self.ColorBlueLayout.setObjectName("ColorBlueLayout")
        self.ColorBlueLabel = QtWidgets.QLabel(self.SelectorColorWidget)
        self.ColorBlueLabel.setObjectName("ColorBlueLabel")
        self.ColorBlueLayout.addWidget(self.ColorBlueLabel)
        self.ColorBlueSBox = QtWidgets.QSpinBox(self.SelectorColorWidget)
        self.ColorBlueSBox.setMaximum(255)
        self.ColorBlueSBox.setObjectName("ColorBlueSBox")
        self.ColorBlueLayout.addWidget(self.ColorBlueSBox)
        self.horizontalLayout_4.addLayout(self.ColorBlueLayout)
        self.ColorGreenLayout = QtWidgets.QVBoxLayout()
        self.ColorGreenLayout.setObjectName("ColorGreenLayout")
        self.ColorGreenLabel = QtWidgets.QLabel(self.SelectorColorWidget)
        self.ColorGreenLabel.setObjectName("ColorGreenLabel")
        self.ColorGreenLayout.addWidget(self.ColorGreenLabel)
        self.ColorGreenSBox = QtWidgets.QSpinBox(self.SelectorColorWidget)
        self.ColorGreenSBox.setMaximum(255)
        self.ColorGreenSBox.setObjectName("ColorGreenSBox")
        self.ColorGreenLayout.addWidget(self.ColorGreenSBox)
        self.horizontalLayout_4.addLayout(self.ColorGreenLayout)
        self.verticalLayout_2.addWidget(self.SelectorColorWidget)
        self.selectorTypes = QtWidgets.QGroupBox(self.centralwidget)
        self.selectorTypes.setObjectName("selectorTypes")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.selectorTypes)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.polygonSelectorRButton = QtWidgets.QRadioButton(self.selectorTypes)
        self.polygonSelectorRButton.setObjectName("polygonSelectorRButton")
        self.horizontalLayout.addWidget(self.polygonSelectorRButton)
        self.boxSelectorRButton = QtWidgets.QRadioButton(self.selectorTypes)
        self.boxSelectorRButton.setObjectName("boxSelectorRButton")
        self.horizontalLayout.addWidget(self.boxSelectorRButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.selectorTypes)
        self.resetSelectionButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetSelectionButton.setObjectName("resetSelectionButton")
        self.verticalLayout_2.addWidget(self.resetSelectionButton)
        self.exportImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportImageButton.setObjectName("exportImageButton")
        self.verticalLayout_2.addWidget(self.exportImageButton)
        self.selectionWidget.addLayout(self.verticalLayout_2)
        self.GraphicWidget.addLayout(self.selectionWidget)
        self.mainLayout_horizontal.addLayout(self.GraphicWidget)
        self.mainLayout_horizontal.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.mainLayout_horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.importImagesButton.setText(_translate("MainWindow", "Import Images"))
        self.loadImageButton.setText(_translate("MainWindow", "Load Image"))
        self.removeImageButton.setText(_translate("MainWindow", "Remove Image"))
        self.zoom_label.setText(_translate("MainWindow", "zoom"))
        self.exportChoices.setTitle(_translate("MainWindow", "Selection Area"))
        self.exportRegionRbutton.setText(_translate("MainWindow", "Region"))
        self.exportColumnRbutton.setText(_translate("MainWindow", "Column"))
        self.exportLineRbutton.setText(_translate("MainWindow", "Line"))
        self.exportCharRbutton.setText(_translate("MainWindow", "Character"))
        self.SelectorColorWidget.setTitle(_translate("MainWindow", "Selector Color"))
        self.ColorRedLabel.setText(_translate("MainWindow", "Red"))
        self.ColorBlueLabel.setText(_translate("MainWindow", "Blue"))
        self.ColorGreenLabel.setText(_translate("MainWindow", "Green"))
        self.selectorTypes.setTitle(_translate("MainWindow", "Selector Type"))
        self.polygonSelectorRButton.setText(_translate("MainWindow", "Polygon Selector"))
        self.boxSelectorRButton.setText(_translate("MainWindow", "Box Selector"))
        self.resetSelectionButton.setText(_translate("MainWindow", "Reset Selections"))
        self.exportImageButton.setText(_translate("MainWindow", "Export Selected Coordinates"))
