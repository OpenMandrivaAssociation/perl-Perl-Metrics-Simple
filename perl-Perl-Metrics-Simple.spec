%define upstream_name    Perl-Metrics-Simple
%define upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Methods analyzing a single file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::File)
BuildRequires: perl(PPI)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Readonly)
BuildRequires: perl(Statistics::Basic::Mean)
BuildRequires: perl(Statistics::Basic::Median)
BuildRequires: perl(Statistics::Basic::StdDev)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
*Perl::Metrics::Simple* provides just enough methods to run static analysis
of one or many Perl files and obtain a few metrics: packages, subroutines,
lines of code, and an approximation of cyclomatic (mccabe) complexity for
the subroutines and the "main" portion of the code.

*Perl::Metrics::Simple* is far simpler than the Perl::Metrics manpage.

Installs a script called *countperl*.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE META.yml README
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


