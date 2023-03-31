# check disabled to avoid circular dependencies
%bcond_with check

%global crate pulldown-cmark

Name:           rust-%{crate}
Version:        0.8.0
Release:        2
Summary:        Pull parser for CommonMark

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/pulldown-cmark
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pull parser for CommonMark.}

%description %{_description}

%if ! %{__cargo_skip_build}
%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc README.md CONTRIBUTING.md
%{_bindir}/pulldown-cmark
%endif

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md CONTRIBUTING.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+gen-tests-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gen-tests-devel %{_description}

This package contains library source intended for building other packages
which use "gen-tests" feature of "%{crate}" crate.

%files       -n %{name}+gen-tests-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+getopts-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getopts-devel %{_description}

This package contains library source intended for building other packages
which use "getopts" feature of "%{crate}" crate.

%files       -n %{name}+getopts-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+simd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+simd-devel %{_description}

This package contains library source intended for building other packages
which use "simd" feature of "%{crate}" crate.

%files       -n %{name}+simd-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
