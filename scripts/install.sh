
# Must activate virtualenv first

pyinstaller src/Main.py            \
    --name SpaceRun                \
    --onefile                      \
    --paths venv/lib/site-packages \
    --specpath pyinstaller         \
    --distpath pyinstaller/dist    \
    --workpath pyinstaller/build   \
    --noconfirm
