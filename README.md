# Medcalc

MedCalc is a medical calculator for the Symbian S60 platform.

The source code was forked from https://code.google.com/p/medcalcs60/ for development continuation.


## Testing

[PyS60 Emulation Library](http://sourceforge.net/p/pys60-compat/) (pys60compat) can be handy. Use [latest](http://sourceforge.net/p/pys60-compat/code/HEAD/tarball) version from SVN. Works fine only on Windows for me.


## Building

*NB! Windows bat file is outdated. I'm building sis package on Archlinux with `create_sis.sh`*

* Receive own certificate on [shoujizu.net](http://www.shoujizu.net/en/cer.php) or [allnokia.ru](http://allnokia.ru/symb_cert/) site (symbiansigned had closed).
* Install python 2.5.
* Download and unpack [PythonForS60_2.0.0.tar.gz](https://garage.maemo.org/frs/download.php/7486/PythonForS60_2.0.0.tar.gz) from PyS60 SDK ('ensymble' buld system included).
* Edit paths in `create_sis.sh` script for compatibility with your SDK and other files placement.

        git clone https://github.com/radioxoma/medcalcs60.git
        cd medcalcs60
        sh ./create_sis.sh


## Installing

* Install python 2.0 (actually it's [2.5.4](https://www.python.org/doc/2.5.4/)) runtime on device.
* Install the built sis package.
