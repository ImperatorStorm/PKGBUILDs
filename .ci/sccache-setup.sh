#!/usr/bin/env sh
install -vdm 755 "/usr/lib/sccache/bin"
for _prog in gcc g++ c++; do
  ln -vs /usr/bin/sccache "/usr/lib/sccache/bin/$_prog"
  ln -vs /usr/bin/sccache "/usr/lib/sccache/bin/$(uname -m)-$_prog"
done
# sccache supports rustc here too
for _prog in cc clang clang++ rustc; do
  ln -vs /usr/bin/sccache "/usr/lib/sccache/bin/$_prog"
done