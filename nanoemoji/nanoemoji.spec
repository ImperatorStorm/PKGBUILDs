Name:           nanoemoji
Version:        0.15.3
Release:        %autorelease
%global commit0 7f434e5818ad84e755e44fd680b6aea4bed98b20
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Summary:        Compiler for color fonts
License:        Apache-2.0
URL:            https://github.com/googlefonts/nanoemoji
Source:         %{pypi_source nanoemoji}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  fonttools
BuildRequires:  python3-fonttools
BuildRequires:  nototools
BuildRequires:  python3-nototools
BuildRequires:  python3-importlib-resources
BuildRequires:  python3-lxml
BuildRequires:  python3-absl-py
BuildRequires:  python3-ninja
BuildRequires:  ninja-build
BuildRequires:  python3-picosvg
BuildRequires:  python3-absl-py
BuildRequires:  python3-pillow-devel
BuildRequires:  python3-pillow
BuildRequires:  python3-regex
BuildRequires:  python3-toml
BuildRequires:  python3-ufo2ft+cffsubr
BuildRequires:  python3-ufoLib2
BuildRequires:  python3-zopfli
BuildRequires:  pngquant
BuildRequires:  resvg

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'nanoemoji' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-nanoemoji
Summary:        %{summary}

%description -n python3-nanoemoji %_description

Source0: https://github.com/googlefonts/noto-emoji/archive/%{commit0}.tar.gz#/noto-emoji-%{shortcommit0}.tar.gz

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-nanoemoji dev,lint,test

%prep
%autosetup -p1 -n nanoemoji-%{version}
sed -i '/resvg/d' setup.py


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x dev,lint,test


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-nanoemoji -f %{pyproject_files}


%changelog
%autochangelog