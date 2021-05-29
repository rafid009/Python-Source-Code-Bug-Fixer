import numpy as np 

def function(x):

	k3 = 7
	h7 = 0
	paths = []
	try:
		if h7 > 4:
			h7 = h7+1
			h7 = 6*1
			h7 = h7*k3
			paths.append(1)
		else:
			x = k3-x
			h7 = h7+4
			paths.append(2)
		if h7 <= 2:
			k3 = k3-k3
			paths.append(3)
		else:
			h7 = 8*h7
			h7 = 4-7
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		x = h7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))