Name:		texlive-bxjaprnind
Version:	59641
Release:	1
Summary:	Adjust the position of parentheses at paragraph head
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxjaprnind
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaprnind.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxjaprnind.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In Japanese typesetting, opening parentheses placed at the
beginning of paragraphs or lines are treated specially; for
example, while the paragraph indent before normal kanji
characters is 1em, the indent before parentheses can be 0.5em,
1em or 1.5em deoending on the local rule in effect.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxjaprnind
%doc %{_texmfdistdir}/doc/latex/bxjaprnind

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
