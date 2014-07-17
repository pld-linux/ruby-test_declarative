#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	test_declarative
Summary:	Simply adds a declarative test method syntax to test/unit
Name:		ruby-%{pkgname}
Version:	0.0.5
Release:	2
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	994da4bb1425c8cb72c7effeeacd5abc
URL:		http://github.com/svenfuchs/test_declarative
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simply adds a declarative test method syntax to test/unit.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%if %{with tests}
testrb test
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.textile MIT-LICENSE
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
