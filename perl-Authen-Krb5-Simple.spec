#
# TODO: pl desc
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Authen
%define		pnam	Krb5-Simple
Summary:	Authen::Krb5::Simple - Basic user authentication using Kerberos 5
Summary(pl.UTF-8):	Authen::Krb5::Simple - Autentykacja przy pomocy Kerberosa 5
Name:		perl-Authen-Krb5-Simple
Version:	0.43
Release:	13
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Authen/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	209812d935d778c0a22247b5159bc0f6
URL:		http://search.cpan.org/dist/Authen-Krb5-Simple/
BuildRequires:	heimdal-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Authen::Krb5::Simple module provides a means to authenticate a
user/password using Kerberos 5 protocol. The module's authenticate
function takes a username (or user@kerberos_realm) and a password, and
authenticates that user using the local Kerberos 5 installation. It
was initially created to allow perl scripts to perform authentication
against a Microsoft Active Directory (AD) server configured to accept
Kerberos client requests.

It is important to note: This module only performs simple
authentication. It does not get, grant, use, or retain any kerberos
tickets. It will check user credentials against the Kerberos server
(as configured on the local system) each time the authenticate method
is called.

#%description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}"
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/Authen/Krb5
%{perl_vendorarch}/Authen/Krb5/Simple.pm
%dir %{perl_vendorarch}/auto/Authen/Krb5
%dir %{perl_vendorarch}/auto/Authen/Krb5/Simple
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/Krb5/Simple/Simple.so
%{_mandir}/man3/*
