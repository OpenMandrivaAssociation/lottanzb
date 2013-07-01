Summary:	- Automated Usenet Client
Name:		lottanzb
Version:	0.5.3
Release:	3
License:	GPL
Group:		Networking/News
Url:		http://www.lottanzb.org/
Source0:	http://launchpad.net/lottanzb/0.5/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-kiwi
BuildRequires:	intltool
Requires:	python-kiwi
Requires:	python
Requires:	hellanzb
Requires:	pygtk2.0
Requires:	pygtk2.0-libglade
BuildArch:	noarch

%description
LottaNZB is a Usenet client that automates the download of 
Usenet files with the help of NZB files. It uses HellaNZB as
its backend and PyGTK for its user interface.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --packaging-mode --root=%{buildroot}

%find_lang %{name} --with-gnome

rm -fr %{buildroot}%{_datadir}/doc

%files -f %{name}.lang
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

