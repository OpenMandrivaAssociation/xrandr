Name: xrandr
Version: 1.2.2
Release: %mkrel 1
Summary: Primitive command line interface to RandR extension
Group: System/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1: http://troumad.info/Linux/xrandr.1.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxrandr-devel >= 1.1.0.2
BuildRequires: libxrender-devel >= 0.9.0.2
BuildRequires: x11-util-macros >= 1.0.1

%description
Xrandr is a command line application used to set the screen size,
orientation, reflection and/or the active display(s) using the RandR
extension.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/fr/man1/
install -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/fr/man1/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xrandr
%defattr(-,root,man)
%{_mandir}/man1/xrandr.1.*
%{_mandir}/fr/man1/xrandr.1.*


