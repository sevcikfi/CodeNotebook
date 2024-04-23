---
alias:
tag: IT/linux CodeNotebook
---

# RPM

## package

### naming convention

`<name>-<version>-<release>.<arch>.rpm`

### prereq

Requireid: `rpmdevtools rpmlint`

Useful: `tree`

### Setup file tree

`rpmdev-setuptree` sets up file tree in home folder of current user or alternatively use.

`mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}` in directory other than in user's home folder.

```text
rpmbuild/
├── BUILD
├── RPMS
├── SOURCES
├── SPECS
└── SRPMS
```

- The **BUILD** directory is used during the build process of the RPM package, ideal for temp files and similar.
- The **RPMS** directory holds RPM packages built for different architectures and noarch if specified in .spec file or during the build.
- The **SOURCES** directory holds sources. This can be a simple script, a complex C project that needs to be compiled, a pre-compiled program, etc. Usually, the sources are compressed as .tar.gz or .tgz files.
- The **SPEC** directory contains the .spec files. The .spec file defines how a package is built.
- The **SRPMS** directory holds the .src.rpm packages. A Source RPM package doesn't belong to an architecture or distribution. The actual .rpm package build is based on the .src.rpm package.

### spec file

#### spec file macros

Built-in:

```bash
%_prefix /usr
%_exec_prefix %{_prefix}
%_bindir %{_exec_prefix}/bin
%_sbindir %{_exec_prefix}/sbin
%_libexecdir %{_exec_prefix}/libexec
%_datadir %{_prefix}/share
%_sysconfdir %{_prefix}/etc
%_sharedstatedir %{_prefix}/com
%_localstatedir %{_prefix}/var
%_libdir %{_exec_prefix}/lib
%_includedir %{_prefix}/include
%_oldincludedir /usr/include
%_infodir %{_prefix}/info
%_mandir %{_prefix}/man

%description # multiline description
%changelog   # multiline changelog
%license #license file
%docs #docs file

```

User defined and possible combinations:

```bash
%define major_version 1
%define minor_version 4
%define micro_version 4
%define prog_name     elasticsearch
%define prog_dir      /var/lib/elasticsearch

#->

Version: %{major_version}.%{minor_version}.%{micro_version}
```

Flow of execution:

- `%prep` - Code executed before build process.\
- `%build` - Build code.
- `%clean` - post built clean up.
- `%pre` - This is where code is run before the install scripts run.
- `%install` - Install code.
- `%preun` – The section where code is executed prior to uninstall.
- `%post` – Section for code to be executed after installation.
- `%postun` – Section for code to be executed after uninstallation.
- `%files` - This section declares which files and directories are owned by the package, and thus which files and directories will be placed into the binary RPM.

### useful command

All may be run both on *installed* package e.g. `rpm -qi nginx` or specific not yet installed `.rpm`

Options for `rpm`:

- `-q` required for queries below
- `-p` specifies the package
- `-i` inspects the spec file
- `-l` list the files in the package with absolute path
- `-v` list the files in long format

Useful combo:

- `rpm -qi` shows only the spec file
- `rpm -ql` to list the files
- `rpm -qpivl --changelog --nomanifest` prints out spec file, files in the package and changelog

### hello-world package

1. Create `hello.sh` with following content

    ```bash
    #!/bin/sh
    echo "Hello world"
    ```

2. Copy it into folder with semantic versioning and tar it

    ```bash
    mkdir hello-0.0.1
    cp hello.sh hello-0.0.1
    tar czvf hello-0.0.1.tar.gz hello-0.0.1/
    ```

3. Create and edit spec file

    ```bash
    rpmdev-newspec SPECS/hello.spec
    vim/nano SPECS/hello.spec
    ```

    Optionally run `rpmlint /path/to/spec` to catch errors.

4. Build the rpm package

- b to build
- s source
- b binary
- a both

    ```bash
    rpmbuild -ba SPECS/hello.spec
    ```

## repo

### prereqs

Required: `createrepo rpm-build rpm-sign yum-utils gpg pinentry`

Useful: `wget gcc python3 tree`

### Useful commands

- `rpm -Uvh [package or url]` - upgrades (install + removes older) package

### Example repo

1. Make repository directory

   ```bash
   mkdir -p ~/example/packages
   ```

2. Create repo and add your packages there

    ```bash
    createrepo ~/example/packages/
    cp /some/folder/pack.rpm ~/example/packages/.
    ```

    and update the metadata list

    ```bash
    createrepo --update ~/example/packages/
    ```

3. Create repo config

    ```ini
    [example-repo]
    name=Example Repo
    baseurl=http://some-ip-or-host:port/packages
    enabled=1
    gpgcheck=1
    gpgkey=http://some-ip-or-host:port/pgp-key.public"
    ```

4. GPG keys

    Either generate or import gpg key.

    ```bash
    gpg --import ~/example/pgp-key.private
    #or
    gpg --gen-key
    gpg --armor --export example > ~/example/pgp-key.public
    gpg --armor --export-secret-keys example > ~/example/pgp-key.private
    ```

    List pgp key signature `gpg --list-signatures`

5. Sign all your packages

    Add your key ID into `.rpmmacros`

    ```bash
    echo "%_signature gpg
    %_gpg_name <your key id here>" > /root/.rpmmacros
    ```

    Sign all packages with

    ```bash
    rpm --addsign ~/example/packages/*.rpm
    ```

    And finally sign repo metadata

    ```bash
    gpg --detach-sign --armor ~/example/packages/repodata/repomd.xml
    ```

6. Test the repo

    On server, open a port and test with simple python web server (default port 8000)

    ```bash
    firewall-cmd --permanent --add-port=some-port/tcp && firewall-cmd --reload
    python3 -m http.server
    ```

    in your client, add the repo, update cache and either search or try to install some package

    ```bash
    yum-config-manager --add-repo http://ip-or-url:port/example.repo
    yum clean all && yum update
    yum -v search --showduplicates your-package
    #or
    yum info -v your-package
    ```

## Source

1. [Build package - Opensource.com](https://opensource.com/article/18/9/how-build-rpm-packages)
2. [BUild package and repo - Opensource.com](https://earthly.dev/blog/creating-and-hosting-your-own-rpm-packages-and-yum-repo/)
3. [RPM package - Red Hat](https://www.redhat.com/sysadmin/create-rpm-package)
4. [Create RPM repo with Nginx - Red hat](https://www.redhat.com/sysadmin/nginx-based-yum-dnf-repo)
5. [Create RPM repo with FTP - Red hat](https://www.redhat.com/sysadmin/ftp-yum-dnf-repository)
6. [Make your own repo - Percona blog](https://www.percona.com/blog/how-to-create-your-own-repositories-for-packages/)
7. [Packaging tutorial - Fedora docs](https://docs.fedoraproject.org/en-US/package-maintainers/Packaging_Tutorial_GNU_Hello/)
8. [Software management - Rockylinux docs](https://docs.rockylinux.org/books/admin_guide/13-softwares/)
9. [How to build package 1](https://rogerwelin.github.io/rpm/rpmbuild/2015/04/04/rpmbuild-tutorial-part-1.html)
10. [How to build package 2](https://rogerwelin.github.io/rpm/rpmbuild/elasticsearch/2015/04/22/rpmbuild-tutorial-elasticsearch-part-2.html)
11. [Add custom repo](https://www.redhat.com/sysadmin/add-yum-repository)
