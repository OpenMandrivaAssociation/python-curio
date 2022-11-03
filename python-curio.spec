%define module curio

Summary:	A coroutine-based library for concurrent Python systems programming using async/await
Name:		python-%{module}
Version:	1.6
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://github.com/dabeaz/curio/%{module}
Source:		https://files.pythonhosted.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sphinx)
# test
BuildRequires:	python3dist(pytest)

BuildArch:	noarch

%description
Curio is a coroutine-based library for concurrent Python systems programming
using async/await. It provides standard programming abstractions such as as tasks,
sockets, files, locks, and queues as well as some advanced features such as
support for structured concurrency. It works on Unix and Windows and has zero
dependencies. You'll find it to be familiar, small, fast, and fun.

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

