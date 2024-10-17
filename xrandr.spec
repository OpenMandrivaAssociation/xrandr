Summary:	Primitive command line interface to RandR extension
Name:		xrandr
Version:	1.5.2
Release:	2
License:	MIT
Group:		System/X11
Url:		https://www.x.org/wiki/Projects/XRandR
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(xorg-macros)

%description
Xrandr is a command line application used to set the screen size,
orientation, reflection and/or the active display(s) using the RandR
extension.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

# (cg) NB Until we package nickle and cairo-5c (that works) kill this.
rm -f %{buildroot}/%{_bindir}/xkeystone

%files
%{_bindir}/xrandr
%doc %{_mandir}/man1/xrandr.1.*
