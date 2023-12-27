import maya.cmds as cmds
from const import ASSETS_ROOT


def getCurrentProject():
    curProjectPath = cmds.workspace(query=True, fullName=True)
    if curProjectPath.startswith(ASSETS_ROOT):
        projName = curProjectPath.split(ASSETS_ROOT)[-1]
        return projName
    return None