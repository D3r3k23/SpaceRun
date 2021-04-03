
@echo off

mkdir package
mkdir package\SpaceRun

xcopy pyinstaller\dist\SpaceRun.exe package\SpaceRun /d
xcopy resources package\SpaceRun\resources\ /d /s
