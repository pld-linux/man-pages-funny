Summary:	alt.sysadmin.recovery(and others) manual pages
Summary(pl):	Strony man z grupy alt.sysadmin.recovery (i nie tylko)
Name:		man-pages-funny
Version:	1.1
Release:	2.1
License:	distributable
Group:		Documentation
Source0:	funny-manpages_%{version}.orig.tar.gz
# Source0-md5:	7b9e70e7bab57110f381204a8e7eb347
Source1:	ftp://ftp.winternet.com/users/asr.pages.tar
# Source1-md5:	5d7596563fc8ee35b13c654a977216aa
Patch0:		funny-manpages-DEBIAN.patch
Patch1:		asr-manpages-DEBIAN.patch
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	funny-manpages

%description
A set of humorous manual pages developed on alt.sysadmin.recovery
(don't treat them seriously!). They document a set of really useful
tools that for some strange reason are not included in any
implementation of Unix. This includes such famous commands as lart,
sysadmin, luser, bosskill and others. The authors recommend these man
pages should be installed on every system. There are also other funny
manpages collected by Pawel Wiecek for Debian distribution.

%description -l pl
Zestaw humorystycznych stron manuala stworzonych na grupie
alt.sysadmin.recovery (nie traktuj jej powa¿nie!). Udokumentowano
zestaw bardzo u¿ytecznych narzêdzi niezamieszczonych z jaki¶ wa¿nych
powodów w standardowych wersjach Unix-a. S± tutaj zawarte takie
komendy jak lart, sysadmin, luser, bosskill i inne. Autorzy zalecaj±
instalacjê tych manuali na ka¿dym systemie. Jest tutaj tak¿e kilka
innych zabawnych stron manuala zebranych przez Paw³a Wiecka dla
dystrybucji Debian.

%prep
%setup -q -n funny-manpages-%{version}.orig -a 1
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man{1,2,3,8}

mv lart.1{m,}
for n in 1 2 3 8; do
	install *.$n $RPM_BUILD_ROOT%{_mandir}/man$n
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc debian/copyright
%{_mandir}/man*/*
