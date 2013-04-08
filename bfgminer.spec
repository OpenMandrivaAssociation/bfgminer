# this defines the library version that this package builds.
%define libname %mklibname blkmaker0.1
%define devname %mklibname blkmaker0.1 -d
%define libjname %mklibname blkmaker_jansson0.1 

Summary: 	A bitcoin miner
Name: 		bfgminer
Version: 	3.0.0
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
%{_bindir}/bitstreams/COPYING_fpgaminer
%{_bindir}/bitstreams/COPYING_ztex
%{_bindir}/bitstreams/fpgaminer_x6500-overclocker-0402.bit
%{_bindir}/bitstreams/ztex_ufm1_15b1.bit
%{_bindir}/bitstreams/ztex_ufm1_15d1.bit
%{_bindir}/bitstreams/ztex_ufm1_15d3.bit
%{_bindir}/bitstreams/ztex_ufm1_15d4.bin
%{_bindir}/bitstreams/ztex_ufm1_15d4.bit
%{_bindir}/bitstreams/ztex_ufm1_15y1.bin
%{_bindir}/bitstreams/ztex_ufm1_15y1.bit
%{_bindir}/diablo121016.cl
%{_bindir}/diakgcn121016.cl
%{_bindir}/phatk121016.cl
%{_bindir}/poclbm121016.cl
%{_bindir}/scrypt121016.cl

%files -n %{devname}
%{_libdir}/libblkmaker_jansson-0.1.so
%{_libdir}/libblkmaker-0.1.so
%{_includedir}/libblkmaker-0.1/blkmaker.h
%{_includedir}/libblkmaker-0.1/blktemplate.h
%{_libdir}/pkgconfig/libblkmaker_jansson-0.1.pc

%files -n %{libjname}
%{_libdir}/libblkmaker_jansson-0.1.so.0
%{_libdir}/libblkmaker_jansson-0.1.so.0.4.0

%files -n %{libname}
%{_libdir}/libblkmaker-0.1.so.0
%{_libdir}/libblkmaker-0.1.so.0.4.0
