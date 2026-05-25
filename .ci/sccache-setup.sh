#!/usr/bin/env sh
install -vdm 755 "/usr/local/bin"
for _prog in gcc g++ c++; do
  ln -vs /usr/bin/sccache "/usr/local/bin/$_prog"
  ln -vs /usr/bin/sccache "/usr/local/bin/$(uname -m)-$_prog"
done
# sccache supports rustc here too
for _prog in cc clang clang++ rustc; do
  ln -vs /usr/bin/sccache "/usr/local/bin/$_prog"
done