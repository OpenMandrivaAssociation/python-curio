Summary:	Coroutine library for concurrent Python programs
Name:		python-curio
Version:	1.6
Release:	4
License:	BSD
Group:		Development/Python
Url:		https://github.com/dabeaz/curio/curio
Source:		https://files.pythonhosted.org/packages/source/c/curio/curio-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

BuildArch:	noarch

%description
Curio is a coroutine library for concurrent Python programs.
It provides tasks, sockets, files, locks, and queues, and
supports structured concurrency. It has no runtime dependencies.

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

