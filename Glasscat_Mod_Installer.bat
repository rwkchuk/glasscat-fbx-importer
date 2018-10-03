@echo off
echo ------------------------------
echo ------------------------------
echo ----- MOD FILE INSTALL -----
echo ------------------------------
echo ------------------------------

set DIR_LOCATION=%~dp0

:INSTALL
echo Start MAYA MOD FILE install . . .
echo %userprofile%
echo .

IF EXIST %userprofile%\Documents\maya\modules\ (
    echo Found MAYA MODULES and started installation . . .
    echo . . .
    XCOPY "%DIR_LOCATION%glasscat.mod" "%userprofile%\Documents\maya\modules\" /Y
    echo . . . Installation has finished
) else (
    echo MAYA MODULES is not found
    echo making modules folder . . .
    MD %userprofile%\Documents\maya\modules\
    echo folder made . . .

    GOTO INSTALL
)

echo Setting ENVIRONMENT VARIABLES

::move up to tools folder
CD ..
echo %cd%

::save tools folder as environment variable
set _CD=%cd%
set _MAYA_CD=%_CD:\=/%
echo %_MAYA_CD%
setx DIR_TEAM_SPOOPY_TOOLS %_MAYA_CD%
setx DIR_TEAM_SPOOPY_SCRIPTS %_MAYA_CD%/MayaModule/scripts
setx DIR_TEAM_SPOOPY_ICONS %_MAYA_CD%/MayaModule/icons
setx DIR_TEAM_SPOOPY_ASSETS %_MAYA_CD%/MayaModule/assets

pause