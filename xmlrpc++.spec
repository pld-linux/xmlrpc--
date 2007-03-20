# TODO:
# - build doxygen docs
# - check compile.patch
#
Summary:	XmlRpc++ is a C++ implementation of the XML-RPC
Name:		xmlrpc++
Version:	0.7
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xmlrpcpp/%{name}%{version}.tar.gz
# Source0-md5:	d88f0f9c36d938316d672d16f6c37d7e
Patch0:		%{name}-compile.patch
Patch1:		%{name}-use_autotools.patch
URL:		http://xmlrpcpp.sourcforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XmlRpc++ is an implementation of the XmlRpc protocol written in C++,
based upon Shilad Sen's excellent py-xmlrpc library. XmlRpc++ is
designed to make it easy to incorporate XmlRpc client and server
support into C++ applications. Or use both client and server objects
in your app for easy peer-to-peer support.

%package devel
Summary:	Header files for XmlRpc++ library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki XmlRpc++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
%patch0 -p1
%patch1 -p1

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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
