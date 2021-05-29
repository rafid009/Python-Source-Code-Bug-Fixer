import numpy as np 

def function(x):

	h1 = x
	j7 = x
	paths = []
	try:
		if j7 < 6:
			j7 = 1*6
			j7 = h1-x
			j7 = 0*4
			paths.append(1)
		else:
			h1 = 6+j7
			paths.append(2)
		if j7 < 7:
			h1 = 2*0
			h1 = h1/5
			h1 = 0+2
			paths.append(3)
		else:
			h1 = h1-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))