Name:           xcp-ng-deps
Version:        7.5.0
Release:        2
Summary:        A meta package pulling all needed dependencies for XCP-ng
# License covers this spec file
License:        GPLv2
URL:            https://xcp-ng.org

BuildArch:      noarch

# Unversioned requires, sorted alphabetically
# Extracted from groups.xml
Requires: QCS-CLI
Requires: QConvergeConsoleCLI-Citrix
Requires: aic94xx-firmware
Requires: bash-completion
Requires: blktap
Requires: bugtool-conn-tests
Requires: bzip2
Requires: cifs-utils
Requires: compat-db47
Requires: compat-libstdc++-33
Requires: control-slice
Requires: conversion-plugin
Requires: cronie-noanacron
Requires: dlm
Requires: dracut-network
Requires: e2fsprogs
Requires: efibootmgr
Requires: elxocmcore
Requires: expect
Requires: fcoe-utils
Requires: fontconfig
Requires: gdisk
Requires: gfs2-utils
Requires: gnu-free-sans-fonts
Requires: gnupg
Requires: gpumon
Requires: grub
Requires: grub-efi
Requires: guest-templates-json-data-linux
Requires: guest-templates-json-data-other
Requires: guest-templates-json-data-windows
Requires: guest-templates-json-data-xenapp
Requires: host-upgrade-plugin
Requires: interface-rename
Requires: ipmitool
Requires: ipset
Requires: irqbalance
Requires: iscsi-initiator-utils
Requires: kbd
Requires: kexec-tools
Requires: libempserver
Requires: linux-firmware
Requires: linux-guest-loader
Requires: linux-guest-loader-data
Requires: livepatch-utils
Requires: lsof
Requires: makedumpfile
Requires: mcelog
Requires: mdadm
Requires: memtest86+
Requires: microcode_ctl
Requires: module-init-tools
Requires: nano
Requires: net-snmp
Requires: nfs-utils
Requires: ntp
Requires: ocaml-xenops-tools
Requires: openssh-clients
Requires: openssh-server
Requires: openssl-perl
Requires: openvswitch
Requires: oprofile
Requires: parted
Requires: pbis-open
Requires: plymouth
Requires: plymouth-graphics-libs
Requires: plymouth-plugin-script
Requires: pmtools
Requires: policycoreutils
Requires: portmap
Requires: pyserial
Requires: python-fasteners
Requires: redhat-lsb-core
Requires: redhat-lsb-submod-security
Requires: rootfiles
Requires: rrd2csv
Requires: rrdd-plugins
Requires: rsync
Requires: rsyslog
Requires: samba-client
Requires: samba-winbind-clients
Requires: screen
Requires: sharutils
Requires: sm
Requires: sm-cli
Requires: sm-rawhba
Requires: smartmontools
Requires: squeezed
Requires: strace
Requires: stunnel_xs
Requires: sudo
Requires: sysfsutils
Requires: sysstat
Requires: system-config-firewall-tui
Requires: systemd-networkd
Requires: systemtap-runtime
Requires: tcpdump
Requires: telnet
Requires: unzip
Requires: usbutils
Requires: vconfig
Requires: vcputune
Requires: vendor-drivers
Requires: vendor-update-keys
Requires: vhd-tool
Requires: vhostmd
Requires: vncsnapshot
Requires: vncterm
Requires: wget
Requires: wsproxy
Requires: xapi-nbd
Requires: xapi-storage
Requires: xapi-storage-script
Requires: xapi-tests
Requires: xcp-featured
Requires: xcp-networkd
Requires: xcp-ng-center
Requires: xcp-ng-plymouth-theme
Requires: xcp-ng-pv-tools
Requires: xcp-ng-release
Requires: xcp-ng-release-config
Requires: xcp-ng-updater
Requires: xcp-python-libs-xenserver
Requires: xcp-rrdd
Requires: xdelta
Requires: xen-crashdump-analyser
Requires: xen-device-model
Requires: xengt-modules
Requires: xenopsd-xc
Requires: xenopsd-xenlight
Requires: xenserver-dracut
Requires: xenserver-firstboot
Requires: xenserver-hwdata
Requires: xenserver-status-report
Requires: xenserver-transfer-vm
Requires: xha
Requires: xsconsole
Requires: yum
Requires: zip

%description
This package has dependencies to all the packages that make a XCP-ng server.

Keep it installed to make sure that future updates will pull additional
packages needed by the newer version of XCP-ng.

%files

%changelog
* Wed Jul 25 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.5.0-1
- Initial package
