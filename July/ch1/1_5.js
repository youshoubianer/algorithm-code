/*
* 最长回文字串
*/
'use strict';

let s = process.argv[2];
let n = s.length;
let res = longestPalindrome(s,n);
console.log('longestPalindrome : ',res);

function longestPalindrome(s,n){
  let i,j,max=0,c;
  
  if(n<1){
    return 0
  }
  //遍历回文中心
  for(i = 0; i < n; i++){
    //回文长度为奇数
    for(j = 0; (i - j) >= 0 && (i + j) < n; j++){
      if(s[i+j] !== s[i-j]){
        break;
      }
      c = j * 2 + 1;
    }
    max = Math.max(c, max);
    
    //回文长度为偶数
    for(j = 0; (i - j) >= 0 && (i+j+1) < n; j++){
      if(s[i-j] !== s[i+j+1]){
        break;
      }
      c = j * 2 + 2;
    }
    max = Math.max(c,max);
  }
  return max;
}


