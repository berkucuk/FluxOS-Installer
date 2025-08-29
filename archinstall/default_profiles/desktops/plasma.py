from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('FluxOS Desktop (KDE Plasma)', ProfileType.DesktopEnv)

	@property
	@override
	def packages(self) -> list[str]:
		return [
			# Core KDE Plasma packages (only KDE-specific)
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
			'konsole',
			'kate',
			'dolphin',
			'ark',
			# KDE-specific multimedia packages
			'qt5-webengine',
			'qt6-webengine',
			# KDE-specific graphics packages
			'xf86-video-amdgpu',
			'xf86-video-ati',
			'xf86-video-nouveau',
			'libva-mesa-driver',
			'libva-intel-driver',
			'intel-media-driver',
			'vulkan-radeon',
			'vulkan-nouveau',
			# KDE display manager
			'sddm',
			'kscreen',
			'sddm-kcm',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType:
		return GreeterType.Sddm
	
	@override
	def post_install(self, install_session) -> None:
		super().post_install(install_session)
		
		# KDE Plasma specific setup
		self._setup_kde_plasma(install_session)
	
	def _setup_kde_plasma(self, install_session) -> None:
		"""Setup KDE Plasma specific configurations"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up KDE Plasma specific configurations...')
			
			# Enable SDDM display manager
			info('Enabling SDDM display manager...')
			install_session.enable_service(['sddm'])
			
			# Copy FluxOS KDE configurations
			self._copy_fluxos_kde_configs(install_session)
			
			# Copy FluxOS SDDM themes
			self._copy_fluxos_sddm_themes(install_session)
			
			# Setup lock screen and power management
			self._setup_fluxos_power_and_lock(install_session)
			
			info('KDE Plasma setup completed successfully')
			
		except Exception as e:
			warn(f'Failed to setup KDE Plasma: {e}')
	
	def _copy_fluxos_kde_configs(self, install_session) -> None:
		"""Copy FluxOS KDE configuration files"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Copying FluxOS KDE configurations...')
			
			# Create KDE config directories
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.config')
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share')
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share/konsole')
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share/color-schemes')
			
			# Copy KDE configs from fluxos_config_files
			# Note: These paths need to be adjusted based on actual file locations
			config_source = '/fluxos_config_files/sddm_theme/kde_configs'
			
			# Copy KDE Plasma configurations
			SysCommand(f'cp -r {config_source}/.local/share/plasma /home/flux/.local/share/')
			
			# Copy Konsole configurations
			SysCommand(f'cp -r {config_source}/.local/share/konsole/* /home/flux/.local/share/konsole/')
			
			# Copy color schemes
			SysCommand(f'cp -r {config_source}/.local/share/color-schemes/* /home/flux/.local/share/color-schemes/')
			
			# Copy Konsole color schemes and profiles
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share/konsole')
			SysCommand(f'cp -r {config_source}/.local/share/konsole/* /home/flux/.local/share/konsole/')
			
			# Copy additional KDE config files
			SysCommand(f'cp -r {config_source}/.config/kglobalshortcutsrc /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/kwinrc /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/kdeglobals /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/plasmarc /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/plasmashellrc /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/konsolerc /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/kwinoutputconfig.json /home/flux/.config/')
			SysCommand(f'cp -r {config_source}/.config/plasma-org.kde.plasma.desktop-appletsrc /home/flux/.config/')
			
			# Setup dock configuration
			self._setup_fluxos_dock(install_session)
			
			# Set proper ownership
			SysCommand(f'arch-chroot {install_session.target} chown -R flux:flux /home/flux/.config')
			SysCommand(f'arch-chroot {install_session.target} chown -R flux:flux /home/flux/.local/share')
			
			info('FluxOS KDE configurations copied successfully')
			
		except Exception as e:
			warn(f'Failed to copy FluxOS KDE configs: {e}')
	
	def _setup_fluxos_dock(self, install_session) -> None:
		"""Setup FluxOS dock configuration using KDE config files"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS dock configuration...')
			
			# Create KDE config directories
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.config')
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share')
			
			# Copy KDE config files from fluxos_config_files
			config_source = '/fluxos_config_files/sddm_theme/kde_configs'
			
			# Copy KDE Plasma panel configuration
			if SysCommand(f'test -f {config_source}/.config/plasma-org.kde.plasma.desktop-appletsrc').exit_code == 0:
				SysCommand(f'cp {config_source}/.config/plasma-org.kde.plasma.desktop-appletsrc /home/flux/.config/')
				info('KDE Plasma panel config copied')
			else:
				# Create basic panel configuration if config doesn't exist
				self._create_basic_panel_config(install_session)
			
			# Copy KDE global shortcuts and favorites
			if SysCommand(f'test -f {config_source}/.config/kglobalshortcutsrc').exit_code == 0:
				SysCommand(f'cp {config_source}/.config/kglobalshortcutsrc /home/flux/.config/')
				info('KDE global shortcuts config copied')
			
			# Copy KDE application launcher favorites
			if SysCommand(f'test -f {config_source}/.config/kickoffrc').exit_code == 0:
				SysCommand(f'cp {config_source}/.config/kickoffrc /home/flux/.config/')
				info('KDE kickoff favorites config copied')
			
			# Set proper ownership
			SysCommand(f'arch-chroot {install_session.target} chown -R flux:flux /home/flux/.config')
			
			info('FluxOS dock configuration completed successfully')
			
		except Exception as e:
			warn(f'Failed to setup FluxOS dock: {e}')
	
	def _create_basic_panel_config(self, install_session) -> None:
		"""Create basic KDE Plasma panel configuration"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info
		
		# Create basic panel configuration
		panel_config = '''[Containments][1]
activityId=
formfactor=2
immutability=1
lastScreen=0
location=3
plugin=org.kde.plasma.panel
wallpaperplugin=org.kde.image

[Containments][1][Applets][1]
immutability=1
plugin=org.kde.plasma.kickoff

[Containments][1][Applets][2]
immutability=1
plugin=org.kde.plasma.panelspacer

[Containments][1][Applets][3]
immutability=1
plugin=org.kde.plasma.icontasks

[Containments][1][Applets][4]
immutability=1
plugin=org.kde.plasma.panelspacer

[Containments][1][Applets][5]
immutability=1
plugin=org.kde.plasma.systemtray

[Containments][1][Applets][6]
immutability=1
plugin=org.kde.plasma.digitalclock
'''
		
		SysCommand(f'arch-chroot {install_session.target} echo "{panel_config}" > /home/flux/.config/plasma-org.kde.plasma.desktop-appletsrc')
		
		# Create kickoff favorites configuration
		kickoff_config = '''[Favorites]
favorites=firefox,protonvpn-gui,fluxai-chat,konsole,dolphin
'''
		
		SysCommand(f'arch-chroot {install_session.target} echo "{kickoff_config}" > /home/flux/.config/kickoffrc')
		
		info('Basic KDE Plasma panel configuration created')
	
	def _copy_fluxos_sddm_themes(self, install_session) -> None:
		"""Copy FluxOS SDDM themes"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Copying FluxOS SDDM themes...')
			
			# Copy FluxOS SDDM themes
			theme_source = '/fluxos_config_files/sddm_theme'
			
			# Copy fluxos-breeze theme
			SysCommand(f'cp -r {theme_source}/fluxos-breeze /usr/share/sddm/themes/')
			
			# Copy fluxai-chat theme
			SysCommand(f'cp -r {theme_source}/fluxai-chat /usr/share/sddm/themes/')
			
			# Copy images
			SysCommand(f'cp -r {theme_source}/images /usr/share/sddm/themes/')
			
			# Set SDDM theme to fluxos-breeze
			SysCommand(f'arch-chroot {install_session.target} echo "Current=fluxos-breeze" >> /etc/sddm.conf')
			
			info('FluxOS SDDM themes copied successfully')
			
		except Exception as e:
			warn(f'Failed to copy FluxOS SDDM themes: {e}')
	
	def _setup_fluxos_power_and_lock(self, install_session) -> None:
		"""Setup FluxOS power management and lock screen"""
		from archinstall.lib.general import SysCommand
		from archinstall.lib.output import info, warn
		
		try:
			info('Setting up FluxOS power management and lock screen...')
			
			# Enable power-profiles-daemon service
			install_session.enable_service(['power-profiles-daemon'])
			
			# Copy lock screen background
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /usr/share/sddm/themes/fluxos-breeze/Backgrounds')
			SysCommand(f'cp /fluxos_config_files/sddm_theme/images/fluxos-wallpaper.png /usr/share/sddm/themes/fluxos-breeze/Backgrounds/')
			
			# Update fluxos-breeze theme configuration
			theme_conf = '''[General]
background=Backgrounds/fluxos-wallpaper.png
type=image
color=#1e1e1e
fontColor=#ffffff
needsFullUserModel=false
'''
			SysCommand(f'arch-chroot {install_session.target} echo "{theme_conf}" > /usr/share/sddm/themes/fluxos-breeze/theme.conf')
			
			# Setup power profiles daemon configuration
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /etc/power-profiles-daemon')
			power_conf = '''[daemon]
default-profile=balanced
'''
			SysCommand(f'arch-chroot {install_session.target} echo "{power_conf}" > /etc/power-profiles-daemon/rules.d/00-default.conf')
			
			# Copy lock screen background to KDE Plasma
			SysCommand(f'arch-chroot {install_session.target} mkdir -p /home/flux/.local/share/plasma/wallpapers')
			SysCommand(f'cp /fluxos_config_files/sddm_theme/images/fluxos-wallpaper.png /home/flux/.local/share/plasma/wallpapers/')
			
			# Set proper ownership
			SysCommand(f'arch-chroot {install_session.target} chown -R flux:flux /home/flux/.local/share/plasma')
			
			info('FluxOS power management and lock screen setup completed successfully')
			
		except Exception as e:
			warn(f'Failed to setup FluxOS power and lock screen: {e}')
