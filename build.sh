rm -r releases/*
electron-packager . fbtools --app-version $1 --arch ia32,x64 --platform win32,linux,darwin --asar --overwrite --out releases
cd releases
echo "Zipping..."
for file in fbtools-win32-*
do
echo "$file -> $file.zip"
zip -qr "$file.zip" $file
done
for file in fbtools-linux-*
do
echo "$file -> $file.tar.gz"
tar czf "$file.tar.gz" $file
done
for file in fbtools-darwin-*
do
echo "$file -> $file.tar.gz"
tar czf "$file.tar.gz" $file
done
cd ..
