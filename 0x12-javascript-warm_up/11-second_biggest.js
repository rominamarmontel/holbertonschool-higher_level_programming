#!/usr/bin/node
const argv = process.argv;
const arr = [];
if (argv.length < 4) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    arr[i - 2] = parseInt(argv[i]);
  }
  const max = Math.max.apply(null, arr); // get the max of the array
  arr.splice(arr.indexOf(max), 1); // remove max from the array
  const secondMax = Math.max.apply(null, arr)
  console.log(secondMax); // get the 2nd max
}
