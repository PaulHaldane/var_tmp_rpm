%global debug_package %{nil}

Name: var_tmp
Summary: var_tmp demo of folder permission breakage
Version: 1.0
Release: 1
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL
# BuildArch: noarch

%description
Dummy test

%prep

%setup -q -c -T

%build

%install
install -m 770 -d %{buildroot}/var/tmp

%clean

%files
%defattr(-,root,root)
%dir /var/tmp

%changelog
* Wed Jun 14 2017 Paul Haldane <Paul.Haldane@gmail.com>
- dummy
