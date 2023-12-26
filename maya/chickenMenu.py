import maya.cmds as cmds

def build():
    menuName = menuLabel = 'Chicken'

    if cmds.menu(menuName, l=menuLabel, p='MayaWindow', exists=True):
        cmds.deleteUI(menuName, menu=True)
    mooseMenu = cmds.menu(menuName, label=menuLabel, parent='MayaWindow', tearOff=True)

    try:
        import chickenShelf
        cmds.menuItem('Submitter', label='Build Chicken Shelf', parent=mooseMenu, command=lambda x: chickenShelf.buildShelf())
    except:
        cmds.menuItem('Submitter', label='Chicken Shelf', parent=mooseMenu, enable=False)