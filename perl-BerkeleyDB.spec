#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	BerkeleyDB
%define		pnam	BerkeleyDB
Summary:	BerkeleyDB - Perl extension for Berkeley DB version 2, 3 or 4
Summary(pl.UTF-8):	BerkeleyDB - rozszerzenie Perla do baz Berkeley DB w wersji 2, 3 lub 4
Name:		perl-BerkeleyDB
Version:	0.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/BerkeleyDB/PMQS/%{pnam}-%{version}.tar.gz
# Source0-md5:	3d0cf0651ed8cd3fc36e328d5924a1e9
URL:		http://search.cpan.org/dist/BerkeleyDB/
BuildRequires:	db-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides an interface to most of the functionality
available in Berkeley DB versions 2, 3 and 4. In general it is safe to
assume that the interface provided here to be identical to the
Berkeley DB interface. The main changes have been to make the Berkeley
DB API work in a Perl way. Note that if you are using Berkeley DB 2.x,
the new features available in Berkeley DB 3.x or DB 4.x are not
available via this module.

%description -l pl.UTF-8
Ten moduł Perla dostarcza interfejs do większości funkcjonalności
dostępnej w bazach danych Berkeley DB w wersji 2, 3 i 4. Można
przyjąć, że ten interfejs jest identyczny z interfejsem Berkeley DB.
Główne zmiany zostały poczynione po to, by API DB działało na sposób
perlowy. W przypadku używania Berkeley DB 2.x nowe możliwości dostępne
dopiero w DB 3.x lub DB 4.x nie będą dostępne poprzez ten moduł.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	CC="%{__cc}"

# one of tests relies on English locale
%{?with_tests:%{__make} test LC_ALL=C}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/BerkeleyDB.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/BerkeleyDB/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes Todo
%{perl_vendorarch}/BerkeleyDB
%{perl_vendorarch}/BerkeleyDB.pm
%dir %{perl_vendorarch}/auto/BerkeleyDB
%{perl_vendorarch}/auto/BerkeleyDB/*.bs
%{perl_vendorarch}/auto/BerkeleyDB/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/BerkeleyDB/*.so
%{_mandir}/man3/BerkeleyDB.3pm*
