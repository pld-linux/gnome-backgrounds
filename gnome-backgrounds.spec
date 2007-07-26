Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	2.18.3
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-backgrounds/2.18/%{name}-%{version}.tar.bz2
# Source0-md5:	d91b925d358d2cbc705b4a033e7d5c2e
URL:		http://www.gnome.org/
BuildRequires:	intltool >= 0.35.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for GNOME desktop.

%description -l pl.UTF-8
Zestaw tapet dla środowiska GNOME.

%prep
%setup -q

%build
%configure
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
%{_datadir}/gnome-background-properties
%{_pixmapsdir}/backgrounds
