/*
* leetcode
* 283. Move Zeroes  AC
* zhao xiaodong 2016-12-19
*/

'use strict';

let moveZeros = function(nums){
  let i = 0,j = 1, len = nums.length;
  if(nums.length < 1){
    return nums[0] === 0 ? [nums[1],0] : nums;
  }
  for(i,j; j < len; ){
    if(nums[i] === 0 && nums[j] !== 0){
      let tmp = nums[j];
      nums[j] = nums[i];
      nums[i] = tmp;
      i++; j++;
      continue;
    }
    while(nums[i] !== 0 && i < len){ i++ ; }
    j = i + 1;
    while (nums[j] === 0 && j < len ) { j++ ; }
  }
  console.log(nums);
}

moveZeros(process.argv.slice(2).map(item => {return Number(item)}));
