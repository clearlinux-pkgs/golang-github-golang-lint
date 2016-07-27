Name     : golang-github-golang-lint
Version  : c7bacac2b21ca01afa1dee0acf64df3ce047c28f
Release  : 2
URL      : https://github.com/golang/lint/archive/c7bacac2b21ca01afa1dee0acf64df3ce047c28f.tar.gz
Source0  : https://github.com/golang/lint/archive/c7bacac2b21ca01afa1dee0acf64df3ce047c28f.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
BuildRequires : go
BuildRequires : golang-googlecode-go-tools

%description
Golint is a linter for Go source code.
[![Build Status](https://travis-ci.org/golang/lint.svg?branch=master)](https://travis-ci.org/golang/lint)

%prep
%setup -q -n lint-c7bacac2b21ca01afa1dee0acf64df3ce047c28f

%build
export LANG=C

%install
gopath="/usr/lib/golang"
library_path="github.com/golang/lint/golint"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go" -o -iname "*.h" -o -iname "*.c") ; do
     echo ${file}
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
gopath="/usr/lib/golang"
export GOPATH="%{buildroot}${gopath}"
go test -v -x github.com/golang/lint/golint

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/golang/lint/golint/golint/golint.go
/usr/lib/golang/src/github.com/golang/lint/golint/golint/import.go
/usr/lib/golang/src/github.com/golang/lint/golint/lint.go
/usr/lib/golang/src/github.com/golang/lint/golint/lint16.go
/usr/lib/golang/src/github.com/golang/lint/golint/lint_test.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/4.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/5_test.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/blank-import-lib.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/blank-import-lib_test.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/blank-import-main.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/broken.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/common-methods.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/const-block.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/else-multi.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/else.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/error-return.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/errorf.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/errors.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/import-dot.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/inc.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/make.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/names.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-doc1.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-doc2.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-doc3.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-doc4.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-doc5.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/pkg-main.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/range.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/receiver-names.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/sort.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/stutter.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/time.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/unexp-return.go
/usr/lib/golang/src/github.com/golang/lint/golint/testdata/var-decl.go
