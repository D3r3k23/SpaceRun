
@REM Pyinstaller build
@REM MUST FIRST ACTIVATE VIRTUALENV

@echo off

pyinstaller src\Main.py            ^
    --name SpaceRun                ^
    --onefile                      ^
    --windowed                     ^
    --paths venv\Lib\site-packages ^
    --specpath pyinstaller         ^
    --distpath pyinstaller\dist    ^
    --workpath pyinstaller\build   ^
    --noconfirm

    @REM --icon resources\images\icon\icon.ico ^
    @REM **** Have to manually set the icon for now ****
    
