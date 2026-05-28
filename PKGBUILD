# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
_dist=File-FnMatch
pkgname=perl-file-fnmatch
pkgver=0.02
pkgrel=1
pkgdesc="Perl module that provides simple filename and pathname matching"
arch=(x86_64 arm64)
url="https://metacpan.org/dist/File-FnMatch"
license=('Artistic-1.0-Perl OR GPL-1.0-or-later')
depends=(perl)
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/M/MJ/MJP/$_dist-$pkgver.tar.gz")
noextract=()
b2sums=('16701339747f9daf621bf2feb24a91ecb6df47d33093e6ff0aaebf35d472dab35d46e22cbb26f24b8effdfc257d159cd8680dfd7702c1a8714b39e48b9bf1244')
validpgpkeys=()

build() {
    cd $_dist-$pkgver

    unset PERL_MM_OPT PERL5LIB PERL_LOCAL_LIB_ROOT
    export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps

    /usr/bin/perl Makefile.PL NO_PACKLIST=1 NO_PERLLOCAL=1
    make
}

check() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    make test
}

package() {
    cd $_dist-$pkgver

    unset PERL5LIB PERL_LOCAL_LIB_ROOT

    make install INSTALLDIRS=vendor DESTDIR="$pkgdir"
}