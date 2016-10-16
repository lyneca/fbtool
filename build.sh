electron-packager . fbtools --app-version $1 --arch ia32,x64 --platform win32,linux,darwin --asar --overwrite --out releases
cd releases
echo "Zipping..."
for file in fbtools-*
do
echo "$file -> $file.tar.gz"
tar czf "$file.tar.gz" $file
done
cd ..
