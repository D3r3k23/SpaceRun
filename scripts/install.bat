
@echo off

@REM venv\Scripts\activate

pyinstaller src\Main.py --name SpaceRun --windowed --onedir --specpath pyinstaller --distpath pyinstaller\dist --workpath pyinstaller\build -y

@REM src\Main.py --name SpaceRun --noconfirm --icon resources\images\icon\icon.ico
@REM --distpath pyinstaller\dist --workpath pyinstaller\build --specpath pyinstaller

@REM venv\Scripts\deactivate
