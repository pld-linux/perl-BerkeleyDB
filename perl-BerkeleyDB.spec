%include	/usr/lib/rpm/macros.perl
%define		pdir	BerkeleyDB
%define		pnam	BerkeleyDB
Summary:	BerkeleyDB Perl module
Summary(cs):	Modul BerkeleyDB pro Perl
Summary(da):	Perlmodul BerkeleyDB
Summary(de):	BerkeleyDB Perl Modul
Summary(es):	Módulo de Perl BerkeleyDB
Summary(fr):	Module Perl BerkeleyDB
Summary(it):	Modulo di Perl BerkeleyDB
Summary(ja):	BerkeleyDB Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	BerkeleyDB ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul BerkeleyDB
Summary(pl):	Modu³ Perla BerkeleyDB
Summary(pt):	Módulo de Perl BerkeleyDB
Summary(pt_BR):	Módulo Perl BerkeleyDB
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl BerkeleyDB
Summary(sv):	BerkeleyDB Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl BerkeleyDB
Summary(zh_CN):	BerkeleyDB Perl Ä£¿é
Name:		perl-BerkeleyDB
Version:	0.19
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	db3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Database perl module.

%description -l cs
Modul BerkeleyDB pro Perl.

%description -l da
Perlmodul BerkeleyDB.

%description -l de
BerkeleyDB Perl Modul.

%description -l es
Módulo de Perl BerkeleyDB.

%description -l fr
Module Perl BerkeleyDB.

%description -l it
Modulo di Perl BerkeleyDB.

%description -l ja
BerkeleyDB Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
BerkeleyDB ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul BerkeleyDB.

%description -l pl
Modu³ perla BerkeleyDB.

%description -l pt
Módulo de Perl BerkeleyDB.

%description -l pt_BR
Módulo Perl BerkeleyDB.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl BerkeleyDB.

%description -l sv
BerkeleyDB Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl BerkeleyDB.

%description -l zh_CN
BerkeleyDB Perl Ä£¿é

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
