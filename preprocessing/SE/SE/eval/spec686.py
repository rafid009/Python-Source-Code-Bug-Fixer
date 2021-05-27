import numpy as np 

def function(x):

	j1 = 9
	h7 = x
	paths = []
	try:
		if h7 < 5:
			x = x-4
			paths.append(1)
		else:
			j1 = h7*j1
			j1 = j1*5
			x = 1+7
			paths.append(2)
		if h7 > 0:
			h7 = 9+h7
			j1 = 9-j1
			j1 = 3-j1
			paths.append(3)
		else:
			x = x*x
			x = x/9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))