#!/usr/bin/node

exports.converter = function (base) {
  return function (nmb) {
    return nmb.toString(base);
  };
};
