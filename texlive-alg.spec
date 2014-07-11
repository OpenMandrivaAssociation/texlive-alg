# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/alg
# catalog-date 2006-12-17 11:41:28 +0100
# catalog-license lppl
# catalog-version 2001-03-13
Name:		texlive-alg
Version:	20010313
Release:	8
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20010313-2
+ Revision: 749157
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20010313-1
+ Revision: 717810
- texlive-alg
- texlive-alg
- texlive-alg
- texlive-alg
- texlive-alg

