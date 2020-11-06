# pre_clean
rm -rf dist
rm -rf build

# build (amd64)
#docker build -t csv2xlsx_image --build-arg ARCH=amd64 .
docker run -i --rm -v $(pwd):/home csv2xlsx_image /bin/sh << CMD
cd /home
pyinstaller --onefile csv2xlsx.py
mv dist/csv2xlsx dist/csv2xlsx_amd64
CMD

# post_clean
rm -rf build