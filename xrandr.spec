Summary:	Primitive command line interface to RandR extension
Name:		xrandr
Version:	1.4.2
Release:	2
License:	MIT
Group:		System/X11
Url:		http://www.x.org/wiki/Projects/XRandR
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xrandr) >= 1.1.0.2
BuildRequires:	pkgconfig(xrender) >= 0.9.0.2
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xrandr is a command line application used to set the screen size,
orientation, reflection and/or the active display(s) using the RandR
extension.

%prep
%setup -q
%build
%configure2_5x \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

# (cg) NB Until we package nickle and cairo-5c (that works) kill this.
rm -f %{buildroot}/%{_bindir}/xkeystone

%files
%{_bindir}/xrandr
#%%{_bindir}/xkeystone
%{_mandir}/man1/xrandr.1.*

