Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	3.28.0
Release:	1
License:	GPL v2
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-backgrounds/3.28/%{name}-%{version}.tar.xz
# Source0-md5:	eca3276373841a0cec2ed582d52a5899
URL:		http://www.gnome.org/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel
BuildRequires:	meson >= 0.41.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/gnome
