# Maintainer: weilinfox <caiweilin at iscas.ac.cn>

pkgname=autopkgtest
pkgver=5.55
pkgrel=1
pkgdesc="automatic as-installed testing for Debian packages"
arch=('any')
url="https://salsa.debian.org/ci-team/autopkgtest"
license=('GPL-2.0-or-later')
depends=('fakeroot' 'procps-ng' 'python' 'python-pycodestyle' 'python-pyflakes' 'python-debian' 'python-docutils' 'python-mock')
source=("https://salsa.debian.org/ci-team/autopkgtest/-/archive/debian/$pkgver/autopkgtest-debian-$pkgver.tar.gz")
sha512sums=('000c30effa19615f24b1762d8f63e1537ab328e49f9feca3d7e8fd4b4eadc5f79785134f47ed5d7e52adbbc47939e953449cf2fbfc23967bae1f36aaabd3d000')

build() {
	cd "$pkgname-debian-$pkgver"
	make all
}

package() {
	cd "$pkgname-debian-$pkgver"
	make DESTDIR="$pkgdir/" install
}
