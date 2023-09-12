#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let elemCount = 0;
  list.forEach(element => {
    if (element === searchElement) {
      elemCount++;
    }
  });

  return elemCount;
};
