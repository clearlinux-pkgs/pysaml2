#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysaml2
Version  : 4.3.0
Release  : 25
URL      : http://pypi.debian.net/pysaml2/pysaml2-4.3.0.tar.gz
Source0  : http://pypi.debian.net/pysaml2/pysaml2-4.3.0.tar.gz
Summary  : Python implementation of SAML Version 2
Group    : Development/Tools
License  : Apache-2.0
Requires: pysaml2-bin
Requires: pysaml2-python
BuildRequires : Mako
BuildRequires : MarkupSafe-python
BuildRequires : WebOb-python
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography
BuildRequires : decorator-python
BuildRequires : enum34-python
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : mongodict
BuildRequires : paste-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py-python
BuildRequires : pyOpenSSL-python
BuildRequires : pyasn1-python
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pycrypto-python
BuildRequires : pymongo-python
BuildRequires : pytest-python
BuildRequires : python-dateutil-python
BuildRequires : python-dev
BuildRequires : python-memcached
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : repoze.who-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : xmlsec1
BuildRequires : xmlsec1-dev
BuildRequires : zope.interface-python

%description
This is a very simple setup just to check that all your gear are in order.
The setup consists of one IdP and one SP, in idp2/ and sp-wsgi/ respectively.

%package bin
Summary: bin components for the pysaml2 package.
Group: Binaries

%description bin
bin components for the pysaml2 package.


%package python
Summary: python components for the pysaml2 package.
Group: Default
Requires: decorator-python
Requires: paste-python
Requires: pyOpenSSL-python
Requires: python-dateutil-python
Requires: pytz-python
Requires: repoze.who-python
Requires: requests-python
Requires: six-python
Requires: zope.interface-python

%description python
python components for the pysaml2 package.


%prep
%setup -q -n pysaml2-4.3.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/make_metadata.py
/usr/bin/mdexport.py
/usr/bin/merge_metadata.py
/usr/bin/parse_xsd2.py

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
