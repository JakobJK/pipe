import maya.cmds as cmds
import maya.mel as mel
from pathlib import Path
SCRATCH_DIR = "D:/chicken/pipe/scratch"
FILENAME = "exported.obj"

def _getScratchDir():
    scratch = Path(SCRATCH_DIR)
    scratch.mkdir(parents=True, exist_ok=True)
    return scratch

def importObj():
    file = _getScratchDir() / FILENAME
    all_nodes = cmds.file(str(file), i=True, type="OBJ", rnn=True, ra=True, mnc=True, ns=":", options="mo=1;lo=0", pr=True)
    dagNodes = [node for node in all_nodes if cmds.nodeType(node) == "transform" and cmds.listRelatives(node, type="mesh", shapes=True)]

    for node in dagNodes:
        cmds.sets(node, e=True, forceElement='initialShadingGroup')
        cmds.polySoftEdge(node, a=180, ch=True)
        cmds.delete(node, ch=True)
    mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes");')
    cmds.select(dagNodes, r=True)

def exportObj():
    file = _getScratchDir() / FILENAME
    cmds.file(file, 
          force=True, 
          type="OBJexport", 
          pr=True, 
          es=True)