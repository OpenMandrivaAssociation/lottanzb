Summary: LottaNZB - Automated Usenet Client
Name: lottanzb
Version: 0.5.3
Release: %mkrel 1
Source0: http://launchpad.net/lottanzb/0.5/%{version}/+download/%{name}-%{version}.tar.gz
License: GPL
Group: Networking/News
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: pygtk2.0-devel
BuildRequires: python-kiwi
BuildRequires: intltool
Requires: python-kiwi
Requires: python
Requires: hellanzb
Requires: pygtk2.0
Requires: pygtk2.0-libglade
Url: http://www.lottanzb.org/

%description
LottaNZB is a Usenet client that automates the download of Usenet files with the help of NZB files. It uses HellaNZB as its backend and PyGTK for its user interface.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome
for omf in %buildroot%_datadir/omf/*/*[_-]??.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name.lang
done

rm -fr %buildroot%{_datadir}/mime %buildroot%{_datadir}/doc
%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_desktop_database}
%{update_mime_database}
%update_icon_cache hicolor
%update_scrollkeeper

%postun
%{clean_desktop_database}
%{clean_mime_database}
%clean_icon_cache hicolor
%clean_scrollkeeper

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/apport/crashdb.conf.d/lottanzb-crashdb.conf
%{_datadir}/apport
%{_bindir}/*
%{py_puresitedir}/%{name}/*
%{_datadir}/%{name}/*
%{_datadir}/icons/*
%{py_puresitedir}/%{name}-%{version}-*.egg-info
%{_mandir}/man1/*
%{_datadir}/application-registry/lottanzb.applications
%{_datadir}/applications/lottanzb.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/*
%dir %{_datadir}/omf/lottanzb/
%{_datadir}/omf/lottanzb/*-C.omf
