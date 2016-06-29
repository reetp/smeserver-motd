%define name smeserver-motd
%define version 0.1
%define release 4
Summary: Adjust the login motd display
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: http://libreswan.org/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
Patch1: smeserver-motd-addstatuskey.patch
BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-release >= 8.0
AutoReqProv: no

%description
A small contribution to give a more informative display on ssh login

%changelog
* Wed Jun 29 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-4.sme
- Add db status key

* Tue Jun 28 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1-3.sme
- Initial release to contribs9

* Mon Jun 27 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- Initial build

* Mon Jun 27 2016 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-2
- Fix a typo in the spec file

%prep
%setup
%patch1 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre

%preun

%post

%postun
