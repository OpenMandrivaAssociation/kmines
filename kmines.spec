#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)

Name:		kmines
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
Summary:	The classic mine sweeper
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://games.kde.org/game.php?game=kmines
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/kmines/-/archive/%{gitbranch}/kmines-%{gitbranchd}.tar.bz2#/kmines-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kmines-%{version}.tar.xz
%endif
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(KDEGames6)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Crash)

%rename plasma6-kmines

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
KMines is a classic Minesweeper game. The idea is to uncover all the squares
without blowing up any mines. When a mine is blown up, the game is over.

%files -f %{name}.lang
%{_bindir}/kmines
%{_datadir}/applications/org.kde.kmines.desktop
%{_iconsdir}/hicolor/*/apps/kmines.png
%{_datadir}/kmines
%{_datadir}/metainfo/*.xml
%{_datadir}/qlogging-categories6/kmines.categories
%{_datadir}/qlogging-categories6/kmines.renamecategories
