from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, Profile, ProfileType, SelectResult
from archinstall.lib.output import info
from archinstall.lib.profile.profiles_handler import profile_handler
from archinstall.tui.curses_menu import SelectMenu
from archinstall.tui.menu_item import MenuItem, MenuItemGroup
from archinstall.tui.result import ResultType
from archinstall.tui.types import FrameProperties, PreviewStyle

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class DesktopProfile(Profile):
	def __init__(self, current_selection: list[Profile] = []) -> None:
		super().__init__(
			'Desktop',
			ProfileType.Desktop,
			current_selection=current_selection,
			support_greeter=True,
		)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			# Core system packages
			'nano',
			'vim',
			'openssh',
			'htop',
			'wget',
			'iwd',
			'wireless_tools',
			'wpa_supplicant',
			'smartmontools',
			'xdg-utils',
			# FluxOS Core packages (for all desktop environments)
			'base-devel',
			'linux-headers',
			'git',
			# Internet & Communication
			'firefox',
			'torbrowser-launcher',
			'thunderbird',
			'discord',
			'filezilla',
			# Privacy & Security
			'onionshare',
			'nyx', 
			'openvpn',
			'wireguard-tools',
			'stunnel',
			'proton-vpn-gtk-app',
			# Antivirus & Security Tools
			'clamav',
			'clamtk',
			'rkhunter',
			'lynis',
			'fail2ban',
			'aircrack-ng',
			# Firewall & Network
			'firewalld',
			'network-manager-applet',
			'systemd-resolvconf',
			'openbsd-netcat',
			# Office & Productivity
			'libreoffice-fresh',
			# System Monitoring & Performance
			'btop',
			'htop',
			'iotop',
			'nethogs',
			'powertop',
			'lm_sensors',
			'xsensors',
			'acpi',
			'smartmontools',
			'ethtool',
			# Hardware Support
			'sof-firmware',
			'acpid',
			'thermald',
			'power-profiles-daemon',
			'fprintd',
			# System Utilities
			'partitionmanager',
			'isoimagewriter',
			'unzip',
			'dialog',
			'bash-completion',
			'pacman-contrib',
			# Virtualization
			'virt-manager',
			'vde2',
			'dnsmasq',
			'bridge-utils',
			'edk2-ovmf',
			# Multimedia
			'ffmpeg',
			# Graphics & Display
			'mesa-utils',
			'mesa-demos',
			'vulkan-icd-loader',
			'vulkan-intel',
			'vulkan-tools',
			'xorg-xev',
			'xorg-xmodmap',
			# Fonts
			'ttf-nerd-fonts-symbols',
			'nerd-fonts',
			# Package Management
			'flatpak',
			'fuse2',
			# Development Tools
			'gtkmm',
			'ncurses',
			'libcanberra',
			'pcsclite',
			'gcc',
			'make',
			'libaio',
			'python-pip',
			'python-setuptools',
			# System Services
			'dbus-broker',
			'irqbalance',
			'earlyoom',
			'chrony',
			'zram-generator',
			# Connectivity
			'kdeconnect',
			# Shell & Terminal
			'zsh',
			# Utilities
			'spectacle',
			'okular',
			'gwenview',
			'kwalletmanager',
			# Additional FluxOS packages
			'power-profiles-daemon',
			'firewalld',
			'ufw',
			'iptables',
			'ebtables',
			'protonvpn-cli',
			'protonvpn-gui',
			# Additional packages from releng/packages.x86_64
			'alsa-utils',
			'amd-ucode',
			'arch-install-scripts',
			'b43-fwcutter',
			'bcachefs-tools',
			'bind',
			'bolt',
			'brltty',
			'broadcom-wl',
			'btrfs-progs',
			'clonezilla',
			'cloud-init',
			'cryptsetup',
			'darkhttpd',
			'ddrescue',
			'diffutils',
			'dmidecode',
			'dmraid',
			'dosfstools',
			'edk2-shell',
			'espeakup',
			'exfatprogs',
			'f2fs-tools',
			'fatresize',
			'foot-terminfo',
			'fsarchiver',
			'gpart',
			'gpm',
			'gptfdisk',
			'grml-zsh-config',
			'hdparm',
			'hyperv',
			'intel-ucode',
			'irssi',
			'jfsutils',
			'kitty-terminfo',
			'ldns',
			'lftp',
			'libfido2',
			'libusb-compat',
			'linux-atm',
			'lsscsi',
			'lvm2',
			'lynx',
			'mc',
			'mdadm',
			'memtest86+',
			'memtest86+-efi',
			'mkinitcpio-archiso',
			'mkinitcpio-nfs-utils',
			'mmc-utils',
			'modemmanager',
			'mtools',
			'nbd',
			'ndisc6',
			'nfs-utils',
			'nilfs-utils',
			'nmap',
			'ntfs-3g',
			'nvme-cli',
			'open-iscsi',
			'open-vm-tools',
			'openconnect',
			'openpgp-card-tools',
			'partclone',
			'partimage',
			'ppp',
			'pptpclient',
			'pv',
			'qemu-guest-agent',
			'reflector',
			'rxvt-unicode-terminfo',
			'screen',
			'sdparm',
			'sequoia-sq',
			'sg3_utils',
			'squashfs-tools',
			'syslinux',
			'tcpdump',
			'terminus-font',
			'testdisk',
			'tpm2-tools',
			'tpm2-tss',
			'udftools',
			'usb_modeswitch',
			'usbmuxd',
			'virtualbox-guest-utils-nox',
			'vpnc',
			'wireless-regdb',
			'wvdial',
			'xfsprogs',
			'xl2tpd',
			# KDE Desktop - Basic Plasma
			'plasma-desktop',
			'plasma-workspace',
			'plasma-workspace-wallpapers',
			'plasma-nm',
			'plasma-pa',
			'plasma-vault',
			'plasma-disks',
			'plasma-systemmonitor',
			'plasma-firewall',
			# KDE Applets için gerekli
			'kdeplasma-addons',
			'sddm',
			'dolphin',
			'konsole',
			'kate',
			'ark',
			'breeze-gtk',
			'ttf-roboto',
			'ttf-fira-code',
			'awesome-terminal-fonts',
			# KDE Display & Graphics
			'kde-gtk-config',
			# KDE Settings & Control
			'systemsettings',
			# X11 Display & Resolution
			'xorg-server',
			'xf86-video-vesa',
			'xkeyboard-config',
			'kbd',
			'xorg-setxkbmap',
			'xorg-xkbcomp',
			'xorg-xrandr',
			'xorg-xdpyinfo',
			'xorg-xset',
			'xorg-xsetroot',
			'xorg-xprop',
			'xorg-xwininfo',
			'xorg-xdriinfo',
			'xorg-xgamma',
			'xorg-xrefresh',
			'xorg-xinput',
			# Network & Bluetooth
			'networkmanager',
			'bluez',
			'bluez-utils',
			# System services
			'acpid',
			'dbus-broker',
			'irqbalance',
			'pacman-contrib',
			# Graphics & Multimedia
			'vulkan-tools',
			'mesa-demos',
			'mesa-utils',
			'qt6-webengine',
			'network-manager-applet',
			'partitionmanager',
			'isoimagewriter',
			# Hardware monitoring
			'lm_sensors',
			'xsensors',
			'spice-vdagent',
			'xf86-video-qxl',
			# Development & Runtime
			'python-virtualenv',
			'libpng',
			'pipewire-pulse',
			# Explicit providers to avoid pacman prompts
			'iptables-nft',
			'pipewire-jack',
			'qt6-multimedia-ffmpeg',
			'cronie',
			# Runtime dependencies
			'polkit',
			'libpwquality',
			'ca-certificates',
			'python-pyparted',
			'python-pydantic',
			'sof-firmware',
			'earlyoom',
			'chrony',
			'ncurses',
			'python',
			'vulkan-icd-loader',
			# Additional tools
			'unrar',
			'koko',
			'noise-suppression-for-voice',
			'apparmor',
			'audit',
			'gimp',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType | None:
		combined_greeters: dict[GreeterType, int] = {}
		for profile in self.current_selection:
			if profile.default_greeter_type:
				combined_greeters.setdefault(profile.default_greeter_type, 0)
				combined_greeters[profile.default_greeter_type] += 1

		if len(combined_greeters) >= 1:
			return list(combined_greeters)[0]

		return None

	def _do_on_select_profiles(self) -> None:
		for profile in self.current_selection:
			profile.do_on_select()

	@override
	def do_on_select(self) -> SelectResult:
		items = [
			MenuItem(
				p.name,
				value=p,
				preview_action=lambda x: x.value.preview_text(),
			)
			for p in profile_handler.get_desktop_profiles()
		]

		group = MenuItemGroup(items, sort_items=True, sort_case_sensitive=False)
		group.set_selected_by_value(self.current_selection)

		result = SelectMenu[Profile](
			group,
			multi=True,
			allow_reset=True,
			allow_skip=True,
			preview_style=PreviewStyle.RIGHT,
			preview_size='auto',
			preview_frame=FrameProperties.max('Info'),
		).run()

		match result.type_:
			case ResultType.Selection:
				self.current_selection = result.get_values()
				self._do_on_select_profiles()
				return SelectResult.NewSelection
			case ResultType.Skip:
				return SelectResult.SameSelection
			case ResultType.Reset:
				return SelectResult.ResetCurrent

	@override
	def post_install(self, install_session: 'Installer') -> None:
		# Install FluxAI chat application and basic FluxOS setup for all desktop environments
		self._setup_fluxos_basics(install_session)
		
		# Call post_install for selected desktop profiles
		for profile in self.current_selection:
			profile.post_install(install_session)
	
	def _setup_fluxos_basics(self, install_session) -> None:
		"""Setup basic FluxOS components for all desktop environments"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS basic components...')
			
			# Setup FluxOS swap (20GB swapfile)
			self._setup_fluxos_swap(install_session)
			
			# Setup firewall rules and enable firewalld
			self._setup_fluxos_firewall(install_session)
			
			# Setup desktop shortcuts and dock
			self._setup_fluxos_desktop(install_session)
			
			# Enable and start essential services for FluxOS
			services_to_enable = [
				'firewalld',
				'clamav-daemon', 
				'NetworkManager',
				'acpid',
				'dbus-broker',
				'irqbalance',
				'earlyoom',
				'chrony',
				'thermald',
				'power-profiles-daemon',
				'fail2ban',
			]
			install_session.enable_service(services_to_enable)
			
			info('FluxOS basic components setup completed successfully')
			
		except Exception as e:
			warn(f'Failed to setup FluxOS basic components: {e}')
	
	def _setup_fluxos_firewall(self, install_session) -> None:
		"""Setup FluxOS firewall rules and enable firewalld"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS firewall rules...')
			
			# Enable firewalld service
			install_session.enable_service(['firewalld'])
			
			# Start firewalld to configure rules
			SysCommand(f'arch-chroot {install_session.target} systemctl start firewalld')
			
			# Set default zone to public
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --set-default-zone=public')
			
			# Allow essential services
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-service=ssh')
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-service=dhcpv6-client')
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-service=mdns')
			
			# Allow specific ports
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-port=53/udp')
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-port=53/tcp')
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --permanent --add-port=5353/udp')
			
			# Enable firewalld shield (emergency mode)
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --set-default-zone=drop')
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --set-default-zone=public')
			
			# Reload firewall rules
			SysCommand(f'arch-chroot {install_session.target} firewall-cmd --reload')
			
			info('FluxOS firewall rules configured successfully')
			
		except Exception as e:
			warn(f'Failed to setup FluxOS firewall: {e}')
	
	def _setup_fluxos_swap(self, install_session) -> None:
		"""Setup FluxOS 20GB swap file"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS 20GB swap file...')
			
			# Create 20GB swap file in larger chunks to improve performance
			# Use 4GB chunks instead of 1GB to reduce I/O operations
			info('Creating 20GB swap file in 4GB chunks...')
			
			# Create empty file first
			SysCommand(f'arch-chroot {install_session.target} touch /swapfile')
			
			# Fill file in 4GB chunks to balance memory usage and performance
			# This reduces the number of I/O operations from 20 to 5
			for i in range(5):
				SysCommand(f'arch-chroot {install_session.target} dd if=/dev/zero of=/swapfile bs=4G count=1 oflag=append conv=notrunc')
				info(f'Swap file progress: {(i+1)*4}GB / 20GB')
			
			# Set proper permissions
			SysCommand(f'arch-chroot {install_session.target} chmod 600 /swapfile')
			
			# Make it swap
			SysCommand(f'arch-chroot {install_session.target} mkswap /swapfile')
			
			# Add to fstab
			SysCommand(f'arch-chroot {install_session.target} echo "/swapfile none swap defaults 0 0" >> /etc/fstab')
			
			info('FluxOS 20GB swap file created successfully')
			
		except Exception as e:
			warn(f'Failed to create FluxOS swap file: {e}')
			# Fallback to zram
			try:
				info('Falling back to zram swap...')
				install_session.setup_swap('zram')
				info('Fallback: Using zram for swap')
			except Exception as zram_e:
				warn(f'Failed to setup zram swap: {zram_e}')
				# Final fallback: create smaller swap file
				try:
					info('Trying to create smaller swap file (4GB)...')
					SysCommand(f'arch-chroot {install_session.target} dd if=/dev/zero of=/swapfile bs=4G count=1')
					SysCommand(f'arch-chroot {install_session.target} chmod 600 /swapfile')
					SysCommand(f'arch-chroot {install_session.target} mkswap /swapfile')
					SysCommand(f'arch-chroot {install_session.target} echo "/swapfile none swap defaults 0 0" >> /etc/fstab')
					info('4GB swap file created as final fallback')
				except Exception as final_e:
								warn(f'All swap setup methods failed: {final_e}')
			warn('No swap configured - system may run out of memory under heavy load')
	
	def _setup_fluxos_desktop(self, install_session) -> None:
		"""Setup FluxOS dock configuration using KDE config files"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS dock configuration...')
			
			# Create KDE config directories
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.config')
			
			# Copy KDE config files from fluxos_config_files if available
			config_source = '/fluxos_config_files/sddm_theme/kde_configs'
			
			if SysCommand(f'test -d {config_source}').exit_code == 0:
				# Copy KDE Plasma panel configuration
				if SysCommand(f'test -f {config_source}/.config/plasma-org.kde.plasma.desktop-appletsrc').exit_code == 0:
					SysCommand(f'cp {config_source}/.config/plasma-org.kde.plasma.desktop-appletsrc /home/flux/.config/')
					info('KDE Plasma panel config copied')
				
				# Copy KDE kickoff favorites configuration
				if SysCommand(f'test -f {config_source}/.config/kickoffrc').exit_code == 0:
					SysCommand(f'cp {config_source}/.config/kickoffrc /home/flux/.config/')
					info('KDE kickoff favorites config copied')
			else:
				# Create basic configuration if config files don't exist
				self._create_basic_kde_config(install_session)
			
			# Set proper ownership
			SysCommand(f'arch-chroot {install_session.target} chown -R flux:flux /home/flux/.config')
			
			info('FluxOS dock configuration completed successfully')
			
		except Exception as e:
			warn(f'Failed to setup FluxOS dock: {e}')
	
	def _create_basic_kde_config(self, install_session) -> None:
		"""Create basic KDE configuration for dock"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info
		
		# Create kickoff favorites configuration
		kickoff_config = '''[Favorites]
favorites=firefox,protonvpn-gui,fluxai-chat,konsole,dolphin

[General]
favoritesPortedToKAstats=true
'''
		
		SysCommand(f'arch-chroot {install_session.target} echo "{kickoff_config}" > /home/flux/.config/kickoffrc')
		
		info('Basic KDE configuration created')

	@override
	def install(self, install_session: 'Installer') -> None:
		# Install common packages for all desktop environments
		install_session.add_additional_packages(self.packages)

		for profile in self.current_selection:
			info(f'Installing profile {profile.name}...')

			install_session.add_additional_packages(profile.packages)
			install_session.enable_service(profile.services)

			profile.install(install_session)
