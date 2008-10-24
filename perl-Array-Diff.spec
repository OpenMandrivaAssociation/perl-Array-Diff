%define realname Array-Diff

Summary:	This module do diff two arrays, and return added and deleted arrays 
Name:		perl-%{realname}
Version:	0.05
Release:	%mkrel 1
License:	Artistic or GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/Array-Diff-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Algorithm::Diff)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module do diff two arrays, and return added and deleted arrays. It's
simple usage of Algorithm::Diff.

%prep

%setup -q -n Array-Diff-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
