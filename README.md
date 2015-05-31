# Medcalc

MedCalc is a medical calculator for the Symbian S60 platform.

The source code was forked from https://code.google.com/p/medcalcs60/ for development continuation.


## Installation

* Install python 2.0 (actually it's [2.5.4](https://www.python.org/doc/2.5.4/)) runtime on device. You can download `python_2.0.0.sis` installer from [maemo.org](https://garage.maemo.org/frs/?group_id=854&release_id=3264) (see `PyS60_binaries_certificate_error_fixed.zip` archive).
* Install latest medcalc sis package. Binary installers are available at [releases page](https://github.com/radioxoma/medcalcs60/releases).


## Development


### Building

*NB! Windows bat file is outdated. I'm building sis package on Archlinux with `create_sis.sh`*

* Install python 2.5.
* Download and unpack `PythonForS60_2.0.0.tar.gz` from [PyS60 SDK](https://garage.maemo.org/frs/?group_id=854&release_id=3264) ('ensymble' buld system included).
* `git clone https://github.com/radioxoma/medcalcs60.git`
* Edit paths in `create_sis.sh` script for compatibility with `PythonForS60_2.0.0.tar.gz` content and source code placement.

From now building is easy:

    cd medcalcs60
    sh ./create_sis.sh


### Testing with Nokia SDK emulator

*NB! Symbian native SDK __requires registration__ after trial period and you can't get new account since Nokia forum shutdown.*

For example we are using *Symbian S60 3rd ed. FP2*.

* Download and install Symbian native SDK (includes emulator) from [here](http://n8delight.blogspot.com/2014/05/for-developers-re-up-of-symbian.html).
* Download compatible PyS60 SDK from [maemo.org](https://garage.maemo.org/frs/?group_id=854) (Python_2.0.0_SDK_3rdEdFP2.zip) and place its `epoc32` folder from this archive to Symbian SDK emulator path (e.g. to `C:\S60\devices\S60_3rd_FP2_SDK_v1.1` which contains `epoc32`).
* Now you can run the emulator (`C:\S60\devices\S60_3rd_FP2_SDK_v1.1\epoc32\release\winscw\udeb\epoc.exe`) and python ScriptShlell icon appears in the installed applications list.
