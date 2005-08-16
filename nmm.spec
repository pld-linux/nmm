Summary:	NETWORK-INTEGRATED MULTIMEDIA MIDDLEWARE
Name:		nmm
Version:	0.9.0
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://graphics.cs.uni-sb.de/NMM/dist-0.9.0/Download/%{name}-%{version}.tar.gz
# Source0-md5:	7cd7e34168e1e57c9897f1c67cdce3d5
URL:		http://www.networkmultimedia.org/NMM/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NMM is a multimedia middleware package that allows creation of
distributed multimedia applications easily. A number of plugins
supporting various media types, operations, and I/O devices are
included. The Multimedia-Box application built on top of NMM provides
an extensible home entertainment system for DVD/CD playback and
grabbing, TV with time-shifting, video recording, and playlist
creation and playback for all supported media types.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif
