Summary:	Network-integrated Multimedia Middleware
Summary(pl):	Network-integrated Multimedia Middleware - zintegrowany z sieci� system multimedialny
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

%description -l pl
NMM to pakiet po�rednicz�cego oprogramowania multimedialnego
umo�liwiaj�cy �atwe tworzenie rozproszonych aplikacji multimedialnych.
Za��czonych jest wiele wtyczek obs�uguj�cych r�ne rodzaje medi�w,
operacji i urz�dze� we/wy. Aplikacja Multimedia-Box stworzona w
oparciu o NMM udost�pnia rozszerzalny system domowej rozrywki do
odtwarzania i przechwytywania DVD/CD, telewizji z przesuni�ciem w
czasie, nagrywania obrazu oraz tworzenia playlist dla wszystkich
obs�ugiwanych rodzaj�w medi�w.

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
