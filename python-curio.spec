Summary:	A coroutine-based library for concurrent Python systems programming using async/await
Name:		python-curio
Version:	1.6
Release:	1
License:	BSD
Group:		Development/Python
Url:		https://github.com/dabeaz/curio/curio
Source:		https://files.pythonhosted.org/packages/source/c/curio/curio-%{version}.tar.gz

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
%{python_sitelib}/curio/
%{python_sitelib}/curio-%{version}-py%{pyver}.*-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n curio-%{version}

%build
%py_build

%install
%py_install

