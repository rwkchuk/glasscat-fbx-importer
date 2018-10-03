''' A collection of functions to help with FBX use in Maya. '''
import maya.cmds as cmds
from maya import mel

def fbx_import(str_directory=''):
    ''' import fbx file with no takes and adds to the scene '''
    #setting import options
    mel.eval('FBXImportMode -v add')
    mel.eval('FBXImportSkins -v false')
    mel.eval('FBXImportSetLockedAttribute -v true')
    mel.eval('FBXImportConstraints -v false')

    #printing for testing purposes
    print str_directory
    #importing the fbx
    mel.eval('FBXImport -f "{0}"'.format(str_directory))