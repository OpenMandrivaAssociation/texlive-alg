# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/alg
# catalog-date 2006-12-17 11:41:28 +0100
# catalog-license lppl
# catalog-version 2001-03-13
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/alg/alg.sty
%doc %{_texmfdistdir}/doc/latex/alg/readme.txt
#- source
%doc %{_texmfdistdir}/source/latex/alg/alg.dtx
%doc %{_texmfdistdir}/source/latex/alg/alg.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
