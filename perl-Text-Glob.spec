#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Glob
Version  : 0.11
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-Glob-0.11.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/Text-Glob-0.11.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtext-glob-perl/libtext-glob-perl_0.10-1.debian.tar.xz
Summary  : 'match globbing patterns against text'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Text-Glob-license = %{version}-%{release}
Requires: perl-Text-Glob-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-Text-Glob package.
Group: Development
Provides: perl-Text-Glob-devel = %{version}-%{release}
Requires: perl-Text-Glob = %{version}-%{release}

%description dev
dev components for the perl-Text-Glob package.


%package license
Summary: license components for the perl-Text-Glob package.
Group: Default

%description license
license components for the perl-Text-Glob package.


%package perl
Summary: perl components for the perl-Text-Glob package.
Group: Default
Requires: perl-Text-Glob = %{version}-%{release}

%description perl
perl components for the perl-Text-Glob package.


%prep
%setup -q -n Text-Glob-0.11
cd %{_builddir}
tar xf %{_sourcedir}/libtext-glob-perl_0.10-1.debian.tar.xz
cd %{_builddir}/Text-Glob-0.11
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Text-Glob-0.11/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Text-Glob
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Text-Glob/31ea80126282e708f47e8f8d02d19d35ec5c50be
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Glob.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Text-Glob/31ea80126282e708f47e8f8d02d19d35ec5c50be

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Text/Glob.pm
