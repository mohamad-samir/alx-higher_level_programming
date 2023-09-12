#!/usr/bin/node

exports.esrever = function (list) {
  const reversedList = [];
  for (let e = list.length - 1; e >= 0; e--) {
    reversedList.push(list[e]);
  }

  return reversedList;
};
