%include	/usr/lib/rpm/macros.python

%define module psyco

Summary:	Python extension module which can massively speed up the execution of any Python code.
Name:		python-%{module}
Version:	1.0
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/psyco/%{module}-%{version}-src.tar.gz
# Source0-md5:	c4da85db2edf00e03f1fb3e8cd1058b5
URL:		http://psyco.sourceforge.net/
BuildRequires:	python >= 2.2.1
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
