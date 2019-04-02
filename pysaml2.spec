#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysaml2
Version  : 4.7.0
Release  : 47
URL      : https://files.pythonhosted.org/packages/8c/b5/ddc94816e48cbd50b6fc5c1902563c919dc7bd2dcd7601636ff115201a34/pysaml2-4.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8c/b5/ddc94816e48cbd50b6fc5c1902563c919dc7bd2dcd7601636ff115201a34/pysaml2-4.7.0.tar.gz
Summary  : Python implementation of SAML Version 2 Standard
Group    : Development/Tools
License  : Apache-2.0
Requires: pysaml2-bin = %{version}-%{release}
Requires: pysaml2-license = %{version}-%{release}
Requires: pysaml2-python = %{version}-%{release}
Requires: pysaml2-python3 = %{version}-%{release}
Requires: cryptography
Requires: defusedxml
Requires: pyOpenSSL
Requires: python-dateutil
Requires: pytz
Requires: repoze.who
Requires: requests
Requires: six
Requires: zope.interface
BuildRequires : Mako
BuildRequires : MarkupSafe-python
BuildRequires : Paste
BuildRequires : WebOb-python
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : decorator-python
BuildRequires : enum34-python
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : mongodict
BuildRequires : py-python
BuildRequires : pyOpenSSL-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pycrypto-python
BuildRequires : pymongo-python
BuildRequires : pytest-python
BuildRequires : python-dateutil-python
BuildRequires : python-memcached
BuildRequires : pytz-python
BuildRequires : repoze.who-python
BuildRequires : requests-python
BuildRequires : six
BuildRequires : six-python
BuildRequires : xmlsec1
BuildRequires : xmlsec1-dev
BuildRequires : zope.interface-python

%description
*************************
PySAML2 - SAML2 in Python
*************************
:Version: see VERSION_
:Documentation: https://pysaml2.readthedocs.io/

%package bin
Summary: bin components for the pysaml2 package.
Group: Binaries
Requires: pysaml2-license = %{version}-%{release}

%description bin
bin components for the pysaml2 package.


%package license
Summary: license components for the pysaml2 package.
Group: Default

%description license
license components for the pysaml2 package.


%package python
Summary: python components for the pysaml2 package.
Group: Default
Requires: pysaml2-python3 = %{version}-%{release}

%description python
python components for the pysaml2 package.


%package python3
Summary: python3 components for the pysaml2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pysaml2 package.


%prep
%setup -q -n pysaml2-4.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554224928
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pysaml2
cp LICENSE %{buildroot}/usr/share/package-licenses/pysaml2/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/make_metadata.py
/usr/bin/mdexport.py
/usr/bin/merge_metadata.py
/usr/bin/parse_xsd2.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pysaml2/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
