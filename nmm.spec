Summary:	Network-integrated Multimedia Middleware
Summary(pl.UTF-8):   Network-integrated Multimedia Middleware - zintegrowany z siecią system multimedialny
Name:		nmm
Version:	0.9.1
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://graphics.cs.uni-sb.de/NMM/dist-%{version}/Download/%{name}-%{version}.tar.gz
# Source0-md5:	7e7e1fa9c2648da0d59c54aa414bc9c7
URL:		http://www.networkmultimedia.org/NMM/
BuildRequires:	ImageMagick-c++-devel
BuildRequires:	a52dec-libs-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	doxygen
BuildRequires:	ffmpeg-devel
BuildRequires:	gd-devel
BuildRequires:	libdivxdecore-devel
BuildRequires:	libdvdnav-devel
BuildRequires:	libdvdread-devel
BuildRequires:	libshout-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	lirc-devel
BuildRequires:	live
BuildRequires:	mpeg2dec-devel
BuildRequires:	nasm
BuildRequires:	ncurses-devel
BuildRequires:	qt-devel
BuildRequires:	xerces-c-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NMM is a multimedia middleware package that allows creation of
distributed multimedia applications easily. A number of plugins
supporting various media types, operations, and I/O devices are
included. The Multimedia-Box application built on top of NMM provides
an extensible home entertainment system for DVD/CD playback and
grabbing, TV with time-shifting, video recording, and playlist
creation and playback for all supported media types.

%description -l pl.UTF-8
NMM to pakiet pośredniczącego oprogramowania multimedialnego
umożliwiający łatwe tworzenie rozproszonych aplikacji multimedialnych.
Załączonych jest wiele wtyczek obsługujących różne rodzaje mediów,
operacji i urządzeń we/wy. Aplikacja Multimedia-Box stworzona w
oparciu o NMM udostępnia rozszerzalny system domowej rozrywki do
odtwarzania i przechwytywania DVD/CD, telewizji z przesunięciem w
czasie, nagrywania obrazu oraz tworzenia playlist dla wszystkich
obsługiwanych rodzajów mediów.

%prep
%setup -q

%build
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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
