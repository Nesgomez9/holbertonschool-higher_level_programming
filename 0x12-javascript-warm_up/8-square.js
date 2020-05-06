#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);
if (!isNaN(num)) {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
} else {
  console.log('Missing size');
}
