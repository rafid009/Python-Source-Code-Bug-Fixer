import numpy as np 

def function(x):

	k6 = 3
	h7 = 2
	paths = []
	try:
		if h7 < 0:
			h7 = 1+7
			x = x+h7
			paths.append(1)
		else:
			h7 = h7+k6
			x = x/6
			k6 = k6/8
			paths.append(2)
		if k6 >= 5:
			x = h7*6
			x = x-x
			x = 5-6
			paths.append(3)
		else:
			h7 = x/3
			k6 = 4*k6
			k6 = 1-4
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		h7 = k6**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))