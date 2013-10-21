# this defines the library version that this package builds.
%define libname %mklibname blkmaker0.1
%define devname %mklibname blkmaker0.1 -d
%define libjname %mklibname blkmaker_jansson0.1 

Summary: 	A bitcoin miner
Name: 		bfgminer
Version: 	3.3.0
Release: 	1
License: 	GPL
Group:		Networking/Other 
Source0: 	http://luke.dashjr.org/programs/bitcoin/files/bfgminer/%{version}/bfgminer-%{version}.tbz2
Url: 		https://bitcointalk.org/?topic=78192
BuildRequires:	pkgconfig(jansson)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	uthash-devel
BuildRequires:	yasm-devel
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libjname} = %{version}-%{release}

%description
This is a multi-threaded multi-pool GPU, FPGA and CPU miner with ATI GPU
monitoring, (over)clocking and fanspeed support for bitcoin and derivative
coins.


%package -n	%{libname}
Group: System/Libraries

%description -n	%{libname}
A bitcoin miner libraries.

%package -n	%{libjname}
Group:		System/Libraries

%description -n %{libjname}
A bitcoin miner libraries.

%package -n	%{devname}
Summary:	Libraries and header files for bfgminer
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	bfgminer-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libjname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%description -n	%{libname}
A bitcoin miner libraries.

%prep
%setup -n bfgminer-%{version}

%build
#./autogen.sh
%configure2_5x --enable-ztex --enable-bitforce --enable-icarus --enable-cpumining

%install
%makeinstall_std

%files
%{_bindir}/bfgminer
%{_bindir}/bfgminer-rpc
%{_bindir}/bitforce-firmware-flash
%{_datadir}/%{name}/opencl/*.cl
%{_datadir}/doc/bfgminer/*

%files -n %{devname}
%{_libdir}/libblkmaker_jansson-0.1.so
%{_libdir}/libblkmaker-0.1.so
%{_includedir}/libblkmaker-0.1/blkmaker.h
%{_includedir}/libblkmaker-0.1/blkmaker_jansson.h
%{_includedir}/libblkmaker-0.1/blktemplate.h
%{_libdir}/pkgconfig/libblkmaker_jansson-0.1.pc

%files -n %{libjname}
%{_libdir}/libblkmaker_jansson-0.1.so.0
%{_libdir}/libblkmaker_jansson-0.1.so.0.4.1

%files -n %{libname}
%{_libdir}/libblkmaker-0.1.so.0
%{_libdir}/libblkmaker-0.1.so.0.4.1
