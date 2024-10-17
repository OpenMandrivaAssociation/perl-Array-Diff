%define upstream_name    Array-Diff
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	This module do diff two arrays, and return added and deleted arrays 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Algorithm::Diff)
BuildArch:	noarch

%description
This module do diff two arrays, and return added and deleted arrays. It's
simple usage of Algorithm::Diff.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 656881
- rebuild for updated spec-helper

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 595073
- update to new version 0.07

* Sun Jul 12 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.20-1mdv2011.0
+ Revision: 395062
- fix wrong macro name
- update to 0.05002
- using %%perl_convert_version
- fixed license field

* Fri Oct 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 296956
- update to new version 0.05

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.04-2mdv2009.0
+ Revision: 289435
- restore the spec file

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.04-1mdv2008.1
+ Revision: 136658
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.04-1mdv2008.0
+ Revision: 21928
- Fix BuildRequires
- fix BuildRequires
- Import perl-Array-Diff



* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.04-1mdv2008.0
- First Mandriva package
