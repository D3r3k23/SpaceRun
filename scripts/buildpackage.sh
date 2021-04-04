
executable="pyinstaller/dist/SpaceRun"
package="package/SpaceRun"

mkdir -p $package

if [[ -f $executable ]]; then
    cp -f $executable $package
    cp -f -r resources $package
else
    echo "No executable found."
fi
