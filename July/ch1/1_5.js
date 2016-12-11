/*
* 最长回文字串
*/
'use strict';

let s = process.argv[2];
let n = s.length;
let res1 = longestPalindrome(s,n);
console.log('longestPalindrome : ',res1);

let res2 = manacher(s,n);
console.log('manacher : ',res2);

//manacher init
function manacher(s,n){
  s = `#${s.split('').join('#')}#`;
  // console.log('init s>>>',s);
  n = s.length;
  
  let resP = longestPalindromeManacher(s,n);
  // console.log('resP>>>',resP);
  return Math.max.apply(this,resP)-1
}

//mamacher
function longestPalindromeManacher(s,n){
  let i, id=1, mx=0, p=[];
  p[0] = 1;
  for(i=1; i < n; i++){
    if(mx > i){
      p[i] = Math.min(p[2*id-i],mx-i);
    }
    else{
      p[i] = 1;
    }
    while (s[i+p[i]] == s[i-p[i]]) {
      p[i]++
    }
    
    if(p[i]+i > mx){
      mx = p[i]+i;
      id = i;
    }
  }
  return p;
}


//中心扩展法
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


