import maya.cmds as cmds

def buildShelf():
    SHELF_NAME = "Chicken"

    if cmds.shelfLayout(SHELF_NAME, exists=True):
        cmds.deleteUI(SHELF_NAME)
    cmds.shelfLayout(SHELF_NAME, parent="ShelfLayout")
    
    cmds.shelfButton(parent=SHELF_NAME, label='Export OBJ', sourceType="python", command='print("...")', image='fileNew.png',  noDefaultPopup=True)
    cmds.shelfButton(parent=SHELF_NAME, label='Import OBJ', sourceType="python", command='print("...")', image='fileOpen.png', noDefaultPopup=True)
    cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
    cmds.shelfButton(parent=SHELF_NAME, label='modelChecker', sourceType="python", command='from modelChecker import modelChecker_UI;modelChecker_UI.UI.show_UI()', image='polyGear.png', noDefaultPopup=True)
    try:
        import displayShaders
        cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
        cmds.shelfButton(parent=SHELF_NAME, label='Model Shader', sourceType="python", command=lambda: displayShaders.setDefaultLayer(), image='a_standard_surface.png', noDefaultPopup=True)
        cmds.shelfButton(parent=SHELF_NAME, label='UV Shader', sourceType="python", command=lambda: displayShaders.createMooseRenderLayer(), image='render_checker.png', noDefaultPopup=True)
    except:
        pass
        
    cmds.separator(parent=SHELF_NAME, width=12, height=35, style="shelf", horizontal=False)
    cmds.shelfButton(parent=SHELF_NAME, label='Export Low', sourceType="python", command='print("")', image='out_polyCube.png', noDefaultPopup=True)
    cmds.shelfButton(parent=SHELF_NAME, label='Export High', sourceType="python", command='print("")', image='out_polySphere.png', noDefaultPopup=True)
    cmds.shelfButton(parent=SHELF_NAME, label='Export Game Model', sourceType="python", command='print("")', image='game_exporter.png', noDefaultPopup=True)

    cmds.tabLayout("ShelfLayout", edit=True, selectTab=SHELF_NAME)