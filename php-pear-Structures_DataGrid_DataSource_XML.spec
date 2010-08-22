%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Structures_DataGrid_DataSource_XML
Summary:	%{_pearname} - DataSource driver using XML files
Summary(pl.UTF-8):	%{_pearname} - sterownik DataSource do plików XML
Name:		php-pear-%{_pearname}
Version:	0.2.0
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0f3e1f2f4438acf1b9b6cc47a95b2b57
URL:		http://pear.php.net/package/Structures_DataGrid_DataSource_XML/
BuildRequires:	php-pear-PEAR >= 1:1.6.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.0
Requires:	php-pear-Structures_DataGrid_DataSource_Array >= 0.1.0
Suggests:	php-pear-XML_Serializer
Suggests:	php-pear-XML_XPath
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(XML/Serializer.*) pear(XML/XPath.*)

%description
This is a DataSource driver for Structures_DataGrid using XML files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza sterownik DataSource do plików XML dla
Structures_DataGrid.

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
%{php_pear_dir}/Structures/DataGrid/DataSource/XML.php
