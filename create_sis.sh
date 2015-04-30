#!/usr/bin/env bash

# Path to module-repo, ensymble, inside PythonForS60
PYS60DIR="${HOME}/build/pys60/PythonForS60"
CERPATH="${HOME}/Документы/Dropbox/Документы/doc/Python/PythonForS60/signing/cer"
PROJECTDIR=`pwd`
APPNAME=Medcalc
VERSION=0.6.5
CAPBLS=LocalServices+ReadUserData+WriteUserData+UserEnvironment
SRCDIR=src
TMPDIR=src.tmp

if [ -d "${TMPDIR}" ]
then
    echo "${TMPDIR} found"
    if find ${TMPDIR} -maxdepth 0 -empty | read v
    then
        echo "${TMPDIR} is empty, nothing to do"
    else
        echo "Removing ${TMPDIR} content"
        rm -r ${TMPDIR}/*
    fi
else
    echo "Creating an empty ${TMPDIR} directory"
    mkdir -p "${TMPDIR}/"
fi

cp -r ${SRCDIR}/default.py ${TMPDIR}/
cp -r ${SRCDIR}/medcalc ${TMPDIR}/

echo "Copying images"
mkdir -p ${TMPDIR}/extras/resource/python25/share/medcalc
cp -r ${SRCDIR}/img/* ${TMPDIR}/extras/resource/python25/share/medcalc

echo "Compiling localization files"
# https://wiki.maemo.org/Internationalize_a_Python_application
# Copy localisation file(s) to default location
# gettext._default_localedir == 'c:/resource/python25/share/locale'
mkdir -p ${TMPDIR}/extras/resource/python25/share/locale/ru/LC_MESSAGES/
msgfmt -c ${SRCDIR}/locale/ru/LC_MESSAGES/medcalc.po \
       -o ${TMPDIR}/extras/resource/python25/share/locale/ru/LC_MESSAGES/medcalc.mo
# cp -r ${SRCDIR}/locale/ ${TMPDIR}/extras/resource/python25/share/
# find ${TMPDIR}/extras/resource/python25/share/locale -type f ! -name '*.mo' -delete


# --caption="English Caption","French Caption","German Caption"
# --extrasdir=     - Name of dir. tree placed under drive root
# --extra-modules= - Additional dependency modules that should be packaged with the application
# sys.prefix == 'C:\\resource\\python25'
# etc 'C:\\DATA\\python', 'System\libs', 'System\apps\python\my'

# --textfile
cd ${PYS60DIR}
python2.5 ${PYS60DIR}/ensymble.py py2sis \
    --verbose \
    --appname="${APPNAME}" \
    --version="${VERSION}" \
    --caps="${CAPBLS}" \
    --vendor="Eugene Dvoretsky","Eugene Dvoretsky","Евгений Дворецкий" \
    --cert="${CERPATH}/2009-11-18.cer" \
    --privkey="${CERPATH}/2009-11-18.key" \
    --passphrase="" \
    --lang=EN,PO,RU \
    --extrasdir=extras \
    --icon="${PROJECTDIR}/${SRCDIR}/logo2.svg" \
    --textfile="${PROJECTDIR}/eula/%c.txt" `# UTF-8 with BOM` \
    --heapsize=4k,5M \
    "${PROJECTDIR}/${TMPDIR}" "${PROJECTDIR}/${APPNAME}-${VERSION}.sis"
