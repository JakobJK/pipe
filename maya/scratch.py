import maya.cmds as cmds
import maya.mel as mel
from pathlib import Path
from util import getCurrentProject
from const import SCRATCH_DIR, SCRATCH_FILE, GAME_ASSETS_ROOT, ASSETS_ROOT


def _getScratchDir():
    scratch = Path(SCRATCH_DIR)
    scratch.mkdir(parents=True, exist_ok=True)
    return scratch

def _exportBakeMesh(lod):
    if lod not in ("high", "low"):
        cmds.warning(f"{lod} is not a valid LOD")

    curProject = getCurrentProject()
    if curProject:
        category, asset = curProject
        assetsPath = Path(ASSETS_ROOT) / category / asset
        marmosetPath = assetsPath / "marmoset/" 
        marmosetPath.mkdir(parents=True, exist_ok=True)
        file = marmosetPath / f"{asset}_{lod}.obj"
        cmds.file(str(file),
            options="groups=1;ptgroups=1;materials=0;smoothing=1;normals=1",
            force=True, 
            type="OBJexport",
            es=True)
        cmds.inViewMessage(amg=f"Yay! Asset exported:\n {asset} - {lod}", pos='midCenter', fade=True)
    else:
        cmds.warning(f"{lod} did not get exported!")

def exportHigh():
    _exportBakeMesh('high')


def exportLow():
    _exportBakeMesh('low')


def exportGameModel():
    curProject = getCurrentProject()
    if curProject:
        category, asset = curProject
        gameAssetsPath = Path(GAME_ASSETS_ROOT)
        projectAssetsPath = gameAssetsPath / category / asset
        projectAssetsPath.mkdir(parents=True, exist_ok=True)
        file = projectAssetsPath / f"{asset}_mdl.obj"
        cmds.file(str(file), 
            options="groups=1;ptgroups=1;materials=0;smoothing=1;normals=1",
            force=True, 
            type="OBJexport", 
            es=True)
        cmds.inViewMessage(amg=f"Game model exported:\n {asset}", pos='midCenter', fade=True)
    else:
        cmds.warning("High did not get exported!")


def importObj():
    file = _getScratchDir() / SCRATCH_FILE
    all_nodes = cmds.file(str(file), i=True, type="OBJ", rnn=True, ra=True, mnc=True, ns=":", options="mo=1;lo=0", pr=True)
    dagNodes = [node for node in all_nodes if cmds.nodeType(node) == "transform" and cmds.listRelatives(node, type="mesh", shapes=True)]
    for node in dagNodes:
        cmds.sets(node, e=True, forceElement='initialShadingGroup')
        cmds.polySoftEdge(node, a=180, ch=True)
        cmds.delete(node, ch=True)
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
    cmds.select(dagNodes, r=True)

def exportObj():
    file = _getScratchDir() / SCRATCH_FILE
    cmds.file(str(file),
        options="groups=1;ptgroups=1;materials=0;smoothing=1;normals=1",
        force=True, 
        type="OBJexport", 
        es=True)
    cmds.inViewMessage(amg="Obj Exported", pos='midCenter', fade=True)