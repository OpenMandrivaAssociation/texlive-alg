%global tl_name alg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX environments for typesetting algorithms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alg
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines two environments for typesetting algorithms in LaTeX2e. The
algtab environment is used to typeset an algorithm with automatically
numbered lines. The algorithm environment can be used to encapsulate the
algtab environment algorithm in a floating body together with a header,
a caption, etc. \listofalgorithms is defined.

