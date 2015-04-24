#!/usr/bin/env bash

# Path to module-repo, ensymble, inside PythonForS60
PYS60DIR="${HOME}/build/pys60/PythonForS60"
CERPATH="${HOME}/Документы/Dropbox/Документы/doc/Python/PythonForS60/signing/cer"
PROJECTDIR=`pwd`
APPNAME=Medcalc
VERSION=0.6.1
CAPBLS=LocalServices+ReadUserData+WriteUserData+UserEnvironment
SRCDIR=src
TMPDIR=src.tmp
ICON=${SRCDIR}/logo2.svg

OPTS="--verbose
      --appname=${APPNAME}
      --version=${VERSION}
      --caps=${CAPBLS}
      --vendor=EugeneDvoretsky
      --cert=${CERPATH}/2009-11-18.cer
      --privkey=${CERPATH}/2009-11-18.key
      --passphrase=''
      --lang=PO,EN,RU
      --icon=${PROJECTDIR}/${ICON}
      --textfile=${PROJECTDIR}/disclaimer.txt
      --extrasdir=extras
      --heapsize=4k,5M
	"
# --extrasdir=     - Name of dir. tree placed under drive root
# --extra-modules= - Additional dependency modules that should be packaged with the application

echo "Populating temp dir"
rm -r ${TMPDIR}/*
mkdir -p ${TMPDIR}/extras/data/python/medcalc

cp -r ${SRCDIR}/lib/* ${TMPDIR}/extras/data/python/medcalc/
cp -r ${SRCDIR}/img/* ${TMPDIR}/extras/data/python/medcalc/
cp -r ${SRCDIR}/default.py ${TMPDIR}/

# Compile po files
# https://wiki.maemo.org/Internationalize_a_Python_application

# sys.prefix == 'C:\\resource\\python25'
# etc 'C:\\DATA\\python', 'System\libs', 'System\apps\python\my'

# Отсутствует компонент "Python for S60". Продолжить? Reading past correspondence on this form, this error appears to be because the UID for Python and its runtimes have changed between PyS60 1.4.x and 1.9.x.
# https://garage.maemo.org/frs/?group_id=854&release_id=2763

cd ${PYS60DIR}
python2.5 ${PYS60DIR}/ensymble.py py2sis ${OPTS} "${PROJECTDIR}/${TMPDIR}" "${PROJECTDIR}/${APPNAME}-${VERSION}.sis"
