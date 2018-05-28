""" Given a sorted array of integers, return the index of the given key. Return -1 if not found.
https://www.geeksforgeeks.org/binary-search/
"""

def recursive_binary_search(arr, low, high, key):
	if low>high:
		return -1

	else:
		mid = low + (high - low)/2

		if arr[mid] == key:
			return mid
		elif arr[mid]>key:
			return recursive_binary_search(arr, low, mid - 1, key)
		else:
			return recursive_binary_search(arr, mid + 1, high, key)


def iterative_binary_search(arr, low, high, key):
	while low<=high:
		mid = low + (high - low)/2

		if arr[mid] == key:
			return mid
		elif arr[mid]<key:
			low = mid + 1
		else:
			high = mid - 1

	return -1


if __name__ == '__main__':
	arr = [1, 2, 3, 4, 5, 6, 7, 9, 10] # 8 is missing
	low, high = 0, len(arr) - 1
	key = 10

	print recursive_binary_search(arr, low, high, key)

	print iterative_binary_search(arr, low, high, key)

