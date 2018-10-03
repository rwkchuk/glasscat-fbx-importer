import maya.cmds as cmds
import maya.utils as utils
from maya import mel

#printing for testing purposes
print 'Hello world its johnny !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'

#use mel when available to load the Glasscat tools shelf
utils.executeDeferred("mel.eval('loadNewShelf \"shelf_GlassCatTools.mel\"')")
