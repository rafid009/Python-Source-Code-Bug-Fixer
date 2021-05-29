import numpy as np 

def function(x):

	j3 = x
	h9 = 2
	paths = []
	try:
		if h9 < 6:
			j3 = j3*j3
			paths.append(1)
		else:
			j3 = 3+j3
			x = x+x
			paths.append(2)
		if j3 <= 9:
			x = x-x
			x = h9*x
			paths.append(3)
		else:
			h9 = h9*3
			h9 = h9+x
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