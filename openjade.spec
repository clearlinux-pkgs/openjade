#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openjade
Version  : 1.3.2
Release  : 8
URL      : http://downloads.sourceforge.net/openjade/openjade-1.3.2.tar.gz
Source0  : http://downloads.sourceforge.net/openjade/openjade-1.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: openjade-bin
Requires: openjade-lib
Requires: openjade-doc
Requires: openjade-data
BuildRequires : OpenSP-dev
Patch1: msggen.pl.patch
Patch2: drop.la.patch

%description
This package contains
- a DSSSL processor called OpenJade.
If you got this file as part of an OpenJade distribution, then you can find
information about OpenJade in HTML format in jadedoc/jade.htm.

%package bin
Summary: bin components for the openjade package.
Group: Binaries
Requires: openjade-data

%description bin
bin components for the openjade package.


%package data
Summary: data components for the openjade package.
Group: Data

%description data
data components for the openjade package.


%package dev
Summary: dev components for the openjade package.
Group: Development
Requires: openjade-lib
Requires: openjade-bin
Requires: openjade-data
Provides: openjade-devel

%description dev
dev components for the openjade package.


%package doc
Summary: doc components for the openjade package.
Group: Documentation

%description doc
doc components for the openjade package.


%package lib
Summary: lib components for the openjade package.
Group: Libraries
Requires: openjade-data

%description lib
lib components for the openjade package.


%prep
%setup -q -n openjade-1.3.2
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static --mandir=/usr/share/man \
--enable-http \
--enable-default-catalog=/etc/sgml/catalog \
--enable-default-search-path=/usr/share/sgml \
--datadir=/usr/share/sgml/openjade-1.3.2
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install install-man
## make_install_append content
install -v -m644 dsssl/catalog %{buildroot}/usr/share/sgml/openjade-1.3.2/
install -v -m644 dsssl/*.{dtd,dsl,sgm} %{buildroot}/usr/share/sgml/openjade-1.3.2
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/openjade

%files data
%defattr(-,root,root,-)
/usr/share/sgml/openjade-1.3.2/builtins.dsl
/usr/share/sgml/openjade-1.3.2/catalog
/usr/share/sgml/openjade-1.3.2/demo.dsl
/usr/share/sgml/openjade-1.3.2/demo.sgm
/usr/share/sgml/openjade-1.3.2/dsssl.dtd
/usr/share/sgml/openjade-1.3.2/extensions.dsl
/usr/share/sgml/openjade-1.3.2/fot.dtd
/usr/share/sgml/openjade-1.3.2/style-sheet.dtd

%files dev
%defattr(-,root,root,-)
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
