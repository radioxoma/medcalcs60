#!/usr/bin/env bash

# Path to module-repo, ensymble, inside PythonForS60
PYS60DIR="${HOME}/build/pys60/PythonForS60"
PROJECTDIR=`pwd`
APPNAME=Medcalc
# Version n.n.n appears n.n(n) on device
VERSION=`python2 -c "import runpy; print(
    runpy.run_path('src/medcalc/__init__.py')['__version__'])"`
# VERSION=`grep -o "[0-9].*[0-9]" src/medcalc/__init__.py`
CAPBLS=ReadUserData+WriteUserData
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
find ${SRCDIR}/locale/ -name \*.po -execdir msgfmt medcalc.po -o medcalc.mo \;
mkdir -p ${TMPDIR}/extras/resource/python25/share/locale/
cp -r ${SRCDIR}/locale/ ${TMPDIR}/extras/resource/python25/share/
find ${TMPDIR}/extras/resource/python25/share/locale -type f ! -name '*.mo' -delete

# --extrasdir=     - Name of dir. tree placed under drive root
# --extra-modules= - Additional dependency modules that should be packaged with the application
# sys.prefix == 'C:\\resource\\python25'
# etc 'C:\\DATA\\python', 'System\libs', 'System\apps\python\my'

cd ${PYS60DIR}
python2.5 ${PYS60DIR}/ensymble.py py2sis \
    --verbose \
    --appname="${APPNAME}" \
    --version="${VERSION}" \
    --uid="0xeef3508c" `# From original package`\
    --caps="${CAPBLS}" \
    --vendor="Eugene Dvoretsky","Eugene Dvoretsky","Евгений Дворецкий" \
    --lang=EN,PO,RU \
    --extrasdir=extras \
    --icon="${PROJECTDIR}/${SRCDIR}/logo.svg" \
    --textfile="${PROJECTDIR}/eula/%c.txt" `# UTF-8 with BOM` \
    --heapsize=4k,5M \
    "${PROJECTDIR}/${TMPDIR}" "${PROJECTDIR}/${APPNAME}-${VERSION}.sis"

echo "Binary '${APPNAME}-${VERSION}.sis' created."
