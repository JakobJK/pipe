import os
from pathlib import Path
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds
from util import getMayaMainWindow, getDefaultWorkspaceFile, resetBrowserPrefs, setContextDisplay
from const import ASSETS_ROOT, PROJECT_NAME


class SelectProjectUI(QtWidgets.QMainWindow):
    qmwInstance = None
    @classmethod
    def show_UI(cls):
        if not cls.qmwInstance:
            cls.qmwInstance = SelectProjectUI()
        if cls.qmwInstance.isHidden():
            cls.qmwInstance.show()
        else:
            cls.qmwInstance.raise_()
            cls.qmwInstance.activateWindow()

    def showEvent(self, event):
        """
        This event is called every time the window is shown. 
        Use it to refresh the categories list.
        """
        self._clear()
        super(SelectProjectUI, self).showEvent(event)

    def __init__(self, parent=getMayaMainWindow()):
        super(SelectProjectUI, self).__init__(parent)
        self.currentCategory = ""
        self.currentAsset = ""

        self.setWindowTitle(f"{PROJECT_NAME} - Set Workspace")
        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setMinimumWidth(600)

        self.setCentralWidget(self.mainWidget)
        self.mainLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.columnsLayout = QtWidgets.QHBoxLayout(self.mainWidget)

        # Category Column
        self.categoryColumn = QtWidgets.QVBoxLayout()
        self.categoryLabel = QtWidgets.QLabel("Category")
        self.categoryList = QtWidgets.QListWidget(self)
        self.categoryColumn.addWidget(self.categoryLabel)
        self.categoryColumn.addWidget(self.categoryList)
        self.columnsLayout.addLayout(self.categoryColumn)

        # Asset Column
        self.assetColumn = QtWidgets.QVBoxLayout()
        self.assetLabel = QtWidgets.QLabel("Asset")
        self.assetList = QtWidgets.QListWidget(self)
        self.assetColumn.addWidget(self.assetLabel)
        self.assetColumn.addWidget(self.assetList)
        self.columnsLayout.addLayout(self.assetColumn)

        # Set Button
        self.setButton = QtWidgets.QPushButton("Select Asset")
        self.setButton.setEnabled(False)
        self.mainLayout.addLayout(self.columnsLayout)
        self.mainLayout.addWidget(self.setButton)

        
        self.setButton.clicked.connect(self.onSetClicked)
        self.categoryList.itemClicked.connect(self.onCategorySelected)
        self.assetList.itemClicked.connect(self.onAssetSelected)
        


    def onCategorySelected(self, item):
        self.assetList.clear()
        category = item.text()
        assets = self.getAssetsForCategory(category)
        self.currentCategory = item.text()
        self.currentAsset = ""
        self.setButton.setEnabled(False)
        self.assetList.addItems(assets)
    
    def onAssetSelected(self, item):
        self.currentAsset = item.text()
        self.setButton.setEnabled(True)
        

    def _getCategories(self):
        assetsPath = Path(ASSETS_ROOT)
        directories = [d for d in assetsPath.iterdir() if d.is_dir()]
        for directory in directories:
            self.categoryList.addItem(directory.name)

    def getAssetsForCategory(self, category):
        assetsPath = Path(ASSETS_ROOT) / category
        return [d.name for d in assetsPath.iterdir() if d.is_dir()]

    def onSetClicked(self):
        assetPath = Path(ASSETS_ROOT) / self.currentCategory / self.currentAsset
        cmds.workspace(str(assetPath), openWorkspace=True)
        resetBrowserPrefs()
        cmds.inViewMessage(amg=f"Workspace has been set:\n {self.currentCategory} - {self.currentAsset}", pos='midCenter', fade=True)
        setContextDisplay(self.currentCategory, self.currentAsset)
        self.close()
        self._clear()
    
    def _clear(self):
        self.currentCategory = ""
        self.currentAsset = ""
        self.assetList.clear()
        self.categoryList.clear()
        self._getCategories()


