Summary:	Set of backgrounds for GNOME desktop
Summary(pl.UTF-8):	Zestaw tapet dla środowiska GNOME
Name:		gnome-backgrounds
Version:	42.0
Release:	1
License:	CC-BY-SA v3.0
Group:		Themes
Source0:	https://download.gnome.org/sources/gnome-backgrounds/42/%{name}-%{version}.tar.xz
# Source0-md5:	e41d94de9350123d17752860b2c595a8
URL:		https://www.gnome.org/
BuildRequires:	meson >= 0.50.0
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md
%{_datadir}/gnome-background-properties
%{_datadir}/backgrounds/gnome
