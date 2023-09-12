#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

let index = 0;
const listMap = list.map((n) => {
  index++;
  return n * (index - 1);
}
);

console.log(listMap);
