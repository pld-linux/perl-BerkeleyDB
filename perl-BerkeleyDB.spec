#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#

# please check again
#%ifarch ppc
#%%undefine	with_tests
#%endif

%include	/usr/lib/rpm/macros.perl
%define	pdir	BerkeleyDB
%define	pnam	BerkeleyDB
Summary:	BerkeleyDB - Perl extension for Berkeley DB version 2, 3 or 4
Summary(pl):	BerkeleyDB - rozszerzenie Perla do baz Berkeley DB w wersji 2, 3 lub 4
Name:		perl-BerkeleyDB
Version:	0.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	fcef06232d1ccd6c2a9cd114e388ea3d
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

%description -l pl
Ten modu³ Perla dostarcza interfejs do wiêkszo¶ci funkcjonalno¶ci
dostêpnej w bazach danych Berkeley DB w wersji 2, 3 i 4. Mo¿na
przyj±æ, ¿e ten interfejs jest identyczny z interfejsem Berkeley DB.
G³ówne zmiany zosta³y poczynione po to, by API DB dzia³a³o na sposób
perlowy. W przypadku u¿ywania Berkeley DB 2.x nowe mo¿liwo¶ci dostêpne
dopiero w DB 3.x lub DB 4.x nie bêd± dostêpne poprzez ten modu³.

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
%{_mandir}/man3/*
