import maya.cmds as cmds

def buildShelf():
    SHELF_NAME = "Chicken"

    if cmds.shelfLayout(SHELF_NAME, exists=True):
        cmds.deleteUI(SHELF_NAME)
    cmds.shelfLayout(SHELF_NAME, parent="ShelfLayout")
    
    try:
        import scratch
        cmds.shelfButton(parent=SHELF_NAME, label='Export OBJ', sourceType="python", command=scratch.exportObj, image='fileNew.png',  noDefaultPopup=True)
        cmds.shelfButton(parent=SHELF_NAME, label='Import OBJ', sourceType="python", command=scratch.importObj, image='fileOpen.png', noDefaultPopup=True)
        cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
    except:
        pass
    try:
        import creaseEdges
        selectCreaseBtn = cmds.shelfButton(parent=SHELF_NAME, label='modelChecker', sourceType="python", command=lambda *args: creaseEdges.selectCrease(), image='UVEditorEdge.png', noDefaultPopup=True)
        selectCreasePopup = cmds.popupMenu(selectCreaseBtn)
        cmds.menuItem(label="Select Crease - 1", parent=selectCreasePopup, command=lambda _: creaseEdges.selectCrease(1))
        cmds.menuItem(label="Select Crease - 2", parent=selectCreasePopup, command=lambda _: creaseEdges.selectCrease(2))
        cmds.menuItem(label="Select Crease - 3", parent=selectCreasePopup, command=lambda _: creaseEdges.selectCrease(3))
        
        setCreaseBtn = cmds.shelfButton(parent=SHELF_NAME, label='modelChecker', sourceType="python", command=lambda *args: creaseEdges.setCrease(3), image='UVTkEdge.png', noDefaultPopup=True)        
        setCreasePopup = cmds.popupMenu(setCreaseBtn)
        cmds.menuItem(label="Set Crease - 1", parent=setCreasePopup, command=lambda _: creaseEdges.setCrease(1))
        cmds.menuItem(label="Set Crease - 2", parent=setCreasePopup, command=lambda _: creaseEdges.setCrease(2))
        cmds.menuItem(label="Set Crease - 3", parent=setCreasePopup, command=lambda _: creaseEdges.setCrease(3))
        cmds.menuItem(label="Clear Creases" , parent=setCreasePopup, command=lambda _: creaseEdges.clearCrease())
    except:
        pass

    try:
        import modelChecker
        cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
        cmds.shelfButton(parent=SHELF_NAME, label='modelChecker', sourceType="python", command='from modelChecker import modelChecker_UI;modelChecker_UI.UI.show_UI()', image='polyGear.png', noDefaultPopup=True)
    except:
        pass

    try:
        import displayShaders
        cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
        cmds.shelfButton(parent=SHELF_NAME, label='Model Shader', sourceType="python", command=lambda: displayShaders.setDefaultLayer(), image='a_standard_surface.png', noDefaultPopup=True)
        cmds.shelfButton(parent=SHELF_NAME, label='UV Shader', sourceType="python", command=lambda: displayShaders.createMooseRenderLayer(), image='render_checker.png', noDefaultPopup=True)
    except:
        pass
    
    try:
        import scratch
        cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
        cmds.shelfButton(parent=SHELF_NAME, label='Export Low', sourceType="python", command=scratch.exportLow, image='out_polyCube.png', noDefaultPopup=True)
        cmds.shelfButton(parent=SHELF_NAME, label='Export High', sourceType="python", command=scratch.exportHigh, image='out_polySphere.png', noDefaultPopup=True)
        cmds.shelfButton(parent=SHELF_NAME, label='Export Game Model', sourceType="python", command=scratch.exportGameModel, image='game_exporter.png', noDefaultPopup=True)
        cmds.tabLayout("ShelfLayout", edit=True, selectTab=SHELF_NAME)
    except:
        pass