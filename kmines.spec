Name:		kmines
Version:	4.10.3
Release:	1
Epoch:		1
Summary:	The classic mine sweeper
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmines
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
KMines is a classic Minesweeper game. The idea is to uncover all the squares
without blowing up any mines. When a mine is blown up, the game is over.

%files
%{_kde_bindir}/kmines
%{_kde_applicationsdir}/kmines.desktop
%{_kde_appsdir}/kmines
%{_kde_configdir}/kmines.knsrc
%{_kde_docdir}/*/*/kmines
%{_kde_iconsdir}/hicolor/*/apps/kmines.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

