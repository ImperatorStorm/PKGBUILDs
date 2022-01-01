# Maintainer: Imperator Storm <30777770+ImperatorStorm@users.noreply.github.com>
# Contributor: Fredrick Brennan <copypaste@kittens.ph>
# Contributor: Andrew Bueide <abueide@protonmail.com>
# Contributor: rouhannb <rouhannb@protonmail.com>
# Contributor: Wilson E. Alvarez <wilson.e.alvarez1@gmail.com>
# Contributor: Benoit Favre <benoit.favre@gmail.com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Kamil Biduś <kamil.bidus@gmail.com>

pkgname=aseprite
pkgver=1.2.30
pkgrel=1
pkgdesc='Create animated sprites and pixel art'
arch=('x86_64')
url="http://www.aseprite.org/"
license=('custom')
depends=(
# ~ Aseprite's direct dependencies ~
# pixman is not linked to because we use Skia instead
# harfbuzz is linked statically because Aseprite expects an older version
cmark libcurl.so libgif.so libjpeg.so zlib libpng tinyxml libfreetype.so libarchive.so
# ~ Skia deps ~
# (Skia links dynamically to HarfBuzz, only Aseprite itself doesn't. >_<)
libexpat.so=1-64 icu libharfbuzz.so=0-64
# Already required by Aseprite: libjpeg-turbo libpng zlib freetype2
# These two are only reported by Namcap, but don't seem to be direct dependencies?
libfontconfig.so libxcursor)
makedepends=(cmake ninja git python)
source=("https://github.com/aseprite/aseprite/releases/download/v${pkgver}/Aseprite-v${pkgver}-Source.zip"
        # Which branch a given build of Aseprite requires is noted in its `INSTALL.md`
        "git+https://github.com/aseprite/skia.git#branch=aseprite-m81"
	"aseprite.desktop"
        # Python 3-compliant version of the script
        is_clang.py
        # Based on https://patch-diff.githubusercontent.com/raw/aseprite/aseprite/pull/2535.patch
        shared-libarchive.patch)
sha256sums=('9f4b098fe2327f2e9d73eb9f2aeebecad63e87ff2cf6fb6eeeee3c0778bb8874'
            'SKIP'
            'deaf646a615c79a4672b087562a09c44beef37e7acfc6f5f66a437d4f3b97a25'
            'cb901aaf479bcf1a2406ce21eb31e43d3581712a9ea245672ffd8fbcd9190441'
            'e42675504bfbc17655aef1dca957041095026cd3dd4e6981fb6df0a363948aa7')

prepare() {
	# Get Skia's build dependencies (requires connectivity, OK to do in `prepare()`)
	# TODO: we only need very few of these, see if we can skip cloning those we don't need
	env -C skia python tools/git-sync-deps

	# Replace `is_clang.py` with Python 3-compliant version
	cp -v is_clang.py skia/gn

	# Allow using shared libarchive (the bundled version prevents using the `None` build type...)
	patch -p1 <shared-libarchive.patch
}

build() {
	echo Building Skia...
	cd skia
	local skiadir="$PWD"
	# Must use the bundled `gn` executable and HarfBuzz libraries because of incompatibilities
	buildtools/linux64/gn gen build --args="is_debug=false is_official_build=true "\
skia_use_system_{expat,icu,libjpeg_turbo,libpng,libwebp,zlib,freetype2}"=true "\
"skia_use_system_harfbuzz=false "\
skia_use_{freetype,harfbuzz}"=true skia_use_sfntly=false skia_pdf_subset_harfbuzz=true"
	ninja -C build skia modules

	echo Building Aseprite...
	cd ..
	# gif2webp or img2webp is required to get `libwebpdemux`, which Aseprite requires
	cmake -S . -B build -G Ninja -Wno-dev -DCMAKE_BUILD_TYPE=None \
-DLAF_WITH_EXAMPLES=OFF -DLAF_WITH_TESTS=OFF -DLAF_BACKEND=skia \
-DSKIA_DIR="$skiadir" -DSKIA_LIBRARY_DIR="$skiadir/build" -DSKIA_LIBRARY="$skiadir/build/libskia.a" \
-DUSE_SHARED_{CMARK,CURL,GIFLIB,JPEGLIB,ZLIB,LIBPNG,TINYXML,PIXMAN,FREETYPE,HARFBUZZ,LIBARCHIVE}=YES \
-DWEBP_BUILD_{ANIM_UTILS,CWEBP,DWEBP,EXTRAS,IMG2WEBP,VWEBP,WEBPINFO,WEBP_JS}=NO \
-DWEBP_BUILD_GIF2WEBP=YES
	ninja -C build
}

check() {
	env -C build ctest --output-on-failure
}

package() {
	# Now the fun part: components of e.g. `libwebp` get installed as well,
	# since we've had to compile it. But we don't want them.
	# So, install normally, and then cherry-pick Aseprite's files out of that.
	# Use a whitelist to prefer installing not enough (breakage goes noticed),
	# instead of too much (cruft rarely goes noticed). Also hope that it doesn't break :)
	cmake --install build --prefix=staging --strip

	install -vDm 755 "$srcdir/staging/bin/aseprite" "$pkgdir/usr/bin/aseprite"
	install -vd "$pkgdir/usr/share/aseprite"
	cp -rv "$srcdir/staging/share/aseprite" "$pkgdir/usr/share"
	# Also install the EULA
	install -vDm 644 -t "$pkgdir/usr/share/licenses/$pkgname" "$srcdir/EULA.txt"
}
