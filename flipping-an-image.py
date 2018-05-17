class Solution(object):
    def flipAndInvertImage(self, A):
    	otpt = list()
    	flag = 1

    	for row in A:
    		otpt.append(sorted(row, reverse=True))

    	for row in 
    	


inpt = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
otpt = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
print Solution().flipAndInvertImage(inpt)


O(n^2)