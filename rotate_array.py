""" Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.
https://www.geeksforgeeks.org/array-rotation/
"""

# Method 1: Using temp array.
def temp_array_rotation(arr, r):
	if r<=0:
		return arr

	else:
		temp_arr = arr[:r]
		arr = arr[r: ]
		arr += temp_arr

	return arr

# Method 2: Using single rotation.
def one_by_one_array_rotation(arr, r):
	if r<=0:
		return arr
	else:
		for i in range(r):
			left_rotation_by_one(arr)

	return arr

def left_rotation_by_one(arr):
	temp = arr[0]
	for i in range(len(arr)-1):
		arr[i] = arr[i+1]

	arr[i+1] = temp


if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5]
	r = 2
	print temp_array_rotation(arr, r)

	print one_by_one_array_rotation(arr, r)