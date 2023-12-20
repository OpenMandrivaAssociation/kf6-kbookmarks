%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Bookmarks
%define devname %mklibname KF6Bookmarks -d
#define git 20231103

Name: kf6-kbookmarks
Version: 5.247.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kbookmarks/-/archive/master/kbookmarks-master.tar.bz2#/kbookmarks-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{version}/kbookmarks-%{version}.tar.xz
%endif
Summary: Bookmarks management library
URL: https://invent.kde.org/frameworks/kbookmarks
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6ConfigWidgets)
# Avoid pulling in the KF5 version
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Bookmarks management library

%package -n %{libname}
Summary: Bookmarks management library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Bookmarks management library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Bookmarks management library

%prep
%autosetup -p1 -n kbookmarks-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kbookmarks.*
%{_datadir}/qlogging-categories6/kbookmarkswidgets.*

%files -n %{devname}
%{_includedir}/KF6/KBookmarks
%{_includedir}/KF6/KBookmarksWidgets
%{_libdir}/cmake/KF6Bookmarks
%{_qtdir}/doc/KF6Bookmarks.*
%{_qtdir}/doc/KF6BookmarksWidgets.*

%files -n %{libname}
%{_libdir}/libKF6Bookmarks.so*
%{_libdir}/libKF6BookmarksWidgets.so*
