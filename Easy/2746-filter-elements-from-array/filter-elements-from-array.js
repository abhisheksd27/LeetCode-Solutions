/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    // Initialize an empty array to store the filtered elements
    let filteredArr = [];
    
    // Iterate over the elements of the input array
    for (let i = 0; i < arr.length; i++) {
        // Apply the filtering function to each element
        if (fn(arr[i], i)) {
            // If the function returns a truthy value, add the element to the filtered array
            filteredArr.push(arr[i]);
        }
    }
    
    // Return the filtered array
    return filteredArr;
};
