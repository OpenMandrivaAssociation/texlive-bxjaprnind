%global tl_name bxjaprnind
%global tl_revision 78793

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4a
Release:	%{tl_revision}.1
Summary:	Adjust the position of parentheses at paragraph head
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/BX/bxjaprnind
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaprnind.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaprnind.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In Japanese typesetting, opening parentheses placed at the beginning of
paragraphs or lines are treated specially; for example, while the
paragraph indent before normal kanji characters is 1em, the indent
before parentheses can be 0.5em, 1em or 1.5em deoending on the local
rule in effect.

