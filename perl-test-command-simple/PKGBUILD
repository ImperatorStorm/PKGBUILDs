# Maintainer: Imperator Storm <ImperatorStorm11@protonmail.com>
_dist=Test-Command-Simple
pkgname=perl-test-command-simple
pkgver=0.05
pkgrel=1
pkgdesc="Perl module that provides simple filename and pathname matching"
arch=(any)
url="https://metacpan.org/dist/Test-Command-Simple"
license=('Artistic-1.0-Perl OR GPL-1.0-or-later')
depends=(perl)
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/D/DM/DMCBRIDE/$_dist-$pkgver.tar.gz")
noextract=()
b2sums=('74258f3e00a550fdcdbb755a37b12141b4e1342501d6af4c79d6c35616def30bb648cb45a4299c024fdf535d3351bae74dab8b9a09e0b442b80c8f5eb3b08130')
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
