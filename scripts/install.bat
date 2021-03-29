
@echo off

venv\Scripts\activate

python scripts\setup.py py2exe

REM pyinstaller src\Main.py
    REM --name CaveRun 
    REM --noconfirm ^
    REM --distpath pyinstaller\dist ^
    REM --workpath pyinstaller\build ^
    REM --specpath pyinstaller ^
    
deactivate
