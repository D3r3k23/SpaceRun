
executable="pyinstaller/dist/SpaceRun"
package_dir="package/SpaceRun"

if [[ -f $executable ]]; then
    if [[ -d $package_dir ]]; then
        rm -rf $package_dir
    fi
    mkdir -p $package_dir

    cp $executable $package_dir
    cp -r resources ${package_dir}/resources
else
    echo "No executable found."
fi
