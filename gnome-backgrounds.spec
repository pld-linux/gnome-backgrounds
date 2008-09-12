Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	2.23.92
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/2.23/%{name}-%{version}.tar.bz2
# Source0-md5:	c532820d4cabb5d2ba3406a18c70287d
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool >= 0.36.2
Requires:	libgnome >= 2.20.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for GNOME desktop.

%description -l pl.UTF-8
Zestaw tapet dla środowiska GNOME.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

[ -d $RPM_BUILD_ROOT%{_datadir}/locale/sr@latin ] || \
	mv -f $RPM_BUILD_ROOT%{_datadir}/locale/sr@{Latn,latin}
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties/*.xml
%{_pixmapsdir}/backgrounds/gnome/*
