#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let v = 0;
  while ((len - v) > 0) {
    const aux = list[len];
    list[len] = list[v];
    listv] = aux;
    v++;
    len--;
  }
  return list;
};
