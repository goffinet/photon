%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_version: %define python_version %(python3 -c "import sys; sys.stdout.write(sys.version[:3])")}

Name:           python-mako
Version:        1.0.6
Release:        2%{?dist}
Summary:        Python templating language
License:        MIT
Group:          Development/Languages/Python
Url:            https://pypi.python.org/packages/56/4b/cb75836863a6382199aefb3d3809937e21fa4cb0db15a4f4ba0ecc2e7e8e/Mako-%{version}.tar.gz
Source0:        Mako-%{version}.tar.gz
%define sha1    Mako=8cbc52319268525208c88dd3ef62c929069e4b24

BuildRequires:  python2
BuildRequires:  python2-libs
BuildRequires:  python-setuptools

Requires:       python2
Requires:       python2-libs

BuildArch:      noarch

%description
A super-fast templating language that borrows the best ideas from the existing templating languages. Mako is a template library written in Python. It provides a familiar, non-XML syntax which compiles into Python modules for maximum performance. Mako’s syntax and API borrows from the best ideas of many others, including Django templates, Cheetah, Myghty, and Genshi.

%package -n     python3-mako
Summary:        python-mako
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-libs
Requires:       python3
Requires:       python3-libs

%description -n python3-mako
Python 3 version.
%prep
%setup -n Mako-%{version}

%build
python setup.py build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
mv %{buildroot}/%{_bindir}/mako-render %{buildroot}/%{_bindir}/mako-render-%{python3_version}
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%check
easy_install py
%{__python} test_mako.py
python3 test_mako.py

%files
%defattr(-,root,root,-)
%{_bindir}/mako-render
%{python_sitelib}/*

%files -n python3-mako
%defattr(-,root,root,-)
%{python3_sitelib}/*
%{_bindir}/mako-render-%{python3_version}

%changelog
*   Fri Mar 03 2017 Xiaolin Li <xiaolinl@vmware.com> 1.0.6-2
-   Added python3 package.
*   Fri Feb 03 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.0.6-1
-   Initial version of python-mako package for Photon.
