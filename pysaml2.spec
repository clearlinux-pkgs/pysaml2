#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysaml2
Version  : 5.3.0
Release  : 63
URL      : https://files.pythonhosted.org/packages/98/1a/fec9de2584bef50d4a71b65ef1ba759e0ea5140c595b10b7d1456b76c6a0/pysaml2-5.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/98/1a/fec9de2584bef50d4a71b65ef1ba759e0ea5140c595b10b7d1456b76c6a0/pysaml2-5.3.0.tar.gz
Summary  : Python implementation of SAML Version 2 Standard
Group    : Development/Tools
License  : Apache-2.0
Requires: pysaml2-bin = %{version}-%{release}
Requires: pysaml2-license = %{version}-%{release}
Requires: pysaml2-python = %{version}-%{release}
Requires: pysaml2-python3 = %{version}-%{release}
Requires: Paste
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
BuildRequires : defusedxml
BuildRequires : idna-python
BuildRequires : mongodict
BuildRequires : py-python
BuildRequires : pyOpenSSL
BuildRequires : pyOpenSSL-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pymongo-python
BuildRequires : pytest-python
BuildRequires : python-dateutil
BuildRequires : python-dateutil-python
BuildRequires : python-memcached
BuildRequires : pytz
BuildRequires : pytz-python
BuildRequires : repoze.who
BuildRequires : repoze.who-python
BuildRequires : requests
BuildRequires : requests-python
BuildRequires : six
BuildRequires : six-python
BuildRequires : xmlsec1
BuildRequires : xmlsec1-dev
BuildRequires : zope.interface
BuildRequires : zope.interface-python

%description
PySAML2 - SAML2 in Python
        *************************

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
Provides: pypi(pysaml2)
Requires: pypi(cryptography)
Requires: pypi(defusedxml)
Requires: pypi(pyopenssl)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the pysaml2 package.


%prep
%setup -q -n pysaml2-5.3.0
cd %{_builddir}/pysaml2-5.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593191997
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pysaml2
cp %{_builddir}/pysaml2-5.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pysaml2/be8f3eb13b3dfb0e413a47009022c3c5897b60e8
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
/usr/share/package-licenses/pysaml2/be8f3eb13b3dfb0e413a47009022c3c5897b60e8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
