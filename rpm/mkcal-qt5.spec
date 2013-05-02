# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       mkcal-qt5

# >> macros
# << macros

Summary:    Extended KDE kcal calendar library port for Maemo
Version:    0.3.11
Release:    1
Group:      System/Libraries
License:    LGPLV2
URL:        https://github.com/mer-packages/mkcal
Source0:    %{name}-%{version}.tar.bz2
Source100:  mkcal-qt5.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(libkcalcoren-qt5)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(timed-qt5)

%description
Extended KDE kcal calendar library port for Maemo


%package devel
Summary:    Development files for mkcal
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
applications using mkcal


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake5 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libmkcal-qt5.so.*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_includedir}/mkcal-qt5/*
%{_libdir}/libmkcal-qt5.so
%{_libdir}/pkgconfig/*.pc
# >> files devel
# << files devel
