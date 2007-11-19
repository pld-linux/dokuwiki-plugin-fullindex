%define		_plugin		fullindex
Summary:	Dokuwiki Full Index plugin
Name:		dokuwiki-plugin-%{_plugin}
Version:	1.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mtbrains.home.comcast.net/~mtbrains/products/DWAdds/fullindex.zip
# Source0-md5:	394239765433d4a418e2a8e21d73d19d
URL:		http://mtbrains.home.comcast.net/~mtbrains/products/DWAdds/index.html
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
A replacement for the built in index action of DokuWiki.
- Assign a unique page title and number to each page and namespace.
- Sort pages and namespaces by assigned numbers.
- Shows all pages in expanded view (may be too much for large wikis).
- Includes a 'level' navigation to show or hide namespaces up to a certain level.
- Graphics in front of the namespaces are clickable to collapse/expand namespaces.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
cd %{_plugin}
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_plugindir}
