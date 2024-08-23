/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
function map(arr, fn) {
    const result = []; // Create an empty array to store the results

    for (let i = 0; i < arr.length; i++) {
        result.push(fn(arr[i], i)); // Apply the function fn to each element and its index
    }

    return result; // Return the transformed array
}