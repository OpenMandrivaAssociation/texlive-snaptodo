%global tl_name snaptodo
%global tl_revision 70676

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A todo that snaps to the closer side
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/snaptodo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snaptodo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/snaptodo.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an alternative to todonotes, from which it differs in
the following ways: Depending on where you call \snaptodo, the note is
put in the left or the right margin, whichever is closer. The notes bump
each other so they never overlap; the lines never overlap either.
Aesthetic and customizable style.

