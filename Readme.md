In this project the function find_matching_pairs is defined. The input of this function is an integer h, and the output is the pairs of NBA players whose heights in inches add up to h.

The data is retrieved from the website https://mach-eight.uc.r.appspot.com/ in json format.

For purpose of efficiency an auxiliary find_index function is defined. This function uses binary search to find the index of an item in a sorted list.

Finally, the find_matching_pairs function is defined and the testing file is also provided. Two test functions are provided, one for the mininum number which returns at least a matching pair, and other for different values which returns "No matching pairs found!"  

The time complexity of this function is less than O(n^2) since binary search is O(log_2(n)) and sort a list and look for elements in a list are both O(nlog_2(n)). Hence, this algorithm is at most O(nlog_2(n)) which is faster than O(n^2).

Thanks for reading.