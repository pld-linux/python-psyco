%define	module	psyco
Summary:	Python extension module which can speed up the execution of Python code
Summary(pl.UTF-8):	Moduł rozszerzenia Pythona mogący przyspieszyć wykonywanie kodu w Pythonie
Name:		python-%{module}
Version:	1.6
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/psyco/%{module}-%{version}-src.tar.gz
# Source0-md5:	8816fca8ba521e05d18dde3e1a11b0bd
URL:		http://psyco.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In short: run your existing Python software much faster, with no
change in your source.

Think of Psyco as a kind of just-in-time (JIT) compiler, a little bit
like Java's, that emit machine code on the fly instead of interpreting
your Python program step by step. The result is that your unmodified
Python programs run faster.

%description -l pl.UTF-8
W skrócie: ten moduł pozwala na o wiele szybsze działanie programów w
Pythonie bez zmian w źródłach.

Psyco jest rodzajem kompilatora JIT (just-in-time), trochę podobnego
do tego z Javy, produkującego kod maszynowy w locie zamiast
interpretowania programu w Pythonie krok po kroku. Efekt jest taki, że
programy w Pythonie bez żadnych modyfikacji działają szybciej.

%prep
%setup -q -n %{module}-%{version}

%build
CC="%{__cc}"; export CC
CFLAGS="%{rpmcflags}"; export CFLAGS
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/psyco/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{py_sitedir}/psyco
%{py_sitedir}/psyco/*.pyc
%{py_sitedir}/psyco/*.pyo
%attr(755,root,root) %{py_sitedir}/psyco/*.so
%{py_sitedir}/*.egg-info
