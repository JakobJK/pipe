import maya.app .renderSetup.model.selector as selector
import maya.app .renderSetup.model.renderSetup as renderSetup
import maya.cmds as cmds
import os

def createMooseModel(name="MooseModelShader"):
    if cmds.objExists(name):
        return name
    shader = cmds.shadingNode('blinn', asShader=True, name=f"{name}")
    shadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{name}SG")
    cmds.connectAttr(f"{shader}.outColor", f"{shadingGroup}.surfaceShader", force=True)
    return shadingGroup
    
def createMooseRenderLayer(shaderType="Checker"):
    rlName = f"Moose{shaderType}ShaderLayer"
    if not f"rs_{rlName}" in cmds.ls(type="renderLayer"):    
        rs = renderSetup.instance()
        rl = rs.createRenderLayer(rlName)
        col = rl.createCollection(f"{shaderType}Geometry")
        filterType, customFilter = selector.Filters.getFiltersFor('mesh')
        col.getSelector().setPattern('*')
        col.getSelector().setFilterType(filterType)
        col.getSelector().setCustomFilterValue(customFilter)
        mooseShader = None
        if shaderType == 'Model':
            mooseShader = createMooseModel()
        if shaderType == 'Checker':
            mooseShader = createMooseChecker()
        shaderOverride = col.createOverride(mooseShader, 'materialOverride')
        shaderOverride.setMaterial(mooseShader)
    cmds.editRenderLayerGlobals(currentRenderLayer=f"rs_{rlName}")
    
def createMooseChecker(name="MooseCheckerShader"):
    if cmds.objExists(name):
        return name
    
    currentFolder = os.path.dirname(os.path.abspath(__file__))
    filePath = f"{currentFolder}/uv.jpg"
    shader = cmds.shadingNode('lambert', asShader=True, name=name)
    shadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=f"{name}SG")
    cmds.connectAttr(f"{shader}.outColor", f"{shadingGroup}.surfaceShader", force=True)
    fileNode = cmds.shadingNode('file', asTexture=True)
    cmds.setAttr(fileNode + '.fileTextureName', filePath, type='string')
    cmds.connectAttr(fileNode + '.outColor', shader + '.color')
    return shadingGroup

def setDefaultLayer():
    cmds.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")