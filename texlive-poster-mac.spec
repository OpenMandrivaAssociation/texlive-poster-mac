Name:		texlive-poster-mac
Version:	18305
Release:	2
Summary:	Make posters and banners with TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/poster
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
