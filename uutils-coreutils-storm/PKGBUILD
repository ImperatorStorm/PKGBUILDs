# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
# Contributor: Sam <dev at samarthj dot com>
# Contributor: Árni Dagur <arnidg@protonmail.ch>

# shellcheck disable=2034,2148,2154

pkgname="uutils-coreutils-storm"
pkgver=r6379.2e251f91f
pkgrel=1
pkgdesc="GNU Coreutils rewritten in Rust"
arch=('x86_64')
url='https://github.com/uutils/coreutils'
license=('MIT')
depends=('glibc' 'gcc-libs')
makedepends=('git' 'rust' 'cargo' 'cmake' 'python-sphinx')
conflicts=('uutils-coreutils-git' 'coreutils')
provides=('coreutils')
source=("uutils::git+https://github.com/uutils/coreutils.git#commit=db22b15faf164190627f05eb52eb3539524bb378")
sha256sums=('SKIP')
options=(!lto)

pkgver() {
  cd ${srcdir}/uutils || exit 1
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd ${srcdir}/uutils || exit 1
  make PROFILE=release
}

check() {
  cd ${srcdir}/uutils || exit 1
   make test \
      PROFILE=release \
      CARGOFLAGS=--release \
      TEST_NO_FAIL_FAST="--no-fail-fast -- \
        --skip test_chown::test_big_p \
        --skip test_chgrp::test_big_p \
        --skip test_chgrp::test_big_h"
}

package() {
  cd ${srcdir}/uutils || exit 1
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