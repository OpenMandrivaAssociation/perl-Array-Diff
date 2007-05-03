%define realname   Array-Diff
%define rel 1
Name:		perl-%{realname}
Version:    0.04
Release:    %mkrel %rel
License:	Artistic or GPL
Group:		Development/Perl
Summary:    This module do diff two arrays, and return added and deleted arrays 
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/Array-Diff-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Algorithm::Diff)
BuildArch: noarch

%description
This module do diff two arrays, and return added and deleted arrays. 
It's simple usage of Algorithm::Diff.

%prep
%setup -q -n Array-Diff-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
