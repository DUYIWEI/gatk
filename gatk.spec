Name:     gatk
Version:  4.2.0.0
Release:  1
Summary:  GATK - Genome Analysis Toolkit
License:  MIT
URL:      https://github.com/broadinstitute/gatk

Source:   gatk-4.2.0.0.zip

%description

The Genome Analysis Toolkit or GATK is a software package developed at
the Broad Institute to analyze high-throughput sequencing data. The
toolkit offers a wide variety of tools, with a primary focus on variant
discovery and genotyping as well as strong emphasis on data quality
assurance. Its robust architecture, powerful processing engine and
high-performance computing features make it capable of taking on
projects of any size.

%prep
%setup -q


%build
mkdir -vp %{buildroot}%{_bindir}/
%{__cp} -a %{_builddir}/*  %{buildroot}%{_bindir}/
%{__cp} -s %{buildroot}%{_bindir}/%{name}-%{version}/gatk %{buildroot}%{_bindir}/



%files
%{_bindir}/


%define debug_package %{nil}


%changelog
* Wed Apr 21 2021 duyiwei <duyiwei@kylinos.cn> - 4.2.0.0-1
- Package init
