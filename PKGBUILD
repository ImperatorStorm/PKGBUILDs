# Maintainer: Imperator Storm <imperatorstorm11@protonmail.com>
pkgname=3beans-git
pkgver=r234.059f190
pkgrel=1
pkgdesc="A low-level 3DS emulator"
arch=(x86_64 aarch64)
url="https://github.com/Hydr8gon/3Beans"
license=('GPL-3.0-or-later')
depends=(wxwidgets-gtk3-git # HACK: replace with wxwidgets-gtk3>=3.3.2
portaudio
libepoxy)
makedepends=(git)
#checkdepends=()
#optdepends=()
provides=(3beans)
conflicts=(3beans)
replaces=()
backup=()
options=()
source=("git+https://github.com/Hydr8gon/3Beans.git")
sha256sums=('SKIP')
validpgpkeys=()

pkgver() {
	cd "$srcdir/3Beans"
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
	cd "$srcdir/3Beans"
	make
}

# check() {
# 	cd "$srcdir/3Beans"
# 	make -k check
# }

package() {
	cd "$srcdir/3Beans"
	make DESTDIR="$pkgdir/" install
}
