%include	/usr/lib/rpm/macros.perl
%define		pdir	BerkeleyDB
%define		pnam	BerkeleyDB
Summary:	BerkeleyDB - Perl extension for Berkeley DB version 2, 3 or 4
Name:		perl-BerkeleyDB
Version:	0.19
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	db3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides an interface to most of the functionality
available in Berkeley DB versions 2, 3 and 4. In general it is safe to
assume that the interface provided here to be identical to the Berkeley DB
interface. The main changes have been to make the Berkeley DB API work in
a Perl way. Note that if you are using Berkeley DB 2.x, the new features
available in Berkeley DB 3.x or DB 4.x are not available via this module.

%prep
%setup -q -n %{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3

%{__make} install DESTDIR=$RPM_BUILD_ROOT

pod2man --section=3pm BerkeleyDB.pod >$RPM_BUILD_ROOT%{_mandir}/man3/BerkeleyDB.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes Todo
%{perl_sitearch}/BerkeleyDB
%{perl_sitearch}/BerkeleyDB.pm
%dir %{perl_sitearch}/auto/BerkeleyDB
%{perl_sitearch}/auto/BerkeleyDB/autosplit.ix
%{perl_sitearch}/auto/BerkeleyDB/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/BerkeleyDB/*.so
%{_mandir}/man3/*
