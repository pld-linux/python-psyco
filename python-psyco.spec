%include	/usr/lib/rpm/macros.python
%define	module	psyco
Summary:	Python extension module which can speed up the execution of Python code
Summary(pl):	Modu³ rozszerzenia Pythona mog±cy przyspieszyæ wykonywanie kodu w Pythonie
Name:		python-%{module}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/psyco/%{module}-%{version}-src.tar.gz
# Source0-md5:	2b12983f5a56a9fafe010b54ef514770
URL:		http://psyco.sourceforge.net/
BuildRequires:	python >= 2.2.3
%pyrequires_eq	python-modules
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In short: run your existing Python software much faster, with no
change in your source.

Think of Psyco as a kind of just-in-time (JIT) compiler, a little bit
like Java's, that emit machine code on the fly instead of interpreting
your Python program step by step. The result is that your unmodified
Python programs run faster.

%description -l pl
W skrócie: ten modu³ pozwala na o wiele szybsze dzia³anie programów w
Pythonie bez zmian w ¼ród³ach.

Psyco jest rodzajem kompilatora JIT (just-in-time), trochê podobnego
do tego z Javy, produkuj±cego kod maszynowy w locie zamiast
interpretowania programu w Pythonie krok po kroku. Efekt jest taki, ¿e
programy w Pythonie bez ¿adnych modyfikacji dzia³aj± szybciej.

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
