%include	/usr/lib/rpm/macros.perl
Summary:	Berkeley Database perl module
Summary(pl):	Modu³ perla BerkeleyDB
Name:		perl-BerkeleyDB
Version:	0.18
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/BerkeleyDB/BerkeleyDB-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	db3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Database perl module.

%description -l pl
Modu³ perla BerkeleyDB.

%prep
%setup -q -n BerkeleyDB-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}" CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes Todo

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/BerkeleyDB
%{perl_sitearch}/BerkeleyDB.*
%dir %{perl_sitearch}/auto/BerkeleyDB
%{perl_sitearch}/auto/BerkeleyDB/*.ix
%attr(755,root,root) %{perl_sitearch}/auto/BerkeleyDB/*.so
