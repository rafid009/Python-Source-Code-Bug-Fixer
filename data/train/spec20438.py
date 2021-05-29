import numpy as np 

def function(x):

	j3 = 5
	h5 = 1
	paths = []
	try:
		if j3 >= 5:
			h5 = 6*h5
			paths.append(1)
		else:
			h5 = 3-x
			j3 = h5-2
			h5 = 6-8
			paths.append(2)
		if x <= 2:
			h5 = x/1
			x = 7*j3
			paths.append(3)
		else:
			h5 = 9*h5
			j3 = 5-7
			x = x+2
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		h5 = j3**0.5
		return h5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))