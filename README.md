# 🚀 FluxOS Installer

**FluxOS için özelleştirilmiş kurulum sihirbazı** - Modern, kullanıcı dostu ve Türkçe destekli Linux dağıtım kurulum aracı.

FluxOS Installer, Arch Linux tabanlı FluxOS dağıtımını kolayca kurmanızı sağlayan gelişmiş bir kurulum aracıdır. Hem etkileşimli kurulum sihirbazı hem de programlanabilir Python kütüphanesi olarak çalışır.

## ✨ Özellikler

### 🎯 **FluxOS'a Özel Tasarım**
* **Tam FluxOS desteği** - Özelleştirilmiş paket koleksiyonu
* **Türkçe arayüz** - Yerli kullanıcılar için optimize edilmiş
* **Modern UI** - Kullanıcı dostu kurulum deneyimi
* **Otomatik yapılandırma** - FluxOS branding ve tema desteği

### 🛠️ **Gelişmiş Özelleştirme**
* **6 Kurulum Profili:**
  * 🎮 **Gaming** - Oyun odaklı sistem
  * 💻 **Developer** - Geliştirici araçları
  * 🔒 **Security** - Güvenlik odaklı
  * 📄 **Office** - Ofis uygulamaları
  * 🏠 **Default** - Standart masaüstü
  * ⚡ **Minimal** - Temel sistem

## 🚀 Kurulum ve Kullanım

### 📋 Gereksinimler
* **UEFI sistem** (Legacy BIOS sınırlı destek)
* **En az 2GB RAM** (8GB önerilen)
* **En az 20GB disk alanı** (50GB önerilen)
* **İnternet bağlantısı** (paket indirme için)

### 💻 FluxOS Installer Kurulumu

#### 1. **FluxOS Live USB'den Kurulum** (Önerilen)
```shell
sudo ./fluxos-install
```

#### 2. **Git ile Manuel Kurulum**
```shell
git clone https://github.com/berkucuk/FluxOS-Installer.git
cd FluxOS-Installer
sudo python -m archinstall
```

#### 3. **Pip ile Kurulum**
```shell
pip install --upgrade git+https://github.com/berkucuk/FluxOS-Installer.git
sudo fluxos-install
```

### 🛠️ **Kurulum Adımları**

#### 1. **Kurulum Türünü Seçin**
* 🌟 **FluxOS Kurulum Sihirbazı** (Önerilen)
* ⚙️ **Klasik Archinstall**

#### 2. **Profilinizi Seçin**
* Kullanım amacınıza uygun profili seçin
* Özel paket seçimleri yapabilirsiniz

#### 3. **Sistem Yapılandırması**
* Disk bölümlendirme
* Kullanıcı hesabı oluşturma
* Ağ yapılandırması
* Bootloader kurulumu

### 📁 **Konfigürasyon Dosyası ile Kurulum**

FluxOS Installer JSON konfigürasyon dosyaları ile çalıştırılabilir:
* `user_configuration.json` - Genel kurulum ayarları
* `user_credentials.json` - Kullanıcı şifreleri ve hassas bilgiler

**İpucu:** Konfigürasyon dosyaları FluxOS Installer'ı çalıştırıp "Konfigürasyonu Kaydet" seçeneği ile otomatik oluşturulabilir.

```shell
sudo python -m archinstall --config <config_dosyası> --creds <credentials_dosyası>
```

### Credentials configuration file encryption
By default all user account credentials are hashed with `yescrypt` and only the hash is stored in the saved `user_credentials.json` file.
This is not possible for disk encryption password which needs to be stored in plaintext to be able to apply it.

However, when selecting to save configuration files, `archinstall` will prompt for the option to encrypt the `user_credentials.json` file content.
A prompt will require to enter a encryption password to encrypt the file. When providing an encrypted `user_configuration.json` as a argument with `--creds <user_credentials.json>`
there are multiple ways to provide the decryption key:
* Provide the decryption key via the command line argument `--creds-decryption-key <password>`
* Store the encryption key in the environment variable `ARCHINSTALL_CREDS_DECRYPTION_KEY` which will be read automatically
* If none of the above is provided a prompt will be shown to enter the decryption key manually


# 🆘 Yardım ve Destek

FluxOS Installer ile ilgili sorunlarınız için aşağıdaki kanalları kullanabilirsiniz:

* **GitHub Issues:** [FluxOS-Installer Issues](https://github.com/berkucuk/FluxOS-Installer/issues)
* **FluxOS Website:** https://fluxos.com.tr
* **E-posta:** support@fluxos.com.tr

## Hata Bildirimi

Hata bildirirken lütfen şunları ekleyin:
* Hata mesajının tam çıktısı (stacktrace)
* `/var/log/archinstall/install.log` dosyasını issue'ya ekleyin
* FluxOS Installer versiyonu
* Sistem bilgileri (RAM, disk, UEFI/BIOS)

**Log dosyasını paylaşmak için:**
```shell
curl -F'file=@/var/log/archinstall/install.log' https://0x0.st
```


# 🌍 Dil Desteği

FluxOS Installer birden fazla dilde kullanılabilir. Dil seçimi kurulum sırasında ilk menüden yapılabilir.

## Desteklenen Diller
* **🇹🇷 Türkçe** - Ana dil (Tam destek)
* **🇺🇸 English** - İngilizce (Tam destek)
* **🇩🇪 Deutsch** - Almanca
* **🇫🇷 Français** - Fransızca
* **🇪🇸 Español** - İspanyolca
* **Ve diğer birçok dil...**

**Not:** Türkçe ve İngilizce dışındaki diller topluluk katkılarıyla çevrilmiştir ve tam çeviri içermeyebilir.

## Fonts
The ISO does not ship with all fonts needed for different languages.
Fonts that use a different character set than Latin will not be displayed correctly. If those languages
want to be selected then a proper font has to be set manually in the console.

All available console fonts can be found in `/usr/share/kbd/consolefonts` and set with `setfont LatGrkCyr-8x16`.


# Scripting your own installation

## Scripting interactive installation

For an example of a fully scripted, interactive installation please refer to the example
[interactive_installation.py](https://github.com/archlinux/archinstall/blob/master/archinstall/scripts/guided.py)


> **To create your own ISO with this script in it:** Follow [ArchISO](https://wiki.archlinux.org/index.php/archiso)'s guide on creating your own ISO.

## Script non-interactive automated installation

For an example of a fully scripted, automated installation please refer to the example
[full_automated_installation.py](https://github.com/archlinux/archinstall/blob/master/examples/full_automated_installation.py)

## Unattended installation based on MAC address

Archinstall comes with an [unattended](https://github.com/archlinux/archinstall/blob/master/examples/mac_address_installation.py)
example which will look for a matching profile for the machine it is being run on, based on any local MAC address.
For instance, if the machine the code is executed on has the MAC address `52:54:00:12:34:56` it will look for a profile called
[52-54-00-12-34-56.py](https://github.com/archlinux/archinstall/blob/master/archinstall/default_profiles/tailored.py).
If it's found, the unattended installation will begin and source that profile as its installation procedure.

# 🎯 FluxOS Kurulum Profilleri

FluxOS Installer, farklı kullanım senaryoları için önceden yapılandırılmış profiller sunar:

## 🎮 **Gaming Profile**
- Steam, Lutris, GameMode
- NVIDIA/AMD oyun optimizasyonları
- Discord, TeamSpeak
- Performans araçları

## 💻 **Developer Profile**  
- Visual Studio Code, Jetbrains araçları
- Docker, Git, Node.js, Python
- Geliştirici terminal araçları
- Veritabanı istemcileri

## 🔒 **Security Profile**
- VPN araçları (OpenVPN, WireGuard)
- Güvenlik tarayıcıları
- Şifreleme araçları
- Güvenlik duvarı yapılandırması

## 📄 **Office Profile**
- LibreOffice paketi
- PDF araçları
- E-posta istemcileri
- Multimedya uygulamaları

## 🏠 **Default Profile**
- Standart masaüstü deneyimi
- Temel uygulamalar
- Web tarayıcısı
- Sistem araçları

## ⚡ **Minimal Profile**
- Sadece temel sistem
- Minimal masaüstü
- Düşük kaynak kullanımı


# Testing

## Using a Live ISO Image

If you want to test a commit, branch, or bleeding edge release from the repository using the standard Arch Linux Live ISO image,
replace the archinstall version with a newer one and execute the subsequent steps defined below.

*Note: When booting from a live USB, the space on the ramdisk is limited and may not be sufficient to allow
running a re-installation or upgrade of the installer. In case one runs into this issue, any of the following can be used
- Resize the root partition https://wiki.archlinux.org/title/Archiso#Adjusting_the_size_of_the_root_file_system
- The boot parameter `copytoram=y` (https://gitlab.archlinux.org/archlinux/mkinitcpio/mkinitcpio-archiso/-/blob/master/docs/README.bootparams#L26)
can be specified which will copy the root filesystem to tmpfs.*

1. You need a working network connection
2. Install the build requirements with `pacman -Sy; pacman -S git python-pip gcc pkgconf`
   *(note that this may or may not work depending on your RAM and current state of the squashfs maximum filesystem free space)*
3. Uninstall the previous version of archinstall with `pip uninstall --break-system-packages archinstall`
4. Now clone the latest repository with `git clone https://github.com/archlinux/archinstall`
5. Enter the repository with `cd archinstall`
   *At this stage, you can choose to check out a feature branch for instance with `git checkout v2.3.1-rc1`*
6. To run the source code, there are 2 different options:
   - Run a specific branch version from source directly using `python -m archinstall`, in most cases this will work just fine, the
      rare case it will not work is if the source has introduced any new dependencies that are not installed yet
   - Installing the branch version with `pip install --break-system-packages .` and `archinstall`

## Without a Live ISO Image

To test this without a live ISO, the simplest approach is to use a local image and create a loop device.<br>
This can be done by installing `pacman -S arch-install-scripts util-linux` locally and doing the following:

    # truncate -s 20G testimage.img
    # losetup --partscan --show --find ./testimage.img
    # pip install --upgrade archinstall
    # python -m archinstall --script guided
    # qemu-system-x86_64 -enable-kvm -machine q35,accel=kvm -device intel-iommu -cpu host -m 4096 -boot order=d -drive file=./testimage.img,format=raw -drive if=pflash,format=raw,readonly,file=/usr/share/ovmf/x64/OVMF.4m.fd -drive if=pflash,format=raw,readonly,file=/usr/share/ovmf/x64/OVMF.4m.fd 

This will create a *20 GB* `testimage.img` and create a loop device which we can use to format and install to.<br>
`archinstall` is installed and executed in [guided mode](#docs-todo). Once the installation is complete, ~~you can use qemu/kvm to boot the test media.~~<br>
*(You'd actually need to do some EFI magic in order to point the EFI vars to the partition 0 in the test medium, so this won't work entirely out of the box, but that gives you a general idea of what we're going for here)*

There's also a [Building and Testing](https://github.com/archlinux/archinstall/wiki/Building-and-Testing) guide.<br>
It will go through everything from packaging, building and running *(with qemu)* the installer against a dev branch.


# FAQ

## Keyring out-of-date
For a description of the problem see https://archinstall.archlinux.page/help/known_issues.html#keyring-is-out-of-date-2213 and discussion in issue https://github.com/archlinux/archinstall/issues/2213.

For a quick fix the below command will install the latest keyrings

```pacman -Sy archlinux-keyring```

## How to dual boot with Windows

To install Arch Linux alongside an existing Windows installation using  `archinstall`, follow these steps:

1. Ensure some unallocated space is available for the Linux installation after the Windows installation.
2. Boot into the ISO and run `archinstall`.
3. Choose `Disk configuration` -> `Manual partitioning`.
4. Select the disk on which Windows resides.
5. Select `Create a new partition`.
6. Choose a filesystem type.
7. Determine the start and end sectors for the new partition location (values can be suffixed with various units).
8. Assign the mountpoint `/` to the new partition.
9. Assign the `Boot/ESP` partition the mountpoint `/boot` from the partitioning menu.
10. Confirm your settings and exit to the main menu by choosing `Confirm and exit`.
11. Modify any additional settings for your installation as necessary.
12. Start the installation upon completion of setup.


# 🎯 Misyon

FluxOS Installer, **basit, güvenli ve kullanıcı dostu** bir Linux kurulum deneyimi sunmayı amaçlar. Projemizin temel hedefleri:

## 🌟 **Vizyon**
* **Herkes için Linux** - Teknik bilgi gerektirmeden kolay kurulum
* **Türkçe öncelik** - Yerli kullanıcılar için optimize edilmiş arayüz
* **Modern tasarım** - Güncel UI/UX standartları
* **Topluluk odaklı** - Açık kaynak geliştirme

## 🛠️ **Teknik Felsefe**
* Arch Linux prensiplerini takip eder
* Modüler ve genişletilebilir yapı
* Geriye uyumluluk garantisi
* Kapsamlı test coverage

---

FluxOS Installer hem **kurulum sihirbazı** hem de **Python kütüphanesi** olarak çalışır. Bu sayede hem son kullanıcılar hem de geliştiriciler için esneklik sağlar.

# 🤝 Katkıda Bulunun

FluxOS Installer açık kaynak bir projedir ve topluluk katkılarını memnuniyetle karşılar!

## 🐛 **Hata Bildirimi**
1. [GitHub Issues](https://github.com/berkucuk/FluxOS-Installer/issues) sayfasını ziyaret edin
2. Ayrıntılı hata açıklaması yapın
3. Log dosyalarını ekleyin
4. Sistem bilgilerinizi paylaşın

## 💡 **Özellik İsteği**
* Yeni profil önerileri
* Paket ekleme istekleri
* UI/UX iyileştirmeleri
* Çeviri katkıları

## 👨‍💻 **Kod Katkısı**
1. Repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b yeni-ozellik`)
3. Değişikliklerinizi commit edin
4. Push edin (`git push origin yeni-ozellik`)
5. Pull Request oluşturun

---

### 💫 FluxOS ile Geleceği Keşfedin
**Modern • Güvenli • Türkçe • Açık Kaynak**
