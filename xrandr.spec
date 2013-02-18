Name:		xrandr
Version:	1.4.0
Release:	1
Summary:	Primitive command line interface to RandR extension
Group:		System/X11
URL:		http://www.x.org/wiki/Projects/XRandR
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxrandr-devel >= 1.1.0.2
BuildRequires:	libxrender-devel >= 0.9.0.2
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
#%{_bindir}/xkeystone
%{_mandir}/man1/xrandr.1.*


%changelog
* Fri 16 2012 akdengi <akdengi> 1.3.5-2.20120910.1
- update to git snapshot of 20120910 for provider interfaces support (PRIME multi-gpu support)

* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.5-1mdv2012.0
+ Revision: 699279
- update to new version 1.3.5

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2
+ Revision: 671360
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 591820
- new release

* Sun Jul 25 2010 Thierry Vignaud <tv@mandriva.org> 1.3.3-1mdv2011.0
+ Revision: 558360
- new release

  + Paulo Ricardo Zanoni <pzanoni@mandriva.com>
    - Remove French xrandr manpage (it is already provided by man-pages-fr)

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-2mdv2010.1
+ Revision: 524464
- rebuilt for 2010.1

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 436635
- new release

* Tue Aug 11 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 415105
- new release

* Wed Apr 01 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-1mdv2009.1
+ Revision: 363389
- New version 1.3.0

* Sun Feb 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.2.99.4-1mdv2009.1
+ Revision: 336169
- update to new version 1.2.99.4

* Thu Jan 01 2009 Colin Guthrie <cguthrie@mandriva.org> 1.2.99.3-2mdv2009.1
+ Revision: 323201
- Update French man page (thanks to Bernard Siaud alias Troumad)

* Mon Dec 15 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.99.3-1mdv2009.1
+ Revision: 314619
- New version: 1.2.99.3

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-2mdv2009.0
+ Revision: 266150
- rebuild early 2009.0 package (before pixel changes)

  + Funda Wang <fwang@mandriva.org>
    - mark lang property

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.2.3-1mdv2009.0
+ Revision: 193008
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.2-2mdv2008.1
+ Revision: 154359
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 05 2007 Colin Guthrie <cguthrie@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 48476
- New upstream version 1.2.2

* Thu Jun 21 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-2mdv2008.0
+ Revision: 42324
- fix/improve group: s/development/system/

* Thu Jun 21 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.1-1mdv2008.0
+ Revision: 42315
- new upstream version: 1.2.1

  + Colin Guthrie <cguthrie@mandriva.org>
    - Update package description

* Thu May 24 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.2.0-2mdv2008.0
+ Revision: 30793
- add french manpage, translation from Bernard Siaud <liste at siaud.org>
  (closes: #30999)
- fix group owner of manpages (now root:man)


* Wed Feb 28 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.2.0-1mdv2007.0
+ Revision: 127069
- new upstream release supporting the version 1.2 of the RandR X extension
- rebuild to fix cooker uploading
- X11R7.1
- increment release
- Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fill in a couple of missing descriptions

