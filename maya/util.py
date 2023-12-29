from shiboken2 import wrapInstance
from PySide2 import QtWidgets
import maya.OpenMayaUI as omui
import maya.cmds as cmds
from const import ASSETS_ROOT, PROJECT_NAME

def setContextDisplay(category, asset):
    "WIP - This needs color n' spice and everything nice."
    menuName = f"{PROJECT_NAME}Context"
    prefix = f"[ {PROJECT_NAME} - "
    suffix = " ]"
    if cmds.menu(menuName, exists=True):
        cmds.deleteUI(menuName)
    contextMenu = cmds.menu(menuName, enable=True, label=f"{prefix}{category} - {asset}{suffix}", parent="MayaWindow")


def getCurrentProject():
    curProjectPath = cmds.workspace(query=True, fullName=True)
    if curProjectPath.startswith(ASSETS_ROOT):
        projName = curProjectPath.split(ASSETS_ROOT)[-1]
        result = projName.split('/')
        if len(result) > 2:
            return None
        return result
    return None

def resetBrowserPrefs():
    optionsVar = cmds.optionVar(list=True)
    for var in optionsVar:
        if var.startswith("browserLocation"):
            cmds.optionVar(remove=var)

def getMayaMainWindow():
    mainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mainWindowPtr), QtWidgets.QWidget)
    return mayaMainWindow


def getDefaultWorkspaceFile():
    return [
    'workspace -fr "fluidCache" "cache/nCache/fluid";',
    'workspace -fr "JT_ATF" "data";',
    'workspace -fr "images" "images";',
    'workspace -fr "offlineEdit" "scenes/edits";',
    'workspace -fr "STEP_ATF Export" "data";',
    'workspace -fr "furShadowMap" "renderData/fur/furShadowMap";',
    'workspace -fr "SVG" "data";',
    'workspace -fr "scripts" "scripts";',
    'workspace -fr "DAE_FBX" "data";',
    'workspace -fr "shaders" "renderData/shaders";',
    'workspace -fr "NX_ATF" "data";',
    'workspace -fr "furFiles" "renderData/fur/furFiles";',
    'workspace -fr "CATIAV5_ATF Export" "data";',
    'workspace -fr "OBJ" "data";',
    'workspace -fr "PARASOLID_ATF Export" "data";',
    'workspace -fr "FBX export" "data";',
    'workspace -fr "furEqualMap" "renderData/fur/furEqualMap";',
    'workspace -fr "DAE_FBX export" "data";',
    'workspace -fr "CATIAV5_ATF" "data";',
    'workspace -fr "SAT_ATF Export" "data";',
    'workspace -fr "movie" "movies";',
    'workspace -fr "ASS Export" "data";',
    'workspace -fr "move" "data";',
    'workspace -fr "mayaAscii" "scenes";',
    'workspace -fr "autoSave" "autosave";',
    'workspace -fr "NX_ATF Export" "data";',
    'workspace -fr "sound" "sound";',
    'workspace -fr "mayaBinary" "scenes";',
    'workspace -fr "timeEditor" "Time Editor";',
    'workspace -fr "DWG_ATF" "data";',
    'workspace -fr "Arnold-USD" "data";',
    'workspace -fr "JT_ATF Export" "data";',
    'workspace -fr "iprImages" "renderData/iprImages";',
    'workspace -fr "FBX" "data";',
    'workspace -fr "renderData" "renderData";',
    'workspace -fr "CATIAV4_ATF" "data";',
    'workspace -fr "fileCache" "cache/nCache";',
    'workspace -fr "eps" "data";',
    'workspace -fr "3dPaintTextures" "sourceimages/3dPaintTextures";',
    'workspace -fr "mel" "scripts";',
    'workspace -fr "translatorData" "data";',
    'workspace -fr "DXF_ATF Export" "data";',
    'workspace -fr "particles" "cache/particles";',
    'workspace -fr "DXF_ATF" "data";',
    'workspace -fr "scene" "scenes";',
    'workspace -fr "USD Export" "data";',
    'workspace -fr "mayaLT" "";',
    'workspace -fr "SAT_ATF" "data";',
    'workspace -fr "PROE_ATF" "data";',
    'workspace -fr "WIRE_ATF Export" "data";',
    'workspace -fr "sourceImages" "sourceimages";',
    'workspace -fr "clips" "clips";',
    'workspace -fr "furImages" "renderData/fur/furImages";',
    'workspace -fr "STEP_ATF" "data";',
    'workspace -fr "DWG_ATF Export" "data";',
    'workspace -fr "depth" "renderData/depth";',
    'workspace -fr "sceneAssembly" "sceneAssembly";',
    'workspace -fr "IGES_ATF Export" "data";',
    'workspace -fr "PARASOLID_ATF" "data";',
    'workspace -fr "IGES_ATF" "data";',
    'workspace -fr "teClipExports" "Time Editor/Clip Exports";',
    'workspace -fr "ASS" "data";',
    'workspace -fr "audio" "sound";',
    'workspace -fr "USD Import" "data";',
    'workspace -fr "Alembic" "data";',
    'workspace -fr "illustrator" "data";',
    'workspace -fr "diskCache" "data";',
    'workspace -fr "WIRE_ATF" "data";',
    'workspace -fr "templates" "assets";',
    'workspace -fr "OBJexport" "data";',
    'workspace -fr "furAttrMap" "renderData/fur/furAttrMap";']

