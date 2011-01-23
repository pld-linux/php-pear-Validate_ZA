%include	/usr/lib/rpm/macros.php
%define		_status		alpha
%define		_pearname	Validate_ZA
Summary:	%{_pearname} - Validation class for South Africa
Summary(pl.UTF-8):	%{_pearname} - Klasa do sprawdzania poprawności dla RPA
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	2
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	56e8c8f516a849f66c094fce97eb0369
URL:		http://pear.php.net/package/Validate_ZA/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Requires:	php-pear-Validate_Finance_CreditCard >= 0.5.0
Obsoletes:	php-pear-Validate_ZA-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package containes locale validation for South Africa such as:
- Postal Code
- Region (province)
- SSN

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Republiki Południowej Afryki
danych takich jak:
- kod pocztowy
- region (prowincja)
- numer ubezpieczenia społecznego (SSN)

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/ZA.php

%{php_pear_dir}/data/%{_pearname}
