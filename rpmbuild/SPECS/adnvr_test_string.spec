#
# spec file for package adnvr_incremental_update
#
# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           adnvr_test_string
Version:	5.3
Release:	1
License:	NA
Summary:	Incremental Update scripts and binaries
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Incremental Update scripts and binaries

%install
mkdir -p %{buildroot}
tar xvf ../SOURCES/%{name}.tar.gz -C %{buildroot}/
#cp ../BUILDROOT/opt/americandynamics/venvr/bin/ve-script/RP_* ../IncrementalUpdateRunZypperProcess ../IncrementalUpdateDownload %{buildroot}/opt/americandynamics/venvr/bin/ve-script/
#cp ../IncrementalUpdateStartInstallService.sh %{buildroot}/opt/americandynamics/venvr/django/rootaccess/scripts/
#cp ../adnvr_incrementalupdateinstall.service %{buildroot}/usr/lib/systemd/system/

%files
%defattr(700,root,root)
/*
#/opt/americandynamics/venvr/bin/ve-script/*IncrementalUpdate*
#/opt/americandynamics/venvr/django/rootaccess/scripts/IncrementalUpdateStartInstallService.sh
#/usr/lib/systemd/system/adnvr_incrementalupdateinstall.service
