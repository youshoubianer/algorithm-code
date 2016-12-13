'use strict';

let n = Number(process.argv[2])
let k = Number(process.argv[3])

console.time('start');

let randomNumbers = generateRandomNum(-1000, 1000, n);
console.log(randomNumbers);
let res = selectK(randomNumbers, k);
console.log('res>>>',res);

console.timeEnd('start')


function generateRandomNum(min,max,n){
  let randomArray = [];
  for(let i = 0; i < n; i++){
    //从min到max的随机数
    let randomNum = Math.floor(Math.random() * (max - min + 1) + min);
    randomArray.push(randomNum)
  }
  return randomArray;
}

function findMax(base){
  let max = -0x3f3f3f,
      idx = -1;
  for(let i = 0,len = base.length; i < len; i++){
    if(base[i] > max){
      max = base[i];
      idx = i;
    }
  }
  
  return {
    max: max,
    idx: idx
  }
}

function selectK(numbers,k) {
  let base = numbers.slice(0,k);
  let remain = numbers.slice(k);
  console.log('base>>>',base,'\nremain>>>',remain);
  let maxObj = findMax(base);
  
  for(let i = 0,len = remain.length; i < len; i++){
    if(remain[i] < maxObj.max){
      base[maxObj.idx] = remain[i];
      maxObj = findMax(base);
    }
  }
  
  return base;
}