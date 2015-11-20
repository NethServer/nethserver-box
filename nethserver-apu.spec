Summary: APU leds management
Name: nethserver-apu
Version: 1.0.2
Release: 1%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz

Requires: kmod-leds-apu

BuildRequires: perl, nethserver-devtools

%description
APU leds management

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
* Fri Nov 20 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1
- Limit clamd memory usage [NH:3965]

* Tue Nov 17 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- Fix fstrim command

* Mon Apr 13 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- Box APU: aggiunto supporto ai led e pulsante per spegnimento NH #3609

