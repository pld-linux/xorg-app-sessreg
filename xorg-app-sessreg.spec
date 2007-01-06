Summary:	sessreg application - manage utmp/wtmp entries for non-init clients
Summary(pl):	Aplikacja sessreg - zarz±dzanie wpisami utmp/wtmp przez klientów innych ni¿ init
Name:		xorg-app-sessreg
Version:	1.0.2
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/sessreg-%{version}.tar.bz2
# Source0-md5:	bee5d87d40615e67c84ab0b0c65049ba
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1
Provides:	sessreg
Obsoletes:	X11-sessreg < 1:7.0.0
Obsoletes:	XFree86-sessreg < 1:7.0.0
Obsoletes:	sessreg < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

%description -l pl
sessreg to prosty program do zarz±dzania wpisami utmp/wtmp dla sesji
xdm.

%prep
%setup -q -n sessreg-%{version}

# xproto is sufficient
%{__sed} -i -e 's/ x11/ xproto/' configure.ac

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
