Summary:	Set of backgrounds for GNOME desktop
Summary(pl):	Zestaw tapet dla ¶rodowiska GNOME
Name:		gnome-backgrounds
Version:	2.13.91
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-backgrounds/2.13/%{name}-%{version}.tar.bz2
# Source0-md5:	3a9226649de2f5fe1465ee19611d60d1
URL:		http://www.gnome.org/
BuildRequires:	intltool >= 0.33
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for GNOME desktop.

%description -l pl
Zestaw tapet dla ¶rodowiska GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties
%{_pixmapsdir}/backgrounds
