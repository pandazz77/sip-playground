```sh
pip install sip

cd foo
sip-build --verbose # build sip module
# sip-sdist # build python package (I CANNOT INSTALL THIS PACKAGE)
# pip install pyfoo-01.tar.gz (I CANNOT INSTALL THIS PACKAGE)
sip-wheel # build python whee
pip install ./pyfoo-0.0.1-cp313-cp313-manylinux_2_5_x86_64.whl
```