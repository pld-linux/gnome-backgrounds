Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	3.34.0
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	f350804df16cdc9ef5306087157cf31b
URL:		https://www.gnome.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	meson >= 0.41.0
BuildRequires:	ninja >= 1.5
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Conflicts:	gtk2-theme-engine-adwaita < 3.14
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Set of backgrounds for GNOME desktop.

%description -l pl.UTF-8
Zestaw tapet dla środowiska GNOME.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING_CCBY* NEWS README
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/gnome
