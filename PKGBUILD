# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
pkgname=debsums
pkgver=3.0.2.4
pkgrel=1
pkgdesc=".deb package installation, upgrading, and removal testing tool"
arch=(any)
url="https://debsums.debian.org/"
license=(GPL-2.0-or-later)
depends=(dpkg perl-file-fnmatch)
makedepends=(po4a)
checkdepends=(perl-test-command-simple)
optdepends=()
provides=()
conflicts=()
replaces=()
source=("https://deb.debian.org/debian/pool/main/d/debsums/debsums_$pkgver.tar.xz")
noextract=()
sha256sums=('ed960631eea07c494f802120d1810e5aaa92dc8a17517d9451d7314521c37495')
validpgpkeys=()

# prepare() {
# 	cd "$pkgname_$pkgver"
# 	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
# }

check() {
	cd "$pkgname"
	make -k test
}

package() {
	cd "$pkgname"
	make DESTDIR="$pkgdir/" prefix=/usr install
	install -vDm755 debsums $pkgdir/usr/bin/debsums
	install -vDm755 rdebsums $pkgdir/usr/bin/rdebsums
	# HACK: I *could* use debhelper here, but it and dh-autoreconf depend
	# 	on eachother and rebuilds would get really messy
	install -vDm644 man/debsums.1 $pkgdir/usr/share/man/man1/debsums.1
	install -vDm644 man/rdebsums.1 $pkgdir/usr/share/man/man1/rdebsums.1
	for lang in de es pt pt_BR ro ru sv; do
	install -vDm644 man/$lang/debsums.$lang.1 $pkgdir/usr/share/man/$lang/man1/debsums.1
	# install -vDm644 man/$lang/rdebsums.$lang.1 $pkgdir/usr/share/man/$lang/man1/rdebsums.1 # English-exclusive??
	done
	gzip debian/changelog
	mkdir -p $pkgdir/usr/share/doc/debsums/
	install -vDm644 README debian/changelog.gz debian/copyright $pkgdir/usr/share/doc/debsums/
	install -vDm644 debian/debsums.bash-completion $pkgdir/usr/share/bash-completion/completions/debsums
	install -vDm644 debian/debsums.lintian-overrides $pkgdir/usr/share/lintian/overrides/debsums
}