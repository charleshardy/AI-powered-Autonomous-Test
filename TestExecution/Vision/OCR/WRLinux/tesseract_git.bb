SUMMARY = "A commercial quality OCR engine "

LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://COPYING;md5=7ea4f9a43aba9d3c849fe5c203a0ed40"

BRANCH = "master"
PV = "4.0.0+git${SRCPV}"
SRCREV = "51316994ccae0b48692d547030f26c0969308214"
SRC_URI = "git://github.com/${BPN}-ocr/${BPN}.git;branch=${BRANCH}"
S = "${WORKDIR}/git"

DEPENDS = "leptonica"

EXTRA_OECONF += "LIBLEPT_HEADERSDIR=${STAGING_INCDIR}/leptonica"


inherit autotools pkgconfig

FILES_${PN} += "${datadir}/tessdata"

RRECOMMENDS_${PN} += "tesseract-lang-eng"
