%global tl_name poster-mac
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Make posters and banners with TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/poster
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/poster-mac.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers macros for making posters and banners with TeX. It is
compatible with most TeX macro formats, including Plain TeX, LaTeX,
AmSTeX, and AmS-LaTeX. The package creates a poster as huge box, which
is then distributed over as many printer pages as necessary. The only
special requirement is that your printer not be bothered by text that
lies off the page. This is true of most printers, including laser
printers and PostScript printers.

