%define		_class		Auth
%define		_subclass	HTTP
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(Auth/Auth.php)

Name:       php-pear-%{upstream_name}
Version:	2.1.6
Release:	%mkrel 11
Summary:	HTTP authentication system using PHP
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Auth_HTTP/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The PEAR::Auth_HTTP class provides methods for creating an HTTP
authentication system using PHP, that is similar to Apache's
realm-based .htaccess authentication.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}
cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


