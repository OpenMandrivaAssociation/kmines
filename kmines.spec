Name:		kmines
Version:	15.04.3
Release:	2
Epoch:		1
Summary:	The classic mine sweeper
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://games.kde.org/game.php?game=kmines
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(KF5KDEGames)
BuildRequires:  cmake(KF5CoreAddons)                                                                   
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5WidgetsAddons)                                                                
BuildRequires:  cmake(KF5Config)                                                                       
BuildRequires:  cmake(KF5DBusAddons)                                                                   
BuildRequires:  cmake(KF5I18n)                                                                         
BuildRequires:  cmake(KF5ConfigWidgets)                                                                
BuildRequires:  cmake(KF5TextWidgets)                                                                  
BuildRequires:  cmake(KF5XmlGui)                                                                       
BuildRequires:  cmake(KF5KIO)                                                                          
BuildRequires:  cmake(KF5NotifyConfig)  


%description
KMines is a classic Minesweeper game. The idea is to uncover all the squares
without blowing up any mines. When a mine is blown up, the game is over.

%files
%{_bindir}/kmines                                                                                      
%{_datadir}/applications/org.kde.kmines.desktop                                                                                                                                        
%{_sysconfdir}/xdg/kmines.knsrc  
%{_datadir}/knotifications5/kmines.notifyrc
%doc %{_docdir}/*/*/kmines   
%{_datadir}/kxmlgui5/kmines/kminesui.rc
%{_iconsdir}/hicolor/*/apps/kmines.pn

#------------------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

