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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines two environments for typesetting algorithms in LaTeX2e. The
algtab environment is used to typeset an algorithm with automatically
numbered lines. The algorithm environment can be used to encapsulate the
algtab environment algorithm in a floating body together with a header,
a caption, etc. \listofalgorithms is defined.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/alg
%dir %{_datadir}/texmf-dist/source/latex/alg
%dir %{_datadir}/texmf-dist/tex/latex/alg
%doc %{_datadir}/texmf-dist/doc/latex/alg/readme.txt
%doc %{_datadir}/texmf-dist/source/latex/alg/alg.dtx
%doc %{_datadir}/texmf-dist/source/latex/alg/alg.ins
%{_datadir}/texmf-dist/tex/latex/alg/alg.sty
