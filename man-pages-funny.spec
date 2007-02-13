Summary:	alt.sysadmin.recovery(and others) manual pages
Summary(pl.UTF-8):	Strony man z grupy alt.sysadmin.recovery(i nie tylko)
Name:		man-pages-funny
Version:	1.1
Release:	5
License:	distributable
Group:		Documentation
Source0:	funny-manpages_%{version}.orig.tar.gz
# Source0-md5:	7b9e70e7bab57110f381204a8e7eb347
Source1:	ftp://ftp.winternet.com/users/asr.pages.tar
# Source1-md5:	5d7596563fc8ee35b13c654a977216aa
Source2:	%{name}-google-en.7
Source3:	%{name}-google-pl.7
Patch0:		funny-manpages-DEBIAN.patch
Patch1:		asr-manpages-DEBIAN.patch
Conflicts:	xscreensaver <= 1:4.16-2
Obsoletes:	funny-manpages
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of humorous manual pages developed on alt.sysadmin.recovery
(don't treat them seriously!). They document a set of really useful
tools that for some strange reason are not included in any
implementation of Unix. This includes such famous commands as lart,
sysadmin, luser, bosskill and others. The authors recommend these man
pages should be installed on every system. There are also other funny
manpages collected by Pawel Wiecek for Debian distribution.

%description -l pl.UTF-8
Zestaw humorystycznych stron manuala stworzonych na grupie
alt.sysadmin.recovery (nie traktuj jej poważnie!). Udokumentowano
zestaw bardzo użytecznych narzędzi niezamieszczonych z jakiś ważnych
powodów w standardowych wersjach Unix-a. Są tutaj zawarte takie
komendy jak lart, sysadmin, luser, bosskill i inne. Autorzy zalecają
instalację tych manuali na każdym systemie. Jest tutaj także kilka
innych zabawnych stron manuala zebranych przez Pawła Więcka dla
dystrybucji Debian.

%prep
%setup -q -n funny-manpages-%{version}.orig -a 1
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}{/man{1,2,3,7,8},/pl/man7}

mv lart.1{m,}
for n in 1 2 3 8; do
	install *.$n $RPM_BUILD_ROOT%{_mandir}/man$n
done
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man7/google.7
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man7/google.7

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/copyright
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man?/*
