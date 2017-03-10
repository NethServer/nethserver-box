Summary: Nethesis box optimizations
Name: nethserver-box
Version: 2.0.3
Release: 1%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz

Requires: kmod-leds-apu2

BuildRequires: perl, nethserver-devtools

%description
Nethesis box optimizations

%prep
%setup

%build
perl createlinks

%post

%preun


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)

%changelog
* Fri Mar 10 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.3-1
- Handle old bios revision for APU2

* Fri Feb 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.2-1
- Shutdown the system after system-init

* Fri Feb 24 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.1-1
- Move leds action on top of system-init

* Thu Feb 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 2.0.0-1
- First release for NS 7

