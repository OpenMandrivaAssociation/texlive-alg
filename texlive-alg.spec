Name:		texlive-alg
Version:	15878
Release:	2
Summary:	LaTeX environments for typesetting algorithms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/alg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines two environments for typesetting algorithms in LaTeX2e.
The algtab environment is used to typeset an algorithm with
automatically numbered lines. The algorithm environment can be
used to encapsulate the algtab environment algorithm in a
floating body together with a header, a caption, etc.
\listofalgorithms is defined.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/alg/alg.sty
%doc %{_texmfdistdir}/doc/latex/alg/readme.txt
#- source
%doc %{_texmfdistdir}/source/latex/alg/alg.dtx
%doc %{_texmfdistdir}/source/latex/alg/alg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
