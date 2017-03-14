# TODO:
# - review unpackaged files

Summary:	Additional components to increase the functionality of KIO
Summary(pl.UTF-8):	Dodatkowe komponenty zwiększające funcjonalność KIO
Name:		kio-extras
Version:	16.12.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
## Source0:	http://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source0:	https://github.com/KDE/kio-extras/archive/v%{version}.tar.gz
# Source0-md5:	3fd06ac74bce60949a8d66be8937dc19
URL:		https://github.com/KDE/kio-extras
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-tools
BuildRequires:	kf5-kactivities-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-kdesignerplugin-devel
BuildRequires:	kf5-kdnssd-devel
BuildRequires:	kf5-kemoticons-devel
BuildRequires:	kf5-khtml-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemmodels-devel
BuildRequires:	kf5-kjs-devel
BuildRequires:	kf5-kpty-devel
BuildRequires:	kf5-kunitconversion-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-karchive-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	phonon-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	with_ccache

%description
Additional components to increase the functionality of KIO

%description -l pl.UTF-8
Dodatkowe komponenty zwiększające funcjonalność KIO

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

# %%find_lang %{name} --with-kde
# locolor icons are deprecated (see kde .spec-s)
rm -f $RPM_BUILD_ROOT%{_iconsdir}/locolor/*/apps/*.png
# %%{__mv} $RPM_BUILD_ROOT%{_docdir}/HTML/pt_BR $RPM_BUILD_ROOT%{_docdir}/HTML/pt

%clean
rm -rf $RPM_BUILD_ROOT

#%%files -f %{name}.lang
%files
%defattr(644,root,root,755)
# %doc AUTHORS ChangeLog FAQ README
%attr(755,root,root) %{_libdir}/libmolletnetwork5.so.*
%attr(755,root,root) %{_libdir}/qt5/plugins/*.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kded/*.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/kio/*.so
%{_datadir}/config.kcfg/jpegcreatorsettings5.kcfg
%{_datadir}/dbus-1/interfaces/kf5_org.kde.network.kioslavenotifier.xml
# TODO: No %{_datadir}/kio_bookmarks/ ?
# %{_datadir}/kio_bookmarks/kio_bookmarks.css
# TODO: No %{_datadir}/kio_docfilter/
# %{_datadir}/kio_docfilter/kio_docfilter.css
# TODO: No %{_datadir}/kio_info ?
# %{_datadir}/kio_info/kde-info2html
# %{_datadir}/kio_info/kde-info2html.conf
# TODO: no %{_datadir}/konqsidebartng/virtual_folders/remote/
# %{_datadir}/konqsidebartng/virtual_folders/remote/virtualfolder_network.desktop
# TODO: no %{_datadir}/konqueror/dirtree/remote/ ?
#%{_datadir}/konqueror/dirtree/remote/mtp-network.desktop
#%{_datadir}/konqueror/dirtree/remote/smb-network.desktop
%{_datadir}/kservices5/*.desktop
%{_datadir}/kservices5/*.protocol
%{_datadir}/kservicetypes5/thumbcreator.desktop
%{_datadir}/mime/packages/kf5_network.xml
%{_datadir}/remoteview/mtp-network.desktop
%{_datadir}/remoteview/network.desktop
%{_datadir}/remoteview/smb-network.desktop
# NOTE: this pulls whole KDE5 replacing KDE4 :/
## %{_datadir}/solid/actions/solid_mtp.desktop
