from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import ProfileType
from archinstall.default_profiles.xorg import XorgProfile

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class TailoredProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('52-54-00-12-34-56', ProfileType.Tailored)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			'nano', 
			'wget', 
			'git',
			# Essential system packages
			'base',
			'linux',
			'linux-firmware',
			'base-devel',
			'linux-headers',
			'vim',
			'openssh',
			'htop',
			# Network tools
			'iwd',
			'wireless_tools',
			'wpa_supplicant',
			'dhcpcd',
			'networkmanager',
			# System utilities
			'sudo',
			'grub',
			'efibootmgr',
			'mkinitcpio',
			# Additional tools from releng/packages.x86_64
			'arch-install-scripts',
			'cryptsetup',
			'dosfstools',
			'e2fsprogs',
			'gptfdisk',
			'parted',
			'rsync',
			'zsh',
			'bash-completion',
			'ncurses',
			'less',
			'man-db',
			'man-pages',
		]

	@override
	def install(self, install_session: 'Installer') -> None:
		super().install(install_session)
		# do whatever you like here :)
