Name:           xcp-ng-deps
Version:        8.0.0
Release:        3
Summary:        A meta package pulling all needed dependencies for XCP-ng
# License covers this spec file
License:        GPLv2
URL:            https://xcp-ng.org

BuildArch:      noarch

# Unversioned requires, sorted alphabetically
# Extracted from groups.xml
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
Requires: htop
Requires: interface-rename
Requires: ipmitool
Requires: ipset
Requires: iptables
Requires: irqbalance
Requires: iscsi-initiator-utils
Requires: kbd
Requires: kexec-tools
Requires: libempserver
Requires: linux-firmware
Requires: linux-guest-loader
Requires: linux-guest-loader-data
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
Requires: systemtap-runtime
Requires: tcpdump
Requires: telnet
Requires: unzip
Requires: usbutils
Requires: varstored
Requires: varstored-tools
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
Requires: xcp-ng-plymouth-theme
Requires: xcp-ng-pv-tools
Requires: xcp-ng-release
Requires: xcp-ng-release-config
Requires: xcp-ng-xapi-plugins
Requires: xcp-rrdd
Requires: xdelta
Requires: xen-crashdump-analyser
Requires: xenopsd-xc
Requires: xenserver-dracut
Requires: xenserver-firstboot
Requires: xenserver-hwdata
Requires: xenserver-status-report
Requires: xenserver-transfer-vm
Requires: xha
Requires: xsconsole
Requires: yum
Requires: zip

Requires(post): sed

# Obsolete package to be removed during upgrade to 7.5 or higher
Obsoletes: vgpu < 7.3.3

# Obsolete packages to be removed during upgrade to 7.6 or higher
Obsoletes: livepatch-utils <= 1.1.0-1
Obsoletes: sm-transport-lib < 0.11.0
Obsoletes: xapi-clusterd < 0.26.0
Obsoletes: xapi-storage-plugins < 1.23.0

# Obsolete packages to be removed during upgrade to 8.0 or higher
Obsoletes: xen-device-model <= 0.10.3
Obsoletes: xengt-modules <= 4.0.0
Obsoletes: xenopsd-xenlight <= 0.66.0
Obsoletes: xcp-ng-center < 8.0
Obsoletes: systemd-networkd < 219-20

%description
This package has dependencies to all the packages that make a XCP-ng server.

Keep it installed to make sure that future updates will pull additional
packages needed by the newer version of XCP-ng.

%post
if [ $1 -gt 1 ]; then
    if [ -f /etc/sysconfig/dlm ]; then
        # Remove line wrongly added by xapi-storage-plugins to /etc/sysconfig/dlm in 7.5
        # In XS fixing this is handled by the scriptlets in xapi-storage-plugins RPM
        # But in 7.6 it has become proprietary so we have to do it ourselves here.
        sed -i /etc/sysconfig/dlm -e '/^@DLM_CONFIG@/ d'
    fi
fi

%files

%changelog
* Mon Jun 03 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-4
- Add htop

* Mon Jun 03 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-3
- Renamed xcp-ng-updater to xcp-ng-xapi-plugins

* Thu May 02 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-2
- Update for XCP-ng 8.0.0
- Added iptables, varstored and varstored-tools to Requires
- Removed xen-device-model, xengt-modules, xenopsd-xenlight and xcp-ng-center from Requires
- Removed systemd-networkd from Requires
- Obsoleted those packages

* Wed Oct 03 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.6.0-4
- Don't obsolete QLogic and Emulex packages, so that it's still
  possible to install them from the vendors' sites.

* Thu Sep 20 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.6.0-2
- Obsolete packages to be removed during upgrade to 7.6 or higher

* Fri Sep 14 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.6.0-1
- Update for XCP-ng 7.6.0, work in progress

* Wed Jul 25 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.5.0-1
- Initial package
