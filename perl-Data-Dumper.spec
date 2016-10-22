%{?scl:%scl_package perl-Data-Dumper}

Name:           %{?scl_prefix}perl-Data-Dumper
Version:        2.161
Release:        2%{?dist}
Summary:        Stringify perl data structures, suitable for printing and eval
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Dumper/
Source0:        http://www.cpan.org/authors/id/S/SM/SMUELLER/Data-Dumper-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  sed
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B::Deparse)
BuildRequires:  %{?scl_prefix}perl(bytes)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
BuildRequires:  %{?scl_prefix}perl(XSLoader)
# perl-Test-Simple is in cycle with perl-Data-Dumper
%if !%{defined perl_bootstrap}
# Tests only:
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.98
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional tests:
BuildRequires:  %{?scl_prefix}perl(Encode)
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(B::Deparse)
Requires:       %{?scl_prefix}perl(bytes)
Requires:       %{?scl_prefix}perl(Scalar::Util)
Requires:       %{?scl_prefix}perl(XSLoader)

%{?perl_default_filter}

%description
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.

%prep
%setup -q -n Data-Dumper-%{version}
sed -i '/MAN3PODS/d' Makefile.PL

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -delete
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
%{?scl:scl enable %{scl} '}make test%{?scl:'}
%endif

%files
%doc Changes Todo
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Wed Jul 13 2016 Petr Pisar <ppisar@redhat.com> - 2.161-2
- SCL

* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 2.161-1
- 1.161 bump

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-365
- Increase release to favour standalone package

* Wed May 11 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.160-1
- 2.160 bump in order to dual-live with perl 5.24

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.158-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.158-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.158-2
- Perl 5.22 rebuild

* Wed May 06 2015 Petr Pisar <ppisar@redhat.com> - 2.158-1
- 2.158 bump in order to dual-live with perl 5.22

* Fri Sep 19 2014 Petr Pisar <ppisar@redhat.com> - 2.154-1
- 2.154 bump (fixes CVE-2014-4330 (limit recursion when dumping deep data
  structures))

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-311
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-310
- Increase release to favour standalone package

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.151-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.151-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.151-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 10 2014 Petr Pisar <ppisar@redhat.com> - 2.151-1
- 2.151 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.145-292
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.145-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.145-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.145-2
- Perl 5.18 rebuild

* Mon Mar 18 2013 Petr Pisar <ppisar@redhat.com> - 2.145-1
- 2.145 bump

* Thu Feb 28 2013 Petr Pisar <ppisar@redhat.com> - 2.143-1
- 2.143 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Petr Pisar <ppisar@redhat.com> - 2.139-1
- 2.139 bump

* Fri Oct 05 2012 Petr Pisar <ppisar@redhat.com> - 2.136-1
- 2.136 bump

* Fri Aug 24 2012 Petr Pisar <ppisar@redhat.com> - 2.135.07-241
- Disable tests on bootstrap

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.135.07-240
- update the version to override the module from perl.srpm
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.131-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.131-2
- Perl 5.16 rebuild

* Tue Apr 10 2012 Petr Pisar <ppisar@redhat.com> 2.131-1
- Specfile autogenerated by cpanspec 1.78.
