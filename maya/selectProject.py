import os
from pathlib import Path
from PySide2 import QtWidgets, QtCore, QtGui
from maya import cmds
from util import getMayaMainWindow, getDefaultWorkspaceFile
from const import ASSETS_ROOT


class SelectProjectUI(QtWidgets.QMainWindow):
    qmwInstance = None
    
    @classmethod
    def show_UI(cls):
        if not cls.qmwInstance:
            cls.qmwInstance = UI()
        if cls.qmwInstance.isHidden():
            cls.qmwInstance.show()
        else:
            cls.qmwInstance.raise_()
            cls.qmwInstance.activateWindow()
    

    def __init__(self, parent=getMayaMainWindow()):
        super(SelectProjectUI, self).__init__(parent)
        self.setWindowTitle("Select Project")
        self.createMayaProject("Boinsk")
    

    def _resetBrowserPrefs(self):
        optionsVar = cmds.optionVar(list=True)
        for var in optionsVar:
            if var.startswith("browserLocation"):
                cmds.optionVar(remove=var)

    def createMayaProject(self, projectName):
        projectPath = Path(ASSETS_ROOT) / projectName
        subdirs = ["scenes", "images", "textures", "sourceimages", "clips", "shaders", "sound", "scripts", "data", "assets", "cache", "movies"]
        projectPath.mkdir(parents=True, exist_ok=True)

        for subdir in subdirs:
            os.makedirs(os.path.join(projectPath, subdir), exist_ok=True)
        cmds.workspace(str(projectPath), openWorkspace=True)

        workspaceMelPath = projectPath / 'workspace.mel'
        with workspaceMelPath.open('w') as file:
            file.write('//Maya 2024 Project Definition\n\n')
            file.writelines('\n'.join(getDefaultWorkspaceFile()))

        cmds.workspace(str(projectPath), openWorkspace=True)
        