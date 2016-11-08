'use strict';

let n = Number(process.argv[2])
let s = process.argv.slice(3).join(' ')

function func0(s,n){
  console.time('func0');
  let res0 = s.slice(n,s.length) + s.slice(0,n)
  console.timeEnd('func0');

  return res0
}

//let res0 = func0(s,n)
//console.log('res0>>>',res0);

//i am a student. ==> student. a am i
function func1(s){
  return s.split(' ').reverse().join(' ');
}
let res1 = func1(s);
console.log('res1>>>',res1);