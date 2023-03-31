Name:		texlive-snaptodo
Version:	61155
Release:	2
Summary:	A todo that snaps to the closer side
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/snaptodo
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snaptodo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/snaptodo.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an alternative to todonotes, from which it
differs in the following ways: Depending on where you call
\snaptodo, the note is put in the left or the right margin,
whichever is closer. The notes bump each other so they never
overlap; the lines never overlap either. Aesthetic and
customizable style.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/snaptodo
%doc %{_texmfdistdir}/doc/latex/snaptodo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
