import os
from pathlib import Path
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds
from util import getMayaMainWindow, getDefaultWorkspaceFile, resetBrowserPrefs
from const import ASSETS_ROOT, PROJECT_NAME


class CreateProjectUI(QtWidgets.QMainWindow):
    qmwInstance = None
    
    @classmethod
    def show_UI(cls):
        if not cls.qmwInstance:
            cls.qmwInstance = CreateProjectUI()
        if cls.qmwInstance.isHidden():
            cls.qmwInstance.show()
        else:
            cls.qmwInstance.raise_()
            cls.qmwInstance.activateWindow()
    

    def __init__(self, parent=getMayaMainWindow()):
        super(CreateProjectUI, self).__init__(parent)
        
        self.setWindowTitle(f"{PROJECT_NAME} - Create Asset")
        self.mainWidget = QtWidgets.QWidget()
        self.mainWidget.setMinimumWidth(500)
        self.setCentralWidget(self.mainWidget)
        self.layout = QtWidgets.QVBoxLayout(self.mainWidget)

        self.columnLayout = QtWidgets.QHBoxLayout()
        self.labelLayout = QtWidgets.QVBoxLayout()
        self.controlsLayout = QtWidgets.QVBoxLayout()

        #Labels
        self.categoryLabel = QtWidgets.QLabel("Existing Categories:")
        self.categoryLabel.setAlignment(QtCore.Qt.AlignRight)
        self.newCategoryLabel = QtWidgets.QLabel("New Category:")
        self.newCategoryLabel.setAlignment(QtCore.Qt.AlignRight)
        self.assetLabel = QtWidgets.QLabel("New Asset Name:")
        self.assetLabel.setAlignment(QtCore.Qt.AlignRight)
        #Controls
        self.categoryInput = QtWidgets.QLineEdit()
        self.categoryDropdown = QtWidgets.QComboBox()
        self.assetInput = QtWidgets.QLineEdit()

        self.createAssetButton = QtWidgets.QPushButton("Create Asset")
        self.createAssetButton.setEnabled(False)
        
        self.labelLayout.addWidget(self.categoryLabel)
        self.labelLayout.addWidget(self.newCategoryLabel)
        self.labelLayout.addWidget(self.assetLabel)

        self.controlsLayout.addWidget(self.categoryDropdown)
        self.controlsLayout.addWidget(self.categoryInput)
        self.controlsLayout.addWidget(self.assetInput)

        self.columnLayout.addLayout(self.labelLayout)
        self.columnLayout.addLayout(self.controlsLayout)
        self.layout.addLayout(self.columnLayout)
        self.layout.addWidget(self.createAssetButton)

        self.populateCategories()
        
        self.categoryDropdown.currentIndexChanged.connect(self.isValid)
        self.categoryInput.textChanged.connect(self.isValid)
        self.assetInput.textChanged.connect(self.isValid)
        self.createAssetButton.clicked.connect(self.createMayaProject)

    def isValid(self):
        cat = self.categoryInput.text()
        self.categoryDropdown.setEnabled(not(cat))
        category = cat if cat else self.categoryDropdown.currentText()
        assetName = self.assetInput.text()
        evl = bool(assetName and category)
        self.createAssetButton.setEnabled(evl)


    def populateCategories(self):
        assetsPath = Path(ASSETS_ROOT)
        categories = [d for d in assetsPath.iterdir() if d.is_dir()]
        for category in categories:
            self.categoryDropdown.addItem(category.name)

    def createMayaProject(self):
        try:
            cat = self.categoryInput.text()
            category = cat if cat else self.categoryDropdown.currentText()
            assetName = self.assetInput.text()

            projectPath = Path(ASSETS_ROOT) / category /  assetName
            subdirs = ["scenes", "images", "textures", "sourceimages", "clips", "shaders", "sound", "scripts", "data", "assets", "cache", "movies"]
            projectPath.mkdir(parents=True, exist_ok=True)

            for subdir in subdirs:
                os.makedirs(os.path.join(projectPath, subdir), exist_ok=True)

            workspaceMelPath = projectPath / 'workspace.mel'
            with workspaceMelPath.open('w') as file:
                file.write('//Maya 2024 Project Definition\n\n')
                file.writelines('\n'.join(getDefaultWorkspaceFile()))

            cmds.workspace(str(projectPath), openWorkspace=True)
            resetBrowserPrefs()
            cmds.inViewMessage(amg=f"Asset has been set & created:\n {category} - {assetName}", pos='midCenter', fade=True)
            self.close()
            self._clear()
        except:
            cmds.error("Failed to create new Asset")
        
    def _clear(self):
        self.assetInput.setText("")
        self.categoryInput.setText("")
        self.populateCategories()

