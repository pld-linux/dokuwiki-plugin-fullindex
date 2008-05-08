%define		plugin		fullindex
Summary:	DokuWiki Full Index plugin
Summary(pl.UTF-8):	Wtyczka Full Index (pełnego indeksu) dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mtbrains.home.comcast.net/~mtbrains/products/DWAdds/fullindex.zip
# Source0-md5:	394239765433d4a418e2a8e21d73d19d
URL:		http://mtbrains.home.comcast.net/~mtbrains/products/DWAdds/index.html
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
A replacement for the built in index action of DokuWiki.
- Assign a unique page title and number to each page and namespace.
- Sort pages and namespaces by assigned numbers.
- Shows all pages in expanded view (may be too much for large wikis).
- Includes a 'level' navigation to show or hide namespaces up to a certain
  level.
- Graphics in front of the namespaces are clickable to collapse/expand
  namespaces.

%description -l pl.UTF-8
Zamiennik dla wbudowanego indeksu z DokuWiki:
- przyporządkowuje unikalny tytuł i numer strony do każdej strony i
  przestrzeni nazw;
- sortuje strony i przestrzenie nazw po przypisanych numerach;
- pokazuje wszystkie strony w rozwiniętym widoku (może być zbyt duży
  dla wielkich wiki);
- zawiera nawigację "poziomową" pokazującą lub ukrywającą przestrzenie
  nazw do określonego poziomu;
- obrazki przed przestrzeniami nazw służą do zwijania i rozwijania
  przestrzeni nazw.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
cd %{plugin}
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{plugindir}
