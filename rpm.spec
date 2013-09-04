
Name: lhasa
Summary: Free LZH archive tool
Version: 0.2.0
Release: 1
Source: https://github.com/downloads/fragglet/lhasa/lhasa-0.2.0.tar.gz
URL: http://fragglet.github.com/lhasa/
Group: Applications/Archiving
BuildRoot: /var/tmp/lhasa-buildroot
License: ISC license
Packager: Simon Howard <fraggle@gmail.com>
Prefix: %{_prefix}
Autoreq: 0

%description
%(cat README)

See  for more information.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
./configure \
 	--prefix=/usr \
	--exec-prefix=/usr \
	--bindir=/usr/bin \
	--sbindir=/usr/sbin \
	--sysconfdir=/etc \
	--datadir=/usr/share \
	--includedir=/usr/include \
	--libdir=/usr/lib \
	--libexecdir=/usr/lib \
	--localstatedir=/var/lib \
	--sharedstatedir=/usr/com \
	--mandir=/usr/share/man \
	--infodir=/usr/share/info
make

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc %{_mandir}/man1/*
/usr/bin/*
/usr/lib*/*
/usr/include/*/*

