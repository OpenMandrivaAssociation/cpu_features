Summary:	A cross platform C99 library to get CPU features at runtime
Summary(pl.UTF-8):	Wieloplatformowa biblioteka C99 do sprawdzania funkcjonalności CPU w czasie działania
Name:		cpu_features
Version:	0.10.1
Release:	1
License:	Apache v2.0
Group:		Libraries
Source0:	https://github.com/google/cpu_features/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://github.com/google/cpu_features
BuildRequires:	cmake

%description
A cross-platform C library to retrieve CPU features (such as available
instructions) at runtime.

%description -l pl.UTF-8
Wieloplatformowa biblioteka C do odczytu funkcjonalności CPU (takiej
jak dostępne instrukcje) w czasie działania programu.

%package devel
Summary:	Header files for cpu_features library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cpu_features
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for cpu_features library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cpu_features.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTING=OFF

%make_build

%install
%make_install -C build

%files
%doc README.md
%{_bindir}/list_cpu_features
%{_libdir}/libcpu_features.so

%files devel
%{_includedir}/cpu_features
%{_libdir}/cmake/CpuFeatures
