import numpy as np 

def function(x):

	h9 = 6
	u9 = x
	paths = []
	try:
		if u9 <= 2:
			u9 = 9+u9
			h9 = h9/3
			u9 = 7*4
			paths.append(1)
		else:
			u9 = 8/8
			paths.append(2)
		if u9 <= 5:
			h9 = h9+x
			u9 = 9+1
			paths.append(3)
		else:
			u9 = x/u9
			u9 = 6/u9
			h9 = h9-u9
			paths.append(4)
		paths.append(5)
		assert h9 >= 0
		h9 = h9**0.5
		return h9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))