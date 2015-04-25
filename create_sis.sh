#!/usr/bin/env bash

# Path to module-repo, ensymble, inside PythonForS60
PYS60DIR="${HOME}/build/pys60/PythonForS60"
CERPATH="${HOME}/Документы/Dropbox/Документы/doc/Python/PythonForS60/signing/cer"
PROJECTDIR=`pwd`
APPNAME=Medcalc
VERSION=0.6.4
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
      --lang=PO,RU
      --extrasdir=extras
      --icon=${PROJECTDIR}/${ICON}
      --textfile=${PROJECTDIR}/disclaimer.txt
      --heapsize=4k,5M
      "
#
# --extrasdir=     - Name of dir. tree placed under drive root
# --extra-modules= - Additional dependency modules that should be packaged with the application
# sys.prefix == 'C:\\resource\\python25'
# etc 'C:\\DATA\\python', 'System\libs', 'System\apps\python\my'

rm -r ${TMPDIR}/*
echo "Populating temp dir"

cp -r ${SRCDIR}/default.py ${TMPDIR}/
cp -r ${SRCDIR}/medcalc ${TMPDIR}/

mkdir -p ${TMPDIR}/extras/data/python/medcalc
cp -r ${SRCDIR}/img/* ${TMPDIR}/extras/data/python/medcalc/
# cp -r ${SRCDIR}/img/* ${TMPDIR}/extras/resource/python25/share/medcalc

echo "Compiling localization files"
# https://wiki.maemo.org/Internationalize_a_Python_application
# Copy localisation file(s) to default location
# gettext._default_localedir == 'c:/resource/python25/share/locale'
mkdir -p ${TMPDIR}/extras/resource/python25/share/locale/ru/LC_MESSAGES/
msgfmt -c ${SRCDIR}/locale/ru/LC_MESSAGES/medcalc.po \
       -o ${TMPDIR}/extras/resource/python25/share/locale/ru/LC_MESSAGES/medcalc.mo
# cp -r ${SRCDIR}/locale/ ${TMPDIR}/extras/resource/python25/share/
# find ${TMPDIR}/extras/resource/python25/share/locale -type f ! -name '*.mo' -delete

cd ${PYS60DIR}
python2.5 ${PYS60DIR}/ensymble.py py2sis ${OPTS} "${PROJECTDIR}/${TMPDIR}" "${PROJECTDIR}/${APPNAME}-${VERSION}.sis"
