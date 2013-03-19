%define		_class		Auth
%define		_subclass	HTTP
%define		upstream_name	%{_class}_%{_subclass}

Name:       php-pear-%{upstream_name}
Version:	2.1.8
Release:	1
Summary:	HTTP authentication system using PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth_HTTP/
Source0:	http://download.pear.php.net/package/Auth_HTTP-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{_class}_%{_subclass}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-14mdv2012.0
+ Revision: 741823
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-13
+ Revision: 679261
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-12mdv2011.0
+ Revision: 613614
- the mass rebuild of 2010.1 packages

* Tue Nov 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.1.6-11mdv2010.1
+ Revision: 464349
- spec cleanup
- use rpm filetriggers to register starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.1.6-10mdv2010.0
+ Revision: 440930
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-9mdv2009.1
+ Revision: 321892
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-8mdv2009.0
+ Revision: 236801
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 2.1.6-7mdv2008.1
+ Revision: 140729
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-7mdv2007.0
+ Revision: 81355
- Import php-pear-Auth_HTTP

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.1.6-1mdk
- initial Mandriva package (PLD import)


