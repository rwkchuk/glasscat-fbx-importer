# glasscat-fbx-importer
Files for the glasscat fbx importer excluding the shelf's .mel file

The fbx_helper.py and fbx_importer.py files are specific to an artist requested tool used in maya. The tool
  imports a copy of the UE4 mannequin into the scene at the press of a shelf button so the artist can get correct scale. Previous 
  to having this tool the project environment artist would keep all props and meshes in a single bloated maya ascii file to keep
  scale consistent. Upon using this tool they would have everything in it's own maya ascii file since scale was so easy to check.
  
The glasscat.mod, userSetup.py, and Glasscat_Mod_Installer.bat files are specific to starting maya for the team. The team consists
  of about 15 members some of who arn't in the same geographic location. The only consistent variables for the team is everyone is
  using windows, perforce, and maya 2018. Due to time and experience I opted to distribute future maya tools for the team through 
  the depot. Thus I use a maya module file that points to the DIR_TEAM_SPOOPY_TOOLS environment variable which is set on the 
  module installation. That dir contains the scripts and icons folders specific to maya but also any additional assets required
  specifically for tool usage such as an assets folder that holds a fbx of the UE4 mannequin.
