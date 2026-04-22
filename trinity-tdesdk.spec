%bcond clang 1
%bcond gamin 1
%bcond kioslave 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_pkg tdesdk
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		The Trinity Software Development Kit (SDK)
Group:			Development/Tools/Other
Version:		14.1.5
Release:		4
URL:			http://www.trinitydesktop.org/

License:		GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/core/%{tarball_name}-%{version}.tar.xz
Source1:		%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/trinity/pkgconfig
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_DBSEARCHENGINE=ON -DWITH_KCAL=ON -DBUILD_ALL=ON
BuildOption:    -DBUILD_KIOSLAVE=%{!?with_kioslave:OFF}%{with_kioslave:ON}
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-perl-dcop >= %{version}
BuildRequires:	trinity-tdepim-devel >= %{version}

BuildRequires:	trinity-tde-cmake >= %{version}

%{!?with_clang:BuildRequires:	gcc-c++}

# ACL support
BuildRequires:	pkgconfig(libacl)

# IDN support
BuildRequires:	pkgconfig(libidn)

# GAMIN support
#  Not on openSUSE.
%{?with_gamin:BuildRequires:	gamin-devel}

# PCRE2 support
BuildRequires:	pkgconfig(libpcre2-posix)

# for kbugbuster/libkcal
BuildRequires:	desktop-file-utils

BuildRequires:  db-devel

# kbabel,  F-7+: flex >= 2.5.33-9
BuildRequires:	flex-devel

# umbrello
BuildRequires:	libxml2-devel
BuildRequires:	subversion-devel
BuildRequires:	neon-devel

# XSLT support
BuildRequires:	pkgconfig(libxslt)

# PERL support
BuildRequires:	perl

# OPENSSL support
BuildRequires:	pkgconfig(openssl)

BuildRequires:  fdupes

# PYTHON support
%define python python

BuildRequires:	%{_lib}ltdl-devel
BuildRequires:	%{_lib}binutils-devel

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Obsoletes:		trinity-kdesdk < %{EVRD}
Provides:		trinity-kdesdk = %{EVRD}
Obsoletes:		trinity-kdesdk-libs < %{EVRD}
Provides:		trinity-kdesdk-libs = %{EVRD}

Requires: trinity-cervisia = %{EVRD}
Requires: trinity-kapptemplate = %{EVRD}
Requires: trinity-kbabel = %{EVRD}
Requires: trinity-kbugbuster = %{EVRD}
Requires: trinity-tdecachegrind = %{EVRD}
Requires: trinity-tdecachegrind-converters = %{EVRD}
Requires: %{name}-kfile-plugins = %{EVRD}
Requires: %{name}-misc = %{EVRD}
Requires: %{name}-scripts = %{EVRD}
Requires: trinity-kmtrace = %{EVRD}
Requires: trinity-kompare = %{EVRD}
Requires: trinity-kspy = %{EVRD}
Requires: trinity-kuiviewer = %{EVRD}
Requires: trinity-libcvsservice0 = %{EVRD}
Requires: trinity-poxml = %{EVRD}
Requires: trinity-umbrello = %{EVRD}
%{?with_kioslave:Requires: %{name}-tdeio-plugins = %{EVRD}}
Requires: trinity-tdeunittest = %{EVRD}


%description
A collection of applications and tools used by developers, including:
* cervisia: a CVS frontend
* kbabel: PO file management
* kbugbuster: a tool to manage the TDE bug report system
* tdecachegrind: a browser for data produced by profiling tools (e.g. cachegrind)
* kompare: diff tool
* kuiviewer: displays designer's UI files
* umbrello: UML modeller and UML diagram tool

%files
%defattr(-,root,root,-)

##########

%package -n trinity-cervisia
Summary:	A graphical CVS front end for Trinity
Group:		Development/Tools/Version Control

%description -n trinity-cervisia
Cervisia is a TDE-based graphical front end for the CVS client.

As well as providing both common and advanced CVS operations, it offers
a variety of methods for graphically viewing information about the CVS
repository, your own sandbox and the relationships between different
versions of files.  A Changelog editor is also included and is coupled
with the commit dialog.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-cervisia
%defattr(-,root,root,-)
%{tde_prefix}/bin/cervisia
%{tde_prefix}/%{_lib}/libtdeinit_cervisia.la
%{tde_prefix}/%{_lib}/libtdeinit_cervisia.so
%{tde_prefix}/%{_lib}/trinity/cervisia.la
%{tde_prefix}/%{_lib}/trinity/cervisia.so
%{tde_prefix}/%{_lib}/trinity/libcervisiapart.la
%{tde_prefix}/%{_lib}/trinity/libcervisiapart.so
%{tde_prefix}/share/applications/tde/cervisia.desktop
%{tde_prefix}/share/apps/cervisia/
%{tde_prefix}/share/apps/cervisiapart/
%{tde_prefix}/share/apps/tdeconf_update/cervisia.upd
%{tde_prefix}/share/apps/tdeconf_update/cervisia-change_repos_list.pl
%{tde_prefix}/share/apps/tdeconf_update/cervisia-normalize_cvsroot.pl
%{tde_prefix}/share/apps/tdeconf_update/move_repositories.pl
%{tde_prefix}/share/apps/tdeconf_update/change_colors.pl
%{tde_prefix}/share/config.kcfg/cervisiapart.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/cervisia.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/vcs_*.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/vcs_*.svgz
%{tde_prefix}/share/man/man1/cervisia.1*
%{tde_prefix}/share/doc/tde/HTML/en/cervisia/

##########

%package -n trinity-kapptemplate
Summary:	Creates a framework to develop a Trinity application
Group:		Development/Languages/Other

%description -n trinity-kapptemplate
KAppTemplate is a shell script that will create the necessary
framework to develop various TDE applications.  It takes care of the
autoconf/automake code as well as providing a skeleton and example of
what the code typically looks like.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kapptemplate
%defattr(-,root,root,-)
%{tde_prefix}/bin/kapptemplate
%{tde_prefix}/share/apps/kapptemplate/
%{tde_prefix}/share/man/man1/kapptemplate.1*

%pre -n trinity-kapptemplate
if [ -d "%{tde_prefix}/bin/kapptemplate" ]; then
  rm -rf "%{tde_prefix}/bin/kapptemplate"
fi

##########

%package -n trinity-kbabel
Summary:	PO-file editing suite for Trinity
Group:		Development/Languages/Other

%description -n trinity-kbabel
This is a suite of programs for editing gettext message files (PO-files).
It is designed to help you translate fast and consistently.

This suite includes KBabel, CatalogManager and KBabelDict.  KBabel is an
advanced and easy to use PO-file editor with full navigational and editing
capabilities, syntax checking and statistics.  CatalogManager is a multi
functional catalog manager which allows you to keep track of many
PO-files at once.  KBabelDict is a dictionary to assist with searching
for common translations.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbabel
%defattr(-,root,root,-)
%{tde_prefix}/bin/catalogmanager
%{tde_prefix}/bin/kbabel
%{tde_prefix}/bin/kbabeldict
%{tde_prefix}/%{_lib}/libkbabelcommon.so.*
%{tde_prefix}/%{_lib}/libkbabeldictplugin.so.*
%{tde_prefix}/%{_lib}/trinity/tdefile_po.la
%{tde_prefix}/%{_lib}/trinity/tdefile_po.so
%{tde_prefix}/%{_lib}/trinity/pothumbnail.la
%{tde_prefix}/%{_lib}/trinity/pothumbnail.so
%{tde_prefix}/%{_lib}/trinity/kbabel_accelstool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_accelstool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_argstool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_argstool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_contexttool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_contexttool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_equationstool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_equationstool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_gettextexport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_gettextexport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_gettextimport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_gettextimport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_lengthtool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_lengthtool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_linguistexport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_linguistexport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_linguistimport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_linguistimport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_nottranslatedtool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_nottranslatedtool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_pluraltool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_pluraltool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_punctuationtool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_punctuationtool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_regexptool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_regexptool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_setfuzzytool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_setfuzzytool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_whitespacetool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_whitespacetool.so
%{tde_prefix}/%{_lib}/trinity/kbabel_xliffexport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_xliffexport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_xliffimport.la
%{tde_prefix}/%{_lib}/trinity/kbabel_xliffimport.so
%{tde_prefix}/%{_lib}/trinity/kbabel_xmltool.la
%{tde_prefix}/%{_lib}/trinity/kbabel_xmltool.so
%{tde_prefix}/%{_lib}/trinity/kbabeldict_dbsearchengine.la
%{tde_prefix}/%{_lib}/trinity/kbabeldict_dbsearchengine.so
%{tde_prefix}/%{_lib}/trinity/kbabeldict_poauxiliary.la
%{tde_prefix}/%{_lib}/trinity/kbabeldict_poauxiliary.so
%{tde_prefix}/%{_lib}/trinity/kbabeldict_pocompendium.la
%{tde_prefix}/%{_lib}/trinity/kbabeldict_pocompendium.so
%{tde_prefix}/%{_lib}/trinity/kbabeldict_tmxcompendium.la
%{tde_prefix}/%{_lib}/trinity/kbabeldict_tmxcompendium.so
%{tde_prefix}/share/applications/tde/catalogmanager.desktop
%{tde_prefix}/share/applications/tde/kbabel.desktop
%{tde_prefix}/share/applications/tde/kbabeldict.desktop
%{tde_prefix}/share/apps/catalogmanager/
%{tde_prefix}/share/apps/kbabel/
%{tde_prefix}/share/apps/tdeconf_update/kbabel-difftoproject.upd
%{tde_prefix}/share/apps/tdeconf_update/kbabel-project.upd
%{tde_prefix}/share/apps/tdeconf_update/kbabel-projectrename.upd
%{tde_prefix}/share/config.kcfg/kbabel.kcfg
%{tde_prefix}/share/config.kcfg/kbprojectsettings.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kbabel/
%{tde_prefix}/share/icons/hicolor/*/apps/catalogmanager.png
%{tde_prefix}/share/icons/hicolor/*/apps/kbabel.png
%{tde_prefix}/share/icons/hicolor/*/apps/kbabeldict.png
%{tde_prefix}/share/icons/locolor/*/apps/catalogmanager.png
%{tde_prefix}/share/icons/locolor/*/apps/kbabel.png
%{tde_prefix}/share/icons/locolor/*/apps/kbabeldict.png
%{tde_prefix}/share/services/dbsearchengine.desktop
%{tde_prefix}/share/services/tdefile_po.desktop
%{tde_prefix}/share/services/pothumbnail.desktop
%{tde_prefix}/share/services/kbabel_accelstool.desktop
%{tde_prefix}/share/services/kbabel_argstool.desktop
%{tde_prefix}/share/services/kbabel_contexttool.desktop
%{tde_prefix}/share/services/kbabel_equationstool.desktop
%{tde_prefix}/share/services/kbabel_gettext_export.desktop
%{tde_prefix}/share/services/kbabel_gettext_import.desktop
%{tde_prefix}/share/services/kbabel_lengthtool.desktop
%{tde_prefix}/share/services/kbabel_linguist_export.desktop
%{tde_prefix}/share/services/kbabel_linguist_import.desktop
%{tde_prefix}/share/services/kbabel_nottranslatedtool.desktop
%{tde_prefix}/share/services/kbabel_pluralformstool.desktop
%{tde_prefix}/share/services/kbabel_punctuationtool.desktop
%{tde_prefix}/share/services/kbabel_regexptool.desktop
%{tde_prefix}/share/services/kbabel_setfuzzytool.desktop
%{tde_prefix}/share/services/kbabel_whitespacetool.desktop
%{tde_prefix}/share/services/kbabel_xliff_export.desktop
%{tde_prefix}/share/services/kbabel_xliff_import.desktop
%{tde_prefix}/share/services/kbabel_xmltool.desktop
%{tde_prefix}/share/services/pocompendium.desktop
%{tde_prefix}/share/services/poauxiliary.desktop
%{tde_prefix}/share/services/tmxcompendium.desktop
%{tde_prefix}/share/servicetypes/kbabel_tool.desktop
%{tde_prefix}/share/servicetypes/kbabel_validator.desktop
%{tde_prefix}/share/servicetypes/kbabeldict_module.desktop
%{tde_prefix}/share/servicetypes/kbabelfilter.desktop
%{tde_prefix}/share/man/man1/catalogmanager.1*
%{tde_prefix}/share/man/man1/kbabel.1*
%{tde_prefix}/share/man/man1/kbabeldict.1*

##########

%package -n trinity-kbabel-devel
Summary:	PO-file editing suite for Trinity (development files)
Group:		Development/Libraries/Other
Requires:	trinity-kbabel = %{EVRD}

%description -n trinity-kbabel-devel
This is a suite of programs for editing gettext message files (PO-files).
It is designed to help you translate fast and consistently.

This suite includes KBabel, CatalogManager and KBabelDict.  KBabel is an
advanced and easy to use PO-file editor with full navigational and editing
capabilities, syntax checking and statistics.  CatalogManager is a multi
functional catalog manager which allows you to keep track of many
PO-files at once.  KBabelDict is a dictionary to assist with searching
for common translations.

This package contains the KBabel development files.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbabel-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/kbabel/
%{tde_prefix}/%{_lib}/libkbabelcommon.la
%{tde_prefix}/%{_lib}/libkbabelcommon.so
%{tde_prefix}/%{_lib}/libkbabeldictplugin.la
%{tde_prefix}/%{_lib}/libkbabeldictplugin.so

##########

%package -n trinity-kbugbuster
Summary:	A front end for the Trinity bug tracking system
Group:		Development/Languages/Other
Requires:	trinity-libkcal >= %{version}

%description -n trinity-kbugbuster
KBugBuster is a GUI front end for the TDE bug tracking system.
It allows the user to view and manipulate bug reports and provides a
variety of options for searching through reports.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kbugbuster
%defattr(-,root,root,-)
%{tde_prefix}/bin/kbugbuster
%{tde_prefix}/%{_lib}/trinity/kcal_bugzilla.la
%{tde_prefix}/%{_lib}/trinity/kcal_bugzilla.so
%{tde_prefix}/share/applications/tde/kbugbuster.desktop
%{tde_prefix}/share/apps/kbugbuster/
%{tde_prefix}/share/icons/hicolor/*/apps/kbugbuster.png
%{tde_prefix}/share/icons/locolor/*/apps/kbugbuster.png
%{tde_prefix}/share/services/tderesources/kcal/bugzilla.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kbugbuster/
%{tde_prefix}/share/man/man1/kbugbuster.1*

##########

%package -n trinity-tdecachegrind
Summary:	Visualisation tool for valgrind profiling output
Group:		Development/Languages/Other

%description -n trinity-tdecachegrind
tdecachegrind is a visualisation tool for the profiling data generated
by calltree, a profiling skin for valgrind.  Applications can be
profiled using calltree without being recompiled, and shared libraries
and plugin architectures are supported.

For visualising the output from other profiling tools, several converters
can be found in the tdecachegrind-converters package.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdecachegrind
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdecachegrind
%{tde_prefix}/share/applications/tde/tdecachegrind.desktop
%{tde_prefix}/share/apps/tdecachegrind/
%{tde_prefix}/share/icons/locolor/*/apps/tdecachegrind.png
%{tde_prefix}/share/icons/hicolor/*/apps/tdecachegrind.png
%{tde_prefix}/share/mimelnk/application/x-tdecachegrind.desktop
%{tde_prefix}/share/doc/tde/HTML/en/tdecachegrind/
%{tde_prefix}/share/man/man1/tdecachegrind.1*

##########

%package -n trinity-tdecachegrind-converters
Summary:	Format converters for tdecachegrind profiling visualisation tool
Group:		Development/Languages/Other
Requires:	%{python}
Requires:	php-cli

%description -n trinity-tdecachegrind-converters
This is a collection of scripts for converting the output from
different profiling tools into a format that tdecachegrind can use.

tdecachegrind is a visualisation tool for the profiling data generated
by calltree, a profiling skin for valgrind.  Applications can be
profiled using calltree without being recompiled, and shared libraries
and plugin architectures are supported.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdecachegrind-converters
%defattr(-,root,root,-)
%{tde_prefix}/bin/dprof2calltree
%{tde_prefix}/bin/hotshot2calltree
%{tde_prefix}/bin/memprof2calltree
%{tde_prefix}/bin/op2calltree
%{tde_prefix}/bin/pprof2calltree
%{tde_prefix}/share/man/man1/dprof2calltree.1*
%{tde_prefix}/share/man/man1/hotshot2calltree.1*
%{tde_prefix}/share/man/man1/memprof2calltree.1*
%{tde_prefix}/share/man/man1/op2calltree.1*
%{tde_prefix}/share/man/man1/pprof2calltree.1*

##########

%package kfile-plugins
Summary:	Trinity file dialog plugins for software development files
Group:		Development/Languages/Other

%description kfile-plugins
This is a collection of plugins for the TDE file dialog.  These plugins
extend the file dialog to offer advanced meta-information for source files,
patch files and Qt Linguist data.

This package is part of Trinity, and a component of the TDE SDK module.

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdefile_cpp.so
%{tde_prefix}/%{_lib}/trinity/tdefile_cpp.la
%{tde_prefix}/%{_lib}/trinity/tdefile_diff.so
%{tde_prefix}/%{_lib}/trinity/tdefile_diff.la
%{tde_prefix}/%{_lib}/trinity/tdefile_ts.so
%{tde_prefix}/%{_lib}/trinity/tdefile_ts.la
%{tde_prefix}/share/services/tdefile_cpp.desktop
%{tde_prefix}/share/services/tdefile_diff.desktop
%{tde_prefix}/share/services/tdefile_h.desktop
%{tde_prefix}/share/services/tdefile_ts.desktop

##########

%package misc
Summary:	Various goodies from the Trinity Software Development Kit
Group:		Development/Languages/Other

%description misc
This package contains miscellaneous goodies provided with the official
TDE release to assist with TDE software development.

Included are:
- headers to assist with profiling TDE code;
- a widget style for checking conformity with the TDE/Qt style guide;
- palettes that match the KDE standard colour palette;
- a TDE address book plugin that reads the list of TDE CVS accounts.

This package is part of Trinity, and a component of the TDE SDK module.

%files misc
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdeabcformat_kdeaccounts.la
%{tde_prefix}/%{_lib}/trinity/tdeabcformat_kdeaccounts.so
%{tde_prefix}/%{_lib}/trinity/plugins/styles/scheck.so
%{tde_prefix}/%{_lib}/trinity/plugins/styles/scheck.la
%{tde_prefix}/share/apps/tdeabc/formats/kdeaccountsplugin.desktop
%{tde_prefix}/share/apps/tdestyle/themes/scheck.themerc
%{tde_prefix}/share/kdepalettes/

%{tde_prefix}/%{_lib}/libkstartperf.so.*
%{tde_prefix}/%{_lib}/libkstartperf.la
%{tde_prefix}/bin/kstartperf

##########

%package scripts
Summary:	a set of useful development scripts for Trinity
Group:		Development/Languages/Other
Requires:	%{python}

%description scripts
This package contains a number of scripts which can be used to help in
developing TDE-based applications.  Many of these scripts however are
not specific to TDE, and in particular there are several general-use
scripts to help users in working with SVN and CVS repositories.

In addition to these scripts, this package provides:
- gdb macros for Qt/TDE programming;
- vim and emacs helper files for Qt/TDE programming;
- bash and zsh completion controls for TDE apps;
- valgrind error suppressions for TDE apps.

This package is part of Trinity, and a component of the TDE SDK module.

%files scripts
%defattr(-,root,root,-)
%{tde_prefix}/bin/adddebug
%{tde_prefix}/bin/build-progress.sh
%{tde_prefix}/bin/cheatmake
%{tde_prefix}/bin/create_cvsignore
%{tde_prefix}/bin/create_makefile
%{tde_prefix}/bin/create_makefiles
%{tde_prefix}/bin/cvs-clean
%{tde_prefix}/bin/cvs2dist
%{tde_prefix}/bin/cvsbackport
%{tde_prefix}/bin/cvsblame
%{tde_prefix}/bin/cvscheck
%{tde_prefix}/bin/cvsforwardport
%{tde_prefix}/bin/cvslastchange
%{tde_prefix}/bin/cvslastlog
%{tde_prefix}/bin/cvsrevertlast
%{tde_prefix}/bin/cvsversion
%{tde_prefix}/bin/cxxmetric
%{tde_prefix}/bin/extend_dmalloc
%{tde_prefix}/bin/extractattr
%{tde_prefix}/bin/extractrc
%{tde_prefix}/bin/findmissingcrystal
%{tde_prefix}/bin/fixkdeincludes
%{tde_prefix}/bin/fixuifiles
%{tde_prefix}/bin/includemocs
%{tde_prefix}/bin/kde-build
%{tde_prefix}/bin/kdedoc
%{tde_prefix}/bin/tdekillall
%{tde_prefix}/bin/kdelnk2desktop.py*
%{tde_prefix}/bin/kdemangen.pl
%{tde_prefix}/bin/makeobj
%{tde_prefix}/bin/noncvslist
%{tde_prefix}/bin/package_crystalsvg
%{tde_prefix}/bin/png2mng.pl
%{tde_prefix}/bin/pruneemptydirs
%{tde_prefix}/bin/qtdoc
%{tde_prefix}/bin/zonetab2pot.py*
%{tde_prefix}/bin/svn2dist
%{tde_prefix}/bin/svnrevertlast
%{tde_prefix}/bin/svnforwardport
%{tde_prefix}/bin/nonsvnlist
%{tde_prefix}/bin/tdesvn-build
%{tde_prefix}/bin/svnlastlog
%{tde_prefix}/bin/svnversions
%{tde_prefix}/bin/create_svnignore
%{tde_prefix}/bin/svnlastchange
%{tde_prefix}/bin/colorsvn
%{tde_prefix}/bin/svnaddcurrentdir
%{tde_prefix}/bin/svnbackport
%{tde_prefix}/bin/svngettags
%{tde_prefix}/bin/svnchangesince
%{tde_prefix}/bin/svn-clean
%{tde_prefix}/share/apps/katepart/syntax/tdesvn-buildrc.xml
%{tde_prefix}/share/man/man1/adddebug.1*
%{tde_prefix}/share/man/man1/build-progress.sh.1*
%{tde_prefix}/share/man/man1/cheatmake.1*
%{tde_prefix}/share/man/man1/create_cvsignore.1*
%{tde_prefix}/share/man/man1/create_makefile.1*
%{tde_prefix}/share/man/man1/create_makefiles.1*
%{tde_prefix}/share/man/man1/cvsblame.1*
%{tde_prefix}/share/man/man1/cvscheck.1*
%{tde_prefix}/share/man/man1/cvs-clean.1*
%{tde_prefix}/share/man/man1/cvs2dist.1*
%{tde_prefix}/share/man/man1/cvsaskpass.1*
%{tde_prefix}/share/man/man1/cvsbackport.1*
%{tde_prefix}/share/man/man1/cvsforwardport.1*
%{tde_prefix}/share/man/man1/cvslastchange.1*
%{tde_prefix}/share/man/man1/cvslastlog.1*
%{tde_prefix}/share/man/man1/cvsrevertlast.1*
%{tde_prefix}/share/man/man1/cvsservice.1*
%{tde_prefix}/share/man/man1/cvsversion.1*
%{tde_prefix}/share/man/man1/cxxmetric.1*
%{tde_prefix}/share/man/man1/extend_dmalloc.1*
%{tde_prefix}/share/man/man1/extractattr.1*
%{tde_prefix}/share/man/man1/extractrc.1*
%{tde_prefix}/share/man/man1/findmissingcrystal.1*
%{tde_prefix}/share/man/man1/fixkdeincludes.1*
%{tde_prefix}/share/man/man1/fixuifiles.1*
%{tde_prefix}/share/man/man1/includemocs.1*
%{tde_prefix}/share/man/man1/kde-build.1*
%{tde_prefix}/share/man/man1/kdedoc.1*
%{tde_prefix}/share/man/man1/kdelnk2desktop.py.1*
%{tde_prefix}/share/man/man1/kdemangen.pl.1*
%{tde_prefix}/share/man/man1/licensecheck.1*
%{tde_prefix}/share/man/man1/noncvslist.1*
%{tde_prefix}/share/man/man1/makeobj.1*
%{tde_prefix}/share/man/man1/package_crystalsvg.1*
%{tde_prefix}/share/man/man1/png2mng.pl.1
%{tde_prefix}/share/man/man1/pruneemptydirs.1
%{tde_prefix}/share/man/man1/qtdoc.1*
%{tde_prefix}/share/man/man1/tdekillall.1*
%{tde_prefix}/share/man/man1/tdesvn-build.1*
%{tde_prefix}/share/man/man1/zonetab2pot.py.1*
%{tde_prefix}/share/doc/tde/HTML/en/tdesvn-build/
#scripts/kde-devel-gdb /opt/trinity/share/tdesdk-scripts
#scripts/kde-devel-vim.vim /opt/trinity/share/tdesdk-scripts
#scripts/kde-emacs/*.el /opt/trinity/share/emacs/site-lisp/tdesdk-scripts
#scripts/kde.supp /opt/trinity/lib/valgrind
#scripts/completions /opt/trinity/share/tdesdk-scripts

#debian/desktop-i18n/createdesktop.pl /opt/trinity/lib/kubuntu-desktop-i18n/
#debian/desktop-i18n/findfiles /opt/trinity/lib/kubuntu-desktop-i18n/
#debian/desktop-i18n/msgsplit /opt/trinity/lib/kubuntu-desktop-i18n/

%if "%{?tde_prefix}" != "/usr"
%{tde_prefix}/bin/licensecheck
%else
%exclude %{tde_prefix}/bin/licensecheck
%endif

##########

%package -n trinity-kmtrace
Summary:	A Trinity memory leak tracer
Group:		Development/Languages/Other
Requires:	less

%description -n trinity-kmtrace
KMtrace is a TDE tool to assist with malloc debugging using glibc's
"mtrace" functionality.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kmtrace
%defattr(-,root,root,-)
%{tde_prefix}/bin/demangle
%{tde_prefix}/bin/kminspector
%{tde_prefix}/bin/kmmatch
%{tde_prefix}/bin/kmtrace
%dir %{tde_prefix}/%{_lib}/kmtrace
%{tde_prefix}/%{_lib}/kmtrace/libktrace.la
%{tde_prefix}/%{_lib}/kmtrace/libktrace.so
%{tde_prefix}/share/apps/kmtrace/
%{tde_prefix}/share/man/man1/demangle.1*
%{tde_prefix}/share/man/man1/kminspector.1*
%{tde_prefix}/share/man/man1/kmmatch.1*
%{tde_prefix}/share/man/man1/kmtrace.1*

##########

%package -n trinity-kompare
Summary:	A Trinity GUI for viewing differences between files
Group:		Development/Languages/Other

%description -n trinity-kompare
Kompare is a graphical user interface for viewing the differences between
files.  It can compare two documents, create a diff file, display a diff
file and/or blend a diff file back into the original documents.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kompare
%defattr(-,root,root,-)
%{tde_prefix}/bin/kompare
%{tde_prefix}/%{_lib}/libkompareinterface.la
%{tde_prefix}/%{_lib}/libkompareinterface.so.*
%{tde_prefix}/%{_lib}/trinity/libkomparenavtreepart.la
%{tde_prefix}/%{_lib}/trinity/libkomparenavtreepart.so
%{tde_prefix}/%{_lib}/trinity/libkomparepart.la
%{tde_prefix}/%{_lib}/trinity/libkomparepart.so
%{tde_prefix}/share/applications/tde/kompare.desktop
%{tde_prefix}/share/apps/kompare/
%{tde_prefix}/share/services/komparenavtreepart.desktop
%{tde_prefix}/share/services/komparepart.desktop
%{tde_prefix}/share/servicetypes/komparenavigationpart.desktop
%{tde_prefix}/share/servicetypes/kompareviewpart.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kompare.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/kompare.svgz
%{tde_prefix}/share/doc/tde/HTML/en/kompare/
%{tde_prefix}/share/man/man1/kompare.1*

##########

%package -n trinity-kspy
Summary:	Examines the internal state of a Qt/TDE app
Group:		Development/Languages/Other
Requires:	trinity-tdelibs-devel

%description -n trinity-kspy
KSpy is a tiny library which can be used to graphically display
the QObjects in use by a Qt/TDE app.  In addition to the object tree,
you can also view the properties, signals and slots of any QObject.

Basically it provides much the same info as QObject::dumpObjectTree() and
QObject::dumpObjectInfo(), but in a much more convenient form.  KSpy has
minimal overhead for the application, because the kspy library is
loaded dynamically using KLibLoader.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kspy
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkspy.la
%{tde_prefix}/%{_lib}/libkspy.so.*
%{tde_prefix}/share/man/man1/testkspy.1*

##########

%package -n trinity-kuiviewer
Summary:	Viewer for Qt Designer user interface files
Group:		Development/Languages/Other

%description -n trinity-kuiviewer
KUIViewer is a utility to display and test the user interface (.ui) files
generated by Qt Designer.  The interfaces can be displayed in a variety of
different widget styles.

The Qt Designer itself is in the package qt3-designer.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-kuiviewer
%defattr(-,root,root,-)
%{tde_prefix}/bin/kuiviewer
%{tde_prefix}/%{_lib}/trinity/libkuiviewerpart.so
%{tde_prefix}/%{_lib}/trinity/libkuiviewerpart.la
%{tde_prefix}/%{_lib}/trinity/quithumbnail.so
%{tde_prefix}/%{_lib}/trinity/quithumbnail.la
%{tde_prefix}/share/applications/tde/kuiviewer.desktop
%{tde_prefix}/share/apps/kuiviewer/
%{tde_prefix}/share/apps/kuiviewerpart/
%{tde_prefix}/share/icons/hicolor/*/apps/kuiviewer.png
%{tde_prefix}/share/icons/locolor/*/apps/kuiviewer.png
%{tde_prefix}/share/services/designerthumbnail.desktop
%{tde_prefix}/share/services/kuiviewer_part.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kuiviewer/
%{tde_prefix}/share/man/man1/kuiviewer.1*

##########

%package -n trinity-libcvsservice0
Summary:	DCOP service for accessing CVS repositories
Group:		Development/Languages/Other
Requires:	cvs

%description -n trinity-libcvsservice0
This library provides a DCOP service for accessing and working with
remote CVS repositories.  Applications may link with this library to
access the DCOP service directly from C++.  Alternatively, scripts may
access the service using the standard "dcop" command-line tool.

DCOP is the Desktop Communication Protocol used throughout TDE.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-libcvsservice0
%defattr(-,root,root,-)
%{tde_prefix}/bin/cvsaskpass
%{tde_prefix}/bin/cvsservice
%{tde_prefix}/%{_lib}/libcvsservice.so.*
%{tde_prefix}/%{_lib}/libtdeinit_cvsaskpass.so
%{tde_prefix}/%{_lib}/libtdeinit_cvsservice.so
%{tde_prefix}/%{_lib}/trinity/cvsaskpass.la
%{tde_prefix}/%{_lib}/trinity/cvsaskpass.so
%{tde_prefix}/%{_lib}/trinity/cvsservice.la
%{tde_prefix}/%{_lib}/trinity/cvsservice.so
%{tde_prefix}/share/services/cvsservice.desktop

##########

%package -n trinity-libcvsservice-devel
Summary:	Development files for CVS DCOP service
Group:		Development/Libraries/Other
Requires:	trinity-libcvsservice0 = %{EVRD}

%description -n trinity-libcvsservice-devel
The library libcvsservice provides a DCOP service for accessing and
working with remote CVS repositories.  Applications may link with this
library to access the DCOP service directly from C++.  Alternatively,
scripts may access the service using the standard "dcop" command-line
tool.

Development files for libcvsservice are included in this package.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-libcvsservice-devel
%defattr(-,root,root,-)
%{tde_prefix}/include/tde/cvsjob_stub.h
%{tde_prefix}/include/tde/cvsservice_stub.h
%{tde_prefix}/include/tde/repository_stub.h
%{tde_prefix}/%{_lib}/libcvsservice.la
%{tde_prefix}/%{_lib}/libcvsservice.so
%{tde_prefix}/%{_lib}/libtdeinit_cvsaskpass.la
%{tde_prefix}/%{_lib}/libtdeinit_cvsservice.la
%{tde_prefix}/share/cmake/cervisia.cmake

##########

%package -n trinity-poxml
Summary:	Tools for using PO-files to translate DocBook XML files
Group:		Development/Languages/Other

%description -n trinity-poxml
This is a collection of tools that facilitate translating DocBook XML
files using gettext message files (PO-files).

Also included are some miscellaneous command-line utilities for
manipulating DocBook XML files, PO-files and PO-template files.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-poxml
%defattr(-,root,root,-)
%{tde_prefix}/bin/po2xml
%{tde_prefix}/bin/split2po
%{tde_prefix}/bin/swappo
%{tde_prefix}/bin/transxx
%{tde_prefix}/bin/xml2pot
%{tde_prefix}/share/man/man1/po2xml.1*
%{tde_prefix}/share/man/man1/split2po.1*
%{tde_prefix}/share/man/man1/swappo.1*
%{tde_prefix}/share/man/man1/transxx.1*
%{tde_prefix}/share/man/man1/xml2pot.1*

##########

%package -n trinity-umbrello
Summary:	UML modelling tool and code generator
Group:		Development/Languages/Other

%description -n trinity-umbrello
Umbrello UML Modeller is a Unified Modelling Language editor for TDE.
With UML you can create diagrams of software and other systems in an
industry standard format.  Umbrello can also generate code from your
UML diagrams in a number of programming languages.

The program supports class diagrams, sequence diagrams, collaboration
diagrams, use case diagrams, state diagrams, activity diagrams, component
diagrams and deployment diagrams.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-umbrello
%defattr(-,root,root,-)
%{tde_prefix}/bin/umbodoc
%{tde_prefix}/bin/umbrello
%{tde_prefix}/share/applications/tde/umbrello.desktop
%{tde_prefix}/share/apps/umbrello/
%{tde_prefix}/share/icons/crystalsvg/*/actions/umbrello_*.png
%{tde_prefix}/share/icons/crystalsvg/*/mimetypes/umbrellofile.png
%{tde_prefix}/share/icons/crystalsvg/scalable/mimetypes/umbrellofile.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/umbrello.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/umbrello.svgz
%{tde_prefix}/share/icons/hicolor/*/mimetypes/umbrellofile.png
%{tde_prefix}/share/mimelnk/application/x-umbrello.desktop
%{tde_prefix}/share/doc/tde/HTML/en/umbrello/
%{tde_prefix}/share/man/man1/umbrello.1*

##########

%if %{with kioslave}

%package tdeio-plugins
Summary:	Subversion ioslave for Trinity
Group:		Development/Languages/Other
Requires:	subversion

Obsoletes:	trinity-tdesdk-kio-plugins < %{EVRD}
Provides:	trinity-tdesdk-kio-plugins = %{EVRD}

%description tdeio-plugins
This package provides easy access to remote SVN repositories from within
Konqueror, and TDE generally, by browsing them as if they were a
filesystem, using URLs like svn://hostname/path, or svn+ssh://, etc.

This package is part of Trinity, and a component of the TDE SDK module.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdeio_svn_helper
%{tde_prefix}/%{_lib}/trinity/kded_ksvnd.la
%{tde_prefix}/%{_lib}/trinity/kded_ksvnd.so
%{tde_prefix}/%{_lib}/trinity/tdeio_svn.la
%{tde_prefix}/%{_lib}/trinity/tdeio_svn.so
%{tde_prefix}/share/apps/konqueror/servicemenus/subversion_toplevel.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/subversion.desktop
%{tde_prefix}/share/services/kded/ksvnd.desktop
%{tde_prefix}/share/services/svn+file.protocol_tdesdk
%{tde_prefix}/share/services/svn+http.protocol_tdesdk
%{tde_prefix}/share/services/svn+https.protocol_tdesdk
%{tde_prefix}/share/services/svn+ssh.protocol_tdesdk
%{tde_prefix}/share/services/svn.protocol_tdesdk
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_switch.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_merge.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_branch.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_remove.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_add.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/svn_status.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_add.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_status.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_remove.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_switch.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_branch.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/svn_merge.svgz

%post tdeio-plugins
for proto in svn+file svn+http svn+https svn+ssh svn; do
  update-alternatives --install \
    %{tde_prefix}/share/services/${proto}.protocol \
    ${proto}.protocol \
    %{tde_prefix}/share/services/${proto}.protocol_tdesdk \
    10
done

%preun tdeio-plugins
if [ $1 -eq 0 ]; then
  for proto in svn+file svn+http svn+https svn+ssh svn; do
    update-alternatives --remove \
      ${proto}.protocol \
      %{tde_prefix}/share/services/${proto}.protocol_tdesdk || :
  done
fi

%endif

##########

%package -n trinity-tdeunittest
Summary:	Unit testing library for Trinity
Group:		Development/Languages/Other

Obsoletes:	trinity-kunittest < %{EVRD}
Provides:	trinity-kunittest = %{EVRD}

%description -n trinity-tdeunittest
tdeunittest is a small library that facilitates the writing of tests for
TDE developers. There are two ways to use the tdeunittest library. One is
to create dynamically loadable modules and use the tdeunittestmodrunner or
tdeunittestguimodrunner programs to run the tests. The other is to use the
libraries to create your own testing application.

This package is part of Trinity, and a component of the TDE SDK module.

%files -n trinity-tdeunittest
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdeunittest
%{tde_prefix}/bin/tdeunittest_debughelper
%{tde_prefix}/bin/tdeunittestmod
%{tde_prefix}/bin/tdeunittestguimodrunner
%{tde_prefix}/%{_lib}/libtdeunittestgui.la
%{tde_prefix}/%{_lib}/libtdeunittestgui.so.*

##########

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries/Other

Requires:	%{name} = %{EVRD}
Requires:	trinity-kbabel-devel = %{EVRD}
Requires:	%{name}-misc = %{EVRD}
Requires:	trinity-kspy = %{EVRD}
Requires:	trinity-kmtrace = %{EVRD}
Requires:	trinity-tdeunittest = %{EVRD}
Requires:	trinity-libcvsservice-devel = %{EVRD}
Requires:	trinity-kompare = %{EVRD}

Obsoletes:	trinity-kdesdk-devel < %{EVRD}
Provides:	trinity-kdesdk-devel = %{EVRD}

%description devel
This package contains the development files for tdesdk.

%files devel
%defattr(-,root,root,-)
# misc
%{tde_prefix}/include/tde/kprofilemethod.h
%{tde_prefix}/%{_lib}/libkstartperf.so
# kspy
%{tde_prefix}/include/tde/kspy.h
%{tde_prefix}/%{_lib}/libkspy.so
# kmtrace
%{tde_prefix}/%{_lib}/kmtrace/libktrace_s.a
%{tde_prefix}/include/tde/ktrace.h
# tdeunittest
%{tde_prefix}/%{_lib}/libtdeunittestgui.so
%{tde_prefix}/include/tde/tdeunittest/runnergui.h
# kompare
%{tde_prefix}/%{_lib}/libkompareinterface.so


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"

%install -a
# Installs kdepalettes
%__install -D -m 644 kdepalettes/kde_xpaintrc %{?buildroot}%{tde_prefix}/share/kdepalettes/kde_xpaintrc
%__install -D -m 644 kdepalettes/KDE_Gimp %{?buildroot}%{tde_prefix}/share/kdepalettes/KDE_Gimp
%__install -D -m 644 kdepalettes/README %{?buildroot}%{tde_prefix}/share/kdepalettes/README

# Installs SVN protocols as alternatives
%if %{with kioslave}
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+file.protocol %{?buildroot}%{tde_prefix}/share/services/svn+file.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+http.protocol %{?buildroot}%{tde_prefix}/share/services/svn+http.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+https.protocol %{?buildroot}%{tde_prefix}/share/services/svn+https.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn+ssh.protocol %{?buildroot}%{tde_prefix}/share/services/svn+ssh.protocol_tdesdk
%__mv -f %{?buildroot}%{tde_prefix}/share/services/svn.protocol %{?buildroot}%{tde_prefix}/share/services/svn.protocol_tdesdk
%endif

# Removes useless stuff
%__rm -f %{?buildroot}%{tde_prefix}/share/apps/kapptemplate/admin/debianrules

# Fix permissions
chmod 644 %{?buildroot}%{tde_prefix}/share/apps/kapptemplate/admin/Doxyfile.global

# Make kapptemplate archive
pushd  %{?buildroot}%{tde_prefix}/share/apps/kapptemplate
mkdir kapptemplate
mv admin appframework bin existing include kapp kpartapp kpartplugin kapptemplate/
tar cfz kapptemplate.tar.gz kapptemplate
rm -rf kapptemplate
popd

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

