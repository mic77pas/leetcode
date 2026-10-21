/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */

// [1,3], [2,6], [2,4]

var merge = function(intervals) {
  intervals.sort((a, b) => a[0] - b[0]);     

  const merged = [];
  for (const [start, end] of intervals) {
    const last = merged[merged.length - 1]; 

    if (last && start <= last[1]) {
      last[1] = Math.max(last[1], end);
    } else {
      merged.push([start, end]); 
    }
    
  }
  return merged;
};