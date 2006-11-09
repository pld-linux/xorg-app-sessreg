Summary:	sessreg application
Summary(pl):	Aplikacja sessreg
Name:		xorg-app-sessreg
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/sessreg-%{version}.tar.bz2
# Source0-md5:	d412730cf30e6341f9df43405a01229a
Patch0:		%{name}-sed.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1
Obsoletes:	X11-sessreg
Obsoletes:	XFree86-sessreg
Obsoletes:	sessreg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sessreg application.

%description -l pl
Aplikacja sessreg.

%prep
%setup -q -n sessreg-%{version}
%patch0 -p1

# xproto is sufficient
sed -i -e 's/ x11/ xproto/' configure.ac

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1x*
