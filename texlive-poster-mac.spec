# revision 18305
# category Package
# catalog-ctan /macros/generic/poster
# catalog-date 2010-05-15 22:56:34 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-poster-mac
Version:	1.1
Release:	9
Summary:	Make posters and banners with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/poster
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers macros for making posters and banners with
TeX. It is compatible with most TeX macro formats, including
Plain TeX, LaTeX, AmSTeX, and AmS-LaTeX. The package creates a
poster as huge box, which is then distributed over as many
printer pages as necessary. The only special requirement is
that your printer not be bothered by text that lies off the
page. This is true of most printers, including laser printers
and PostScript printers.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/poster-mac/poster.sty
%{_texmfdistdir}/tex/generic/poster-mac/poster.tex
%doc %{_texmfdistdir}/doc/generic/poster-mac/Changes
%doc %{_texmfdistdir}/doc/generic/poster-mac/Makefile
%doc %{_texmfdistdir}/doc/generic/poster-mac/README
%doc %{_texmfdistdir}/doc/generic/poster-mac/poster-doc.pdf
%doc %{_texmfdistdir}/doc/generic/poster-mac/poster-doc.tex
%doc %{_texmfdistdir}/doc/generic/poster-mac/poster1.pdf
%doc %{_texmfdistdir}/doc/generic/poster-mac/poster2.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 755024
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719289
- texlive-poster-mac
- texlive-poster-mac
- texlive-poster-mac
- texlive-poster-mac

