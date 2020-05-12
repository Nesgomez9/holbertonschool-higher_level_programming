#!/usr/bin/node

const list = require('./100-data').list;

let newList = [];
let i = 0;

newList = list.map(x => x * i++);

console.log(list);
console.log(newList);
