
mkdir -sgew package/SpaceRun
executable="pyinstaller/dist/SpaceRun"
package="package/SpaceRun"

if $executable exists:
    rm contents of $package
    cpy $executable $package
    cpy $resources $package
