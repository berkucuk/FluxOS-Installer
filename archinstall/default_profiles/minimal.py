from archinstall.default_profiles.profile import Profile, ProfileType


class MinimalProfile(Profile):
	def __init__(self) -> None:
		super().__init__(
			'Minimal',
			ProfileType.Minimal,
		)

	@property
	def packages(self) -> list[str]:
		return [
			# Core system packages
			'base',
			'linux',
			'linux-firmware',
			'base-devel',
			'linux-headers',
			# Essential tools
			'nano',
			'vim',
			'openssh',
			'htop',
			'wget',
			'git',
			# Network
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
			# Additional packages from releng/packages.x86_64
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
