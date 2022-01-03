# Maintainer: Imperator Storm <30777770+ImperatorStorm@users.noreply.github.com>
# Co-Maintainer: Eldred Habert <me@eldred.fr>
# Contributor: Fredrick Brennan <copypaste@kittens.ph>
# Contributor: Andrew Bueide <abueide@protonmail.com>
# Contributor: rouhannb <rouhannb@protonmail.com>
# Contributor: Wilson E. Alvarez <wilson.e.alvarez1@gmail.com>
# Contributor: Benoit Favre <benoit.favre@gmail.com>
# Contributor: Alexander Rødseth <rodseth@gmail.com>
# Contributor: Kamil Biduś <kamil.bidus@gmail.com>

pkgname=aseprite
pkgver=1.2.30
pkgrel=4
pkgdesc='Create animated sprites and pixel art'
arch=('x86_64')
url="https://www.aseprite.org/"
license=('custom')
depends=(# ~ Aseprite's direct dependencies ~
         # pixman is not linked to because we use Skia instead
         # harfbuzz is linked statically because Aseprite expects an older version
         cmark libcurl.so libgif.so libjpeg.so zlib libpng tinyxml libfreetype.so libarchive.so
         hicolor-icon-theme # For installing Aseprite's icons
         # ~ Skia deps ~
         # (Skia links dynamically to HarfBuzz, only Aseprite itself doesn't. >_<)
         libexpat.so=1-64 libharfbuzz.so=0-64
         # Already required by Aseprite: libjpeg-turbo libpng zlib freetype2
         # These two are only reported by Namcap, but don't seem to be direct dependencies?
         libfontconfig.so libxcursor)
makedepends=(# "Meta" dependencies
             cmake ninja git python
             # Aseprite (including e.g. LAF)
             libxi
             # Skia
             # harfbuzz-icu would be required if we weren't using the bundled version
             )
source=("https://github.com/aseprite/aseprite/releases/download/v$pkgver/Aseprite-v$pkgver-Source.zip"
        # Which branch a given build of Aseprite requires is noted in its `INSTALL.md`
        "git+https://github.com/aseprite/skia.git#branch=aseprite-m81"
        "$pkgname.desktop"
        # Python 3-compliant version of the script
        is_clang.py
        # Based on https://patch-diff.githubusercontent.com/raw/aseprite/aseprite/pull/2535.patch
        shared-libarchive.patch)
noextract=("${source[0]##*/}") # Don't extract Aseprite sources at the root
sha256sums=('9f4b098fe2327f2e9d73eb9f2aeebecad63e87ff2cf6fb6eeeee3c0778bb8874'
            'SKIP'
            'deaf646a615c79a4672b087562a09c44beef37e7acfc6f5f66a437d4f3b97a25'
            'cb901aaf479bcf1a2406ce21eb31e43d3581712a9ea245672ffd8fbcd9190441'
            'e42675504bfbc17655aef1dca957041095026cd3dd4e6981fb6df0a363948aa7')

prepare() {
	# Extract Aseprite's sources
	mkdir -p aseprite
	bsdtar -xf "${noextract[0]}" -C aseprite

	# Get Skia's build dependencies (requires connectivity, OK to do in `prepare()`)
	# TODO: we only need very few of these, see if we can skip cloning those we don't need
	env -C skia python tools/git-sync-deps

	# Replace `is_clang.py` with Python 3-compliant version
	cp -v is_clang.py skia/gn

	# Allow using shared libarchive (the bundled version prevents using the `None` build type...)
	env -C aseprite patch -tp1 <shared-libarchive.patch
}

build() {
	echo Building Skia...
	local _skiadir="$PWD/skia/obj"
	# Must use the bundled `gn` executable and HarfBuzz libraries because of incompatibilities
	# Flags can typically be found in `src/skia/gn/skia.gni`... but you're kind of on your own
	env -C skia buildtools/linux64/gn gen "$_skiadir" --args="is_debug=false is_official_build=true "\
skia_use_system_{expat,icu,libjpeg_turbo,libpng,libwebp,zlib,freetype2}"=true "\
"skia_use_system_harfbuzz=false "\
skia_use_{freetype,harfbuzz}"=true skia_use_sfntly=false skia_enable_skottie=false"
	ninja -C "$_skiadir" skia modules

	echo Building Aseprite...
	# gif2webp or img2webp is required to get `libwebpdemux`, which Aseprite requires
	# Suppress install messages since we install to a temporary area; `install -v` will do the job
	cmake -S aseprite -B build -G Ninja -Wno-dev -DCMAKE_INSTALL_MESSAGE=NEVER -DCMAKE_BUILD_TYPE=None \
-DLAF_WITH_EXAMPLES=OFF -DLAF_WITH_TESTS=OFF -DLAF_BACKEND=skia \
-DSKIA_DIR="$PWD/skia" -DSKIA_LIBRARY_DIR="$_skiadir" -DSKIA_LIBRARY="$_skiadir/libskia.a" \
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

	# Install the binary and its `.desktop` file
	install -vDm 755 staging/bin/aseprite "$pkgdir/usr/bin/aseprite"
	install -vDm 644 aseprite.desktop "$pkgdir/usr/share/applications/$pkgname.desktop"
	# Install the icons in the correct directory (which is not the default)
	local _size
	for _size in 16 32 48 64 128 256; do
		# The installed icon's name is taken from the `.desktop` file
		install -vDm 644 staging/share/aseprite/data/icons/ase$_size.png "$pkgdir/usr/share/icons/hicolor/${_size}x$_size/apps/aseprite.png"
	done
	# Delete the icons to avoid copying them in two places (they aren't used by Aseprite itself)
	rm -rf staging/share/aseprite/data/icons
	# Install all of the program's data
	cp -vrt "$pkgdir/usr/share" staging/share/aseprite
	# Also install the licenses
	install -vDm 644 -t "$pkgdir/usr/share/licenses/$pkgname" EULA.txt docs/LICENSES.md
	# Copy the font's license, but leave it in the font directory as well (probably doesn't hurt)
	install -vm 644 data/fonts/LICENSE.txt "$pkgdir/usr/share/licenses/$pkgname/font.txt"
}
