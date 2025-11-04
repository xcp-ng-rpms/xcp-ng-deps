Name:           xcp-ng-deps
Version:        8.99
Release:        0.ydi.11
Summary:        A meta package pulling all needed dependencies for XCP-ng
# License covers this spec file
License:        GPLv2
URL:            https://xcp-ng.org

BuildArch:      noarch

# core distro in addition to Alma's @core
Requires: xcp-ng-release
Requires: xcp-ng-release-config
Requires: almalinux-repos
Requires: bzip2
Requires: cronie-noanacron
%ifarch x86_64
Requires: grub2-efi-x64
Requires: grub2-efi-x64-modules
Requires: shim-x64
%endif
%ifarch aarch64
Requires: grub2-efi-aa64
Requires: grub2-efi-aa64-modules
%endif
Requires: rootfiles
Requires: smartmontools
Requires: usbutils
Requires: wget

# Additional niceties
Requires: bash-completion
Requires: cryptsetup
Requires: htop
Requires: iftop
Requires: less
Requires: lsof
Requires: man-db
Requires: openssh-clients
Requires: openssh-server
Requires: parted
Requires: screen
Requires: strace
Requires: systemtap-runtime
Requires: tcpdump
Requires: unzip
Requires: vim-minimal
Requires: zip

# deps that should live somewhere else
Requires: cifs-utils
Requires: iptables-services
Requires: iptables-utils
Requires: iptables-legacy
Requires: iscsi-initiator-utils
# surely not only host-installer using it?
Requires: chrony
Requires: efibootmgr

# # harware support
# Requires: aic94xx-firmware

# XAPI stack (some should instead be Req'd by other packages?)
Requires: blktap
Requires: guest-templates-json-data-linux
Requires: guest-templates-json-data-windows
Requires: guest-templates-json-data-other
Requires: mdadm
Requires: nfs-utils
Requires: rrdd-plugins
Requires: sm-cli
Requires: varstored
Requires: varstored-tools
Requires: xapi-core
Requires: xapi-nbd
Requires: xapi-tests
Requires: xcp-ng-pv-tools
Requires: xcp-ng-xapi-plugins
Requires: xcp-rrdd
Requires: xenopsd-cli
Requires: xo-lite
Requires: xsconsole

# # not yet built
# # XAPI chokes on nvidia GPUs without that package
# Requires: gpumon
# Requires: host-upgrade-plugin
# Requires: vcputune
# Requires: xcp-ng-plymouth-theme
# Requires: xen-crashdump-analyser
# Requires: xenserver-status-report
# Requires: xha

# # dropped from the list, possibly temporarily
# Requires: control-slice
# Requires: dracut-network
# Requires: expect
# Requires: fcoe-utils
# Requires: gdisk
# Requires: iproute-tc
# Requires: ipset
# Requires: irqbalance
# Requires: kexec-tools
# Requires: makedumpfile
# Requires: mcelog
# Requires: memtest86+
# Requires: nano
# Requires: net-snmp
# # Currently requires acpica-tools, also pulled by xenserver-status-report
# Requires: pmtools
# Requires: policycoreutils
# Requires: portmap
# Requires: pyserial
# Requires: redhat-lsb-core
# Requires: redhat-lsb-submod-security
# Requires: rsyslog
# Requires: samba-client
# Requires: samba-winbind-clients
# Requires: sharutils
# Requires: sudo
# Requires: sysfsutils
# Requires: system-config-firewall-tui
# Requires: telnet
# Requires: vconfig
# Requires: vendor-drivers
# Requires: vendor-update-keys
# Requires: vncsnapshot
# Requires: vncterm
# Requires: wsproxy
# Requires: xapi-storage-script
# Requires: xdelta
# Requires: xenserver-dracut
# Requires: xenserver-hwdata

# # Default provider of libverto-module-base in CentOS 7, to ensure
# # reproducibility of the nfs-utils -> gssproxy -> libverto-module-base
# # chain, which is too weak
# Requires: libverto-tevent

%description
This package has dependencies to all the packages that make a XCP-ng server.

Keep it installed to make sure that future updates will pull additional
packages needed by the newer version of XCP-ng.

%post
if [ $1 -gt 1 ]; then
    > %{_localstatedir}/lib/rpm-state/%{name}-%{version}-%{release}-update
fi

%posttrans
if [ -e %{_localstatedir}/lib/rpm-state/%{name}-%{version}-%{release}-update ]; then
    rm %{_localstatedir}/lib/rpm-state/%{name}-%{version}-%{release}-update
# XCP-ng 8.2: commented out, ough to be fixed upstream now
#    # Update from 8.0: fix systemd symlinks
#    # REVIEW ME NEXT UPGRADE SINCE CITRIX WILL HAVE FIXED IT DIFFERENTLY
#    systemctl enable vm.slice >/dev/null 2>&1 || :
#    systemctl enable sm-mpath-root.service >/dev/null 2>&1 || :
    # rsyslog.service symlink may be wrong
    LINK=$(readlink /etc/systemd/system/multi-user.target.wants/rsyslog.service)
    if [ "$LINK" == "/usr/lib/systemd/system/rsyslog.service" ]; then
        systemctl disable rsyslog >/dev/null 2>&1 || :
        systemctl enable rsyslog >/dev/null 2>&1 || :
    fi
fi

%files

%changelog
* Wed Jul 16 2025 Yann Dirson <yann.dirson@vates.tech> - 8.99-0.ydi.11
- Base for 9.0 based on Alma 10

* Thu Nov 28 2024 Benjamin Reis <benjamin.reis@vates.tech> - 8.3-13
- Require vim-minimal

* Fri Oct 25 2024 Yann Dirson <yann.dirson@vates.tech> - 8.3-12
- Require python2-xapi-storage not obsolete xapi-storage

* Mon Aug 12 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-11
- Obsolete unused package oprofile

* Tue Jul 09 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-10
- Remove dependency to gnu-free-sans-fonts, not required by anything anymore

* Fri Jul 05 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-9
- Remove dependency to fontconfig, which was cut from xcp-ng-plymouth-theme already

* Thu May 30 2024 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-8
- Don't require gfs2-utils, which isn't used in XCP-ng

* Mon Sep 18 2023 Yann Dirson <yann.dirson@vates.fr> - 8.3-7
- Add libverto-tevent as explicit require

* Thu Sep 14 2023 Thierry Escande <thierry.escande@vates.tech> - 8.3-6
- Requires xo-lite

* Thu Mar 16 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-5
- Remove dlm, dlm-lib, corosync and corosynclib
- We don't use XS's clustering feature which means we don't need them

* Wed Feb 15 2023 Yann Dirson <yann.dirson@vates.fr> - 8.3-4
- Requires grubby

* Thu Dec 08 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-3
- Remove and obsolete linux-guest-loader and linux-guest-loader-data

* Tue Oct 25 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-2
- Require varstored instead of uefistored

* Mon Sep 05 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.3-1
- Update to 8.3
- Remove the third digit from the version
- First batch of changes on Requires and Obsoletes
- Removing Requires and obsoleting: pbis-open, pbis-open-upgrade, sm-rawhba, vhostmd
- Removing Requires but already obsoleted elsewhere: microcode_ctl, rrd2csv
- Requires NOT added for xapi-rrd2csv as rrdd-plugins already requires it

* Tue Jan 18 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-12
- Remove dep to bugtool-conn-test, obsoleted by xenserver-status-report
- Remove dep to xenserver-transfer-vm, obsoleted by xcp-ng-deps itself

* Mon Dec 20 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-11
- Sync with CH 8.2.1: obsolete xenserver-transfer-vm

* Wed Nov 25 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-10
- Add dependency to varstored-tools
- Related to https://github.com/xcp-ng/xcp/issues/458

* Wed Nov 04 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-9
- Remove security-tools RPM, not used in our context

* Fri Aug 14 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-8
- Obsolete dummy xcp-ng-secureboot-certs, not required by varstored anymore
- Comment out part of posttrans systemd services enabling, should now be fixed

* Thu Aug 13 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-7
- Re-add dependency to gpumon now that we built a stub one

* Thu Aug 13 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-6
- Add dependency to uefistored

* Tue Jul 07 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-5
- Require security-tools and xapi-xe, since they are...
- ... not pulled by xenserver-firstboot anymore
- Require xenospd-cli, not pulled by anything else...
- ... (xenops-cli used to be pulled by xenopsd)

* Tue Jul 07 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-4
- Remove dependency to xs-openssl, it is only a build dep

* Mon Jul 06 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-3
- Remove dependency to varstored for 8.2 alpha

* Mon Jul 06 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-2
- Remove dependency to gpumon for 8.2 alpha

* Wed Jul 01 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.2.0-1
- Update for XCP-ng 8.2
- First update of deps, to be refined after tests
- Remove guest-templates-json-data-xenapp
- Remove ocaml-xenops-tools
- Remove and obsolete xenserver-firstboot
- Add iproute-tc
- Add xs-openssl
- Replace stunnel_xs with stunnel
- Replace gnupg with gnupg2

* Fri Apr 03 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-10
- Restore dependency to gpumon. XAPI chokes on nvidia gpus without it
- Don't enable the chronyd and chrony-wait services here anymore
- (It's now done as a triggerin in xcp-ng-release-config)

* Wed Mar 25 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-8
- Fix missing or wrong systemd symlinks after an update (CH upstream bug)
- Remove old POST script, not needed in 8.x anymore

* Tue Feb 04 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-6
- Obsolete gpumon to avoid upgrade failures

* Wed Jan 29 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-5
- Remove gpumon

* Mon Jan 20 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-4
- Re-add varstored and varstored-tools

* Tue Jan 14 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-3
- Do not obsolete autogen-libopts, we need it

* Mon Jan 13 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-2
- Temporarily remove dependency to varstored and varstored-tools

* Fri Dec 20 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.1.0-1
- Update for XCP-ng 8.1

* Thu Jun 27 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-6
- Add kpatch back
- See https://github.com/xcp-ng/xcp/issues/209

* Tue Jun 25 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-5
- Add yum-utils

* Mon Jun 03 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 8.0.0-4
- Add htop, iftop and cryptsetup

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
