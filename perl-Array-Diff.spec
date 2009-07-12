%define upstream_name    Array-Diff
%define upstream_version 0.05002

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_name}
Release:	%mkrel 1

Summary:	This module do diff two arrays, and return added and deleted arrays 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Class::Accessor::Fast)
BuildRequires:	perl(Algorithm::Diff)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module do diff two arrays, and return added and deleted arrays. It's
simple usage of Algorithm::Diff.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

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
