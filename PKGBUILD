# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
# Contributor: Sunny <brainworms2002 at gmail dot com>

pkgname="uzdoom-appimage"
pkgver=4.14.3.rc1
_srctag=${pkgver%.*}-${pkgver##*.}
pkgrel=3
pkgdesc="UZDoom is a feature centric port for all Doom engine games, based on GZDoom, adding an advanced renderer and powerful scripting capabilities (Appimage)"
url="https://github.com/UZDoom/UZDoom"
license=("GPL-3.0-or-later" "BSD-3-Clause" "LGPL-3.0-or-later" "LicenseRef-DUMB" "bzip2-1.0.6" "0BSD" )
arch=("x86_64")
provides=("uzdoom")
conflicts=("uzdoom")
depends=(zlib glibc)
source=("https://github.com/UZDoom/UZDoom/releases/download/$_srctag/Linux-UZDoom-$_srctag-x86_64.AppImage")
sha256sums=('12af678fd9855723fda4319bf1dc833ae652e0ee4f792e9fc0f95df52372e932')
options=(!strip !debug)
build() {
  chmod +x "Linux-UZDoom-$_srctag-x86_64.AppImage"
  "./Linux-UZDoom-$_srctag-x86_64.AppImage" --appimage-extract
}

package() {
  install -Dm755 "Linux-UZDoom-$_srctag-x86_64.AppImage" "$pkgdir/usr/bin/uzdoom"
  install -Dm644 "$srcdir/squashfs-root/org.zdoom.UZDoom.svg" -t "$pkgdir/usr/share/pixmaps/"
  install -Dm644 "$srcdir/squashfs-root/org.zdoom.UZDoom.desktop" -t "$pkgdir/usr/share/applications/"
  install -Dm644 "$srcdir/squashfs-root/usr/share/doc/uzdoom/licenses/"* -t "$pkgdir/usr/share/licenses/uzdoom-appimage/"
}
