Name:		texlive-alg
Version:	20010313
Release:	1
Summary:	LaTeX environments for typesetting algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/alg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/alg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Defines two environments for typesetting algorithms in LaTeX2e.
The algtab environment is used to typeset an algorithm with
automatically numbered lines. The algorithm environment can be
used to encapsulate the algtab environment algorithm in a
floating body together with a header, a caption, etc.
\listofalgorithms is defined.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
