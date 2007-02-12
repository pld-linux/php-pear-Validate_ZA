%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	ZA
%define		_status		alpha
%define		_pearname	Validate_ZA

Summary:	%{_pearname} - Validation class for South Africa
Summary(pl.UTF-8):	%{_pearname} - Klasa do sprawdzania poprawności dla RPA
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a64e21b094801d312a4f3bbcc9888383
URL:		http://pear.php.net/package/Validate_ZA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Requires:	php-pear-Validate_Finance_CreditCard >= 0.5.0
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

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
%dir %{php_pear_dir}/data/Validate_ZA
%{php_pear_dir}/data/Validate_ZA/ZA_postcodes.txt

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_ZA
