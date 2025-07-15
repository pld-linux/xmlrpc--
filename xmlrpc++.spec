# TODO:
# - build doxygen docs
# - check compile.patch
#
Summary:	XmlRpc++ is a C++ implementation of the XML-RPC
Summary(pl.UTF-8):	Implementacja protokołu XML-RPC w C++
Name:		xmlrpc++
Version:	0.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/xmlrpcpp/%{name}%{version}.tar.gz
# Source0-md5:	d88f0f9c36d938316d672d16f6c37d7e
Patch0:		%{name}-compile.patch
Patch1:		%{name}-use_autotools.patch
Patch2:		gcc44.patch
URL:		http://xmlrpcpp.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XmlRpc++ is an implementation of the XML-RPC protocol written in C++,
based upon Shilad Sen's excellent py-xmlrpc library. XmlRpc++ is
designed to make it easy to incorporate XML-RPC client and server
support into C++ applications. Or use both client and server objects
in your app for easy peer-to-peer support.

%description -l pl.UTF-8
XmlRpc++ jest implementacją protokołu XML-RPC napisaną w C++. Bazuje
na znakomitej bibliotece py-xmlrpc autorstwa Shilad Sen. XmlRpc++
została zaprojektowana w celu ułatwienia włączenia obsługi klienta i
serwera XML-RPC do aplikacji napisanych z wykorzystaniem C++, lub
użycia obiektów klienta i serwera w aplikacjach peer-to-peer.

%package devel
Summary:	Header files for XmlRpc++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XmlRpc++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for XmlRpc++ library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki XmlRpc++.

%package static
Summary:	Static XmlRpc++ library
Summary(pl.UTF-8):	Statyczna biblioteka XmlRpc++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static XmlRpc++ library.

%description static -l pl.UTF-8
Statyczna biblioteka XmlRpc++.

%prep
%setup -q -n %{name}%{version}
find -name '*.cpp' | xargs %{__sed} -i -e 's,\r$,,'
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.html
%attr(755,root,root) %{_libdir}/libXmlRpc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXmlRpc.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXmlRpc.so
%{_libdir}/libXmlRpc.la
%{_includedir}/XmlRpc*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libXmlRpc.a
