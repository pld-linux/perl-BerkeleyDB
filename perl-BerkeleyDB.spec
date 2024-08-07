#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	BerkeleyDB
%define		pnam	BerkeleyDB
Summary:	BerkeleyDB - Perl extension for Berkeley DB version (version 2 or greater)
Summary(pl.UTF-8):	BerkeleyDB - rozszerzenie Perla do baz Berkeley DB (w wersji 2 lub wyższej)
Name:		perl-BerkeleyDB
Version:	0.65
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/BerkeleyDB/%{pnam}-%{version}.tar.gz
# Source0-md5:	2759214adcff0759e7a9e8ba1d6f7a73
URL:		https://metacpan.org/dist/BerkeleyDB
BuildRequires:	db-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl module provides an interface to most of the functionality
available in Berkeley DB versions 2, 3, 4, 5 and 6. In general it is
safe to assume that the interface provided here to be identical to the
Berkeley DB interface. The main changes have been to make the Berkeley
DB API work in a Perl way. Note that if you are using Berkeley DB 2.x,
the new features available in Berkeley DB 3.x or DB 4.x are not
available via this module.

%description -l pl.UTF-8
Ten moduł Perla dostarcza interfejs do większości funkcjonalności
dostępnej w bazach danych Berkeley DB w wersji 2, 3, 4, 5 i 6. Można
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

# build tools
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/{mkconsts,scan}.pl

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
%attr(755,root,root) %{perl_vendorarch}/auto/BerkeleyDB/BerkeleyDB.so
%{_mandir}/man3/BerkeleyDB.3pm*
