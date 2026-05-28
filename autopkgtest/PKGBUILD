# Maintainer: weilinfox <caiweilin at iscas.ac.cn>

pkgname=autopkgtest
pkgver=5.39
pkgrel=1
pkgdesc="automatic as-installed testing for Debian packages"
arch=('any')
url="https://salsa.debian.org/ci-team/autopkgtest"
license=('GPL-2.0-or-later')
depends=('fakeroot' 'procps-ng' 'python' 'python-pycodestyle' 'python-pyflakes' 'python-debian' 'python-docutils' 'python-mock')
checkdepends=('git' 'pre-commit')
provides=('autopkgtest')
conflicts=('autopkgtest')
source=("https://salsa.debian.org/ci-team/autopkgtest/-/archive/debian/$pkgver/autopkgtest-debian-$pkgver.tar.gz")
sha512sums=("af608ff14dc78c819e29a3cb853ba2ed5a89848bad10edb7d8aef5e7c2bc92f8e81c5097992ae2d2d8208768002683d794fd03d3c45dd95ba83260f9eb308839")

build() {
	cd "$pkgname-debian-$pkgver"
	make all
}

package() {
	cd "$pkgname-debian-$pkgver"
	make DESTDIR="$pkgdir/" install
}
