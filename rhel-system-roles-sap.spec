# avoiding version conflict, set version 0.7.1 for rhel7
%define upstream_vesion 2019-09-30_18-11-12

Name: rhel-system-roles-sap
Summary: System Role prepares a RHEL system for running SAP software for SAP HANA
Version: 0.7.2
Release: 3%{?dist}
License: GPLv3+
Url: https://github.com/berndfinger
Source0: https://than.fedorapeople.org/rhel/%{name}-%{upstream_vesion}.tar.gz
BuildArch: noarch
Requires: uuidd

%description
Collection of Ansible roles which configures a RHEL system according
to applicable SAP notes so that any SAP software can be installed.

%prep
%setup -q -T -c -n %{name}-%{version} -a 0

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/ansible/roles \
         $RPM_BUILD_ROOT%{_pkgdocdir}/sap-hana-preconfigure \
         $RPM_BUILD_ROOT%{_pkgdocdir}/sap-preconfigure \
         $RPM_BUILD_ROOT%{_pkgdocdir}/sap-netweaver-preconfigure

# drop zero file
rm -f */.gitignore sap-hana-preconfigure/tasks/RedHat_6/recommendations.yml

cp -pR sap-hana-preconfigure sap-preconfigure sap-netweaver-preconfigure $RPM_BUILD_ROOT%{_datadir}/ansible/roles/
cp -p sap-hana-preconfigure/{README.md,LICENSE} $RPM_BUILD_ROOT%{_pkgdocdir}/sap-hana-preconfigure/
cp -p sap-preconfigure/{README.md,LICENSE} $RPM_BUILD_ROOT%{_pkgdocdir}/sap-preconfigure/
cp -p sap-netweaver-preconfigure/{README.md,LICENSE} $RPM_BUILD_ROOT%{_pkgdocdir}/sap-netweaver-preconfigure/

%files
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/sap-preconfigure
%dir %{_pkgdocdir}/sap-hana-preconfigure
%dir %{_pkgdocdir}/sap-netweaver-preconfigure
%dir %{_datadir}/ansible
%dir %{_datadir}/ansible/roles
%doc %{_pkgdocdir}/*/README.md
%license %{_pkgdocdir}/*/LICENSE
%{_datadir}/ansible/roles/*

%changelog
* Mon Oct 07 2019 Than Ngo <than@redhat.com> - 0.7.2-3
- own some directories

* Mon Oct 07 2019 Than Ngo <than@redhat.com> - 0.7.2-2
- drop requirement on rhel-system-roles

* Tue Oct 01 2019 Than Ngo <than@redhat.com> - 0.7.2-1
- rebase to 0.7.2 (upstream-version 2019-09-30_18-11-12)

* Fri Sep 13 2019 Than Ngo <than@redhat.com> - 0.7.1-1
- rebase to 0.7.1 (upstream-version 2019-09-12)

* Fri Aug 09 2019 Than Ngo <than@redhat.com> - 0.7-1
- Initial release.
