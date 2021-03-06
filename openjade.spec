#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openjade
Version  : 1.3.2
Release  : 14
URL      : https://sourceforge.net/projects/openjade/files/openjade/1.3.2/openjade-1.3.2.tar.gz
Source0  : https://sourceforge.net/projects/openjade/files/openjade/1.3.2/openjade-1.3.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: openjade-bin = %{version}-%{release}
Requires: openjade-data = %{version}-%{release}
Requires: openjade-lib = %{version}-%{release}
Requires: openjade-license = %{version}-%{release}
Requires: openjade-man = %{version}-%{release}
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
Requires: openjade-data = %{version}-%{release}
Requires: openjade-license = %{version}-%{release}

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
Requires: openjade-lib = %{version}-%{release}
Requires: openjade-bin = %{version}-%{release}
Requires: openjade-data = %{version}-%{release}
Provides: openjade-devel = %{version}-%{release}
Requires: openjade = %{version}-%{release}

%description dev
dev components for the openjade package.


%package lib
Summary: lib components for the openjade package.
Group: Libraries
Requires: openjade-data = %{version}-%{release}
Requires: openjade-license = %{version}-%{release}

%description lib
lib components for the openjade package.


%package license
Summary: license components for the openjade package.
Group: Default

%description license
license components for the openjade package.


%package man
Summary: man components for the openjade package.
Group: Default

%description man
man components for the openjade package.


%prep
%setup -q -n openjade-1.3.2
cd %{_builddir}/openjade-1.3.2
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600306211
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --mandir=/usr/share/man \
--enable-http \
--enable-default-catalog=/etc/sgml/catalog \
--enable-default-search-path=/usr/share/sgml \
--datadir=/usr/share/sgml/openjade-1.3.2
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1600306211
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openjade
cp %{_builddir}/openjade-1.3.2/COPYING %{buildroot}/usr/share/package-licenses/openjade/0165e1ea358c77aad62debbc8ff2500afb2e58e3
cp %{_builddir}/openjade-1.3.2/jadedoc/copying.txt %{buildroot}/usr/share/package-licenses/openjade/6dc2ff7df6f06252d8449a3da8ffc522a0b582f9
%make_install install-man
## install_append content
# From http://www.linuxfromscratch.org/blfs/view/svn/pst/openjade.html
# MIT License

install -v -m644 dsssl/catalog %{buildroot}/usr/share/sgml/openjade-1.3.2/

install -v -m644 dsssl/*.{dtd,dsl,sgm} %{buildroot}/usr/share/sgml/openjade-1.3.2

## install_append end

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
/usr/lib64/libogrove.so
/usr/lib64/libospgrove.so
/usr/lib64/libostyle.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libogrove.so.0
/usr/lib64/libogrove.so.0.0.1
/usr/lib64/libospgrove.so.0
/usr/lib64/libospgrove.so.0.0.1
/usr/lib64/libostyle.so.0
/usr/lib64/libostyle.so.0.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openjade/0165e1ea358c77aad62debbc8ff2500afb2e58e3
/usr/share/package-licenses/openjade/6dc2ff7df6f06252d8449a3da8ffc522a0b582f9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/openjade.1
