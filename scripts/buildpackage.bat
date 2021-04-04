
@echo off

set executable="pyinstaller\dist\SpaceRun.exe"
set package_dir="package\SpaceRun\"

if exist %executable% (
    if exist %package_dir% rmdir /q /s %package_dir%
    mkdir %package_dir%

    xcopy /q %executable% %package_dir%
    xcopy /q /e resources %package_dir%\resources\
) else (
    echo No executable found.
)
