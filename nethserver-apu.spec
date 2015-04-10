Summary: APU leds management
Name: nethserver-apu
Version: 0.0.1
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
