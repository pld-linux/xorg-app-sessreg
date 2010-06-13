Summary:	sessreg application - manage utmp/wtmp entries for non-init clients
Summary(pl.UTF-8):	Aplikacja sessreg - zarządzanie wpisami utmp/wtmp przez klientów innych niż init
Name:		xorg-app-sessreg
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/sessreg-%{version}.tar.bz2
# Source0-md5:	8c8fcda19f4cffe573d43ec9b8255f8e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.4
Provides:	sessreg
Obsoletes:	X11-sessreg < 1:7.0.0
Obsoletes:	XFree86-sessreg < 1:7.0.0
Obsoletes:	sessreg < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sessreg is a simple program for managing utmp/wtmp entries for X
sessions. It was originally written for use with xdm, but may also be
used with other display managers such as gdm or kdm.

%description -l pl.UTF-8
sessreg to prosty program do zarządzania wpisami utmp/wtmp dla sesji
X. Pierwotnie został napisany dla xdm-a, ale może być używany także z
innymi zarządcami ekranów, takimi jak gdm czy kdm.

%prep
%setup -q -n sessreg-%{version}

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
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1x*
