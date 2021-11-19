# Maintainer: lgm <lgm dot aur at outlook dot com>
# Contributor: Ndoskrnl <lollipop.studio.cn@gmail.com>

# Based on the 'forge-server' AUR package by:
# Maintainer: Nitroretro <nitroretro@protonmail.com>

# Based on the `minecraft-server` AUR package by:
## Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
## Contributor: Philip Abernethy <chais.z3r0@gmail.com>
## Contributor: sowieso <sowieso@dukun.de>

_ver="1.17.1_0.9.0-2"
_minecraft_ver_latest="1.17.1"

IFS="-" read -ra _ver_temp <<< "$_ver"
IFS="_" read -ra _pkgver_temp <<< "${_ver_temp[0]}"

_minecraft_ver=${_pkgver_temp[0]}
_fabric_ver=${_pkgver_temp[1]}

_pkgver=${_ver_temp[0]//_/-}

if [ "$_minecraft_ver" = "$_minecraft_ver_latest" ]; then
	pkgname="fabric-server"
	_fabric_name="fabric"
else
	pkgname="fabric-server-${_minecraft_ver}"
	_fabric_name="fabric-${_minecraft_ver}"
fi
pkgver=${_ver_temp[0]}
pkgrel=${_ver_temp[1]}
pkgdesc="Minecraft Fabric server unit files, script and jar"
arch=("any")
url="https://fabricmc.net"
license=("Apache")
depends=("java-runtime-headless>=16" "tmux" "sudo" "bash" "awk" "sed")
optdepends=("tar: needed in order to create world backups"
	"netcat: required in order to suspend an idle server")
provides=("fabric-server=${pkgver}")
backup=("etc/conf.d/${_fabric_name}")
install="fabric-server.install"
source=("fabricd-backup.service"
	"fabricd-backup.timer"
	"fabricd.service"
	"fabricd.sysusers"
	"fabricd.tmpfiles"
	"fabricd.conf"
	"fabricd.sh")
noextract=("fabric-${_pkgver}.jar")
sha512sums=('38642e2cbd218221a93996b86cdb1bf1b1d3c78a377ea22b32c597ce5e4a2e6cb2b4541179d9b4dff6e4c463e60f4bdee101538c58bf455aeb85c73838b6ed2c'
            '755d3f532913f999c3abde1eae8a713f5bee8e758314fdeef0a70f81d4411b91b4c88d30824cdf5b0f8f5dae76ceffc10d2b1e5db6161a1daf02a50399b718d3'
            '78e688805d448be6a0d05cc4aa7bf728c5b662a1f8c335e5a1bab3a5af42de186585761d2b52cf77c97b474780b410fd8f8539052532235285242f71d295abfc'
            'dc1f355d0be1aa6b9941cb50be6543656f7b1dd03582ef760f830ecae723de168281d6a96fcc37920b3226a1e8542225c61b4348852521db5847d8821ef48a39'
            '5c1bcd2e0298d0200bfd3ec4996510e8fc04ac62f0a688bd6ef4cf0c92d6b1c545406fe8cbc447148f1dbaf4fb1e5cbf4c2636c0c088d127a54356d98552beed'
            '4270d2d85902b76df6de5f8e3b908748ff582919734ca835bb9ed4bf957e3127dc758c9247f4bbb8842fa0d4a30983105e84aeb7623e2bc1cf528cc955685b8d'
            'ee04c7e30cedbc724975973bba144b6f0137f66f1d2bd2f132d59e09990e7fa7817dda9eedcdaeb961cef0ce3f728a0727fec3c590ce6abd9b93ef6467a4587f'
            '80b5e7c571676e3489185df140d638bd8d12eebfcddedccd2dc469f6ee0522a0992354ac3411b2356a93d6b2f10ec706209d862d85ae84a02faf8e8761f6846b')

# -- Fabric Installer -- #
source+=("fabric-installer-${_fabric_ver}.jar"::"https://maven.fabricmc.net/net/fabricmc/fabric-installer/${_fabric_ver}/fabric-installer-${_fabric_ver}.jar")
# -- /Fabric Installer -- #

prepare() {
	java -Duser.home="${srcdir}" -jar "fabric-installer-${_fabric_ver}.jar" server -mcversion ${_minecraft_ver} -downloadMinecraft
}

package() {
	_server_root="${pkgdir}/srv/${_fabric_name}"
	_game="fabric"
	# Install fabricd
	install -Dm644 "${_game}d-backup.service" "${pkgdir}/usr/lib/systemd/system/${_fabric_name}d-backup.service"
	install -Dm644 "${_game}d-backup.timer" "${pkgdir}/usr/lib/systemd/system/${_fabric_name}d-backup.timer"
	install -Dm644 "${_game}d.service" "${pkgdir}/usr/lib/systemd/system/${_fabric_name}d.service"
	install -Dm644 "${_game}d.conf" "${pkgdir}/etc/conf.d/${_fabric_name}"
	install -Dm755 "${_game}d.sh" "${pkgdir}/usr/bin/${_fabric_name}d"

	install -Dm644 ${_game}d.sysusers          "${pkgdir}/usr/lib/sysusers.d/${_fabric_name}d.conf"
	install -Dm644 ${_game}d.tmpfiles          "${pkgdir}/usr/lib/tmpfiles.d/${_fabric_name}d.conf"

	# Install Fabric
	install -Dm644 "fabric-server-launch.jar" "${_server_root}/fabric-server-launch.jar"

	# Install Minecraft Server
	install -Dm644 "server.jar" "${_server_root}/server.jar"

	# Link log files
	mkdir -p "${pkgdir}/var/log/"
	install -dm2755 "${_server_root}/logs"
	ln -s "/srv/${_fabric_name}/logs" "${pkgdir}/var/log/${_fabric_name}"

	# Give the group write permissions and set user or group ID on execution
	chmod g+ws "${_server_root}"
}
