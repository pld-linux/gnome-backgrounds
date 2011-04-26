Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	3.0.1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	8d82e0103a258e3e37f7d01e4761927a
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	intltool >= 0.40.0
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
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties/*.xml
%{_datadir}/backgrounds/gnome
