#!/usr/bin/node
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}
const num = parseInt(procces.argv[2]);
if (!isNaN(num)) {
  const res = factorial(parseInt(process.argv[2]));
  console.log(res);
} else {
  console.log(1);
}
