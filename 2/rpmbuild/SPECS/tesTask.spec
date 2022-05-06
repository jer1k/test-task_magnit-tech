Name:           tesTask
Version:	1.0 
Release:        1%{?dist}
Summary:	Test task for Magnit Tech

License:        none
URL:            none
Source0:        %{_sourcedir}/%{name}-%{version}.tar.gz

Requires: python
#Requires: PyYAML.x86_64

%description
Try to create RPM package

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1


%install
rm -rf $RPM_BUILD_ROOT
install -Dpm 0755 %{name}-%{version}/run.py %{buildroot}%{_bindir}/test-task
install -Dpm 0644 %{name}-%{version}/config.json %{buildroot}%{_sysconfdir}/%{name}/config.json


%files
/usr/bin/test-task
/etc/tesTask/config.json

%changelog
* Wed May  4 2022 Cherepanov Sergey
- First rpm-build expirience
