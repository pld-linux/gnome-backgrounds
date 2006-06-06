Summary:	Set of backgrounds for GNOME desktop
Summary(pl):	Zestaw tapet dla ¶rodowiska GNOME
Name:		gnome-backgrounds
Version:	2.14.2.1
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/gnome/sources/gnome-backgrounds/2.14/%{name}-%{version}.tar.bz2
# Source0-md5:	10480df7c2e5a08c920c5b0a2ff4f161
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties
%{_pixmapsdir}/backgrounds
