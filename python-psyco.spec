%define	module	psyco
Summary:	Python extension module which can speed up the execution of Python code
Summary(pl.UTF-8):	Moduł rozszerzenia Pythona mogący przyspieszyć wykonywanie kodu w Pythonie
Name:		python-%{module}
Version:	1.5.2
Release:	2
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/psyco/%{module}-%{version}-src.tar.gz
# Source0-md5:	bceb17423d06b573dc7b875d34e79417
URL:		http://psyco.sourceforge.net/
BuildRequires:	python >= 1:2.2.3
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{module}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.pyc
%{py_sitedir}/%{module}/*.pyo
%{py_sitedir}/%{module}/*.so
