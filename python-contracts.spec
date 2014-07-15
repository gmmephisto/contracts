%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-contracts
Version:        1.5.0
Release:        CROC1%{?dist}
Summary:        PyContracts is a Python package that allows to declare constraints on function parameters and return values.

Group:          Development/Libraries
License:        LGPL
URL:            https://pypi.python.org/pypi/PyContracts
Source0:        contracts.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  python-devel, python-setuptools, python-nose
BuildRequires:  python-decorator, pyparsing

Requires:       python-decorator, pyparsing


%description
PyContracts is a Python package that allows to declare constraints on
function parameters and return values. It supports a basic type system,
variables binding, arithmetic constraints, and has several specialized
contracts (notably for Numpy arrays).


%prep
%setup -q -n contracts


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc LICENSE.txt README.rst
%{python_sitelib}/*


%changelog
* Tue Jul 15 2014 Mikhail Ushanov <MiUshanov@croc.ru> - 1.5.0-CROC1
- Init release
