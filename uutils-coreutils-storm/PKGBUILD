# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
# Contributor: Sam <dev at samarthj dot com>
# Contributor: Árni Dagur <arnidg@protonmail.ch>

# shellcheck disable=2034,2148,2154

pkgname="uutils-coreutils-storm"
_pkgname="coreutils"
pkgver=0.0.13
pkgrel=1
pkgdesc="GNU Coreutils rewritten in Rust"
arch=('x86_64')
url='https://github.com/uutils/coreutils'
license=('MIT')
depends=('glibc' 'gcc-libs')
makedepends=('rust' 'cargo' 'python-sphinx')
conflicts=('uutils-coreutils-git' 'coreutils')
provides=('coreutils')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
        tests.patch)
sha256sums=('4f5de6369a826837dfb6fe578580589d38f69e6d2aa9ccc103c9c075c466ff32'
            'ed6a905a004275b4629d2a720d6697c845e2c48e8a1062bd27284ced3631baf8')
options=(!lto)


prepare() {
  cd $_pkgname-$pkgver
  sed 's|"bin"|"builduser"|g' -i tests/by-util/test_{chgrp,chown}.rs
  patch -Np1 < ../tests.patch
}

build() {
  cd $_pkgname-$pkgver
  make PROFILE=release
}

check() {
  cd $_pkgname-$pkgver
   make test \
      PROFILE=release \
      CARGOFLAGS=--release \
      TEST_NO_FAIL_FAST="--no-fail-fast -- \
        --skip test_chown::test_big_p \
        --skip test_chgrp::test_big_p \
        --skip test_chgrp::test_big_h \
        --skip test_chgrp::test_1 \
        --skip test_chgrp::test_fail_silently \
        --skip test_chgrp::test_preserve_root \
        --skip test_chgrp::test_preserve_root_symlink"
}

package() {
  cd $_pkgname-$pkgver
  make install \
    DESTDIR="$pkgdir" \
    PREFIX=/usr \
    MANDIR=/share/man/man1 \
    PROFILE=release
  # below algos implemented in hashsum, fix to keep compat with GNU Coreutils
  for algo in sha1 sha224 sha256 sha384 sha512 md5 b2 sha3{,-224,-256,-384,-512} shake{128,256}
  do
  ln -s "hashsum" "${pkgdir}/usr/bin/${algo}sum"
  done
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/uutils-coreutils/LICENSE"
}
