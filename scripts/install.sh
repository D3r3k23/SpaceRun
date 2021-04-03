
venv/bin/activate

pyinstaller src/Main.py                   \
    --name SpaceRun                       \
    --onefile                             \
    --windowed                            \
    --icon resources/images/icon/icon.ico \
    --paths venv/Lib/site-packages        \
    --specpath pyinstaller                \
    --distpath pyinstalled/dist           \
    --workpath pyinstaller/build          \
    --noconfirm

venv/bin/deactivate
