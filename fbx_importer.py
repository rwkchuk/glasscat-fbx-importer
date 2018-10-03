''' This py file is to be called in maya in order to load the UE4 mannequin into the scene '''
import fbx_helper as fbx
import os

#printing the file location for testing purposes
print '{0}/SK_Mannequin.fbx'.format(os.getenv("DIR_TEAM_SPOOPY_ASSETS"))
#calling to import the mannequin
fbx.fbx_import('{0}/SK_Mannequin.fbx'.format(os.getenv("DIR_TEAM_SPOOPY_ASSETS")))