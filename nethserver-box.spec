Summary: Nethesis box optimizations
Name: nethserver-box
Version: 2.0.8
Release: 1%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz

BuildRequires: perl, nethserver-devtools

%description
Nethesis box optimizations

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%dir %{_nseventsdir}/%{name}-update
%defattr(-,root,root)

%changelog
* Thu Aug 02 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.8-1
- Box: ethernet down at boot - Nethesis/dev#5442

* Wed Jun 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.7-1
- Box S60: panic at boot with kernel-3.10.0-862.3.3.el7.x86_64 - Bug nethesis/dev#5417

* Fri Apr 20 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.6-1
- FS trim: use systemd timer

* Fri Nov 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.5-1
- Box: missing network configuration after first boot - Nethesis/dev#5253

* Mon May 22 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.4-1
- Disable and remove standard clamav signatures - Nethesis/dev#5136

* Fri Mar 10 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.3-1
- Handle old bios revision for APU2

* Fri Feb 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.2-1
- Shutdown the system after system-init

* Fri Feb 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- Move leds action on top of system-init

* Thu Feb 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0-1
- First release for NS 7

