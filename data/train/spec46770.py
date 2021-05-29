import numpy as np 

def function(x):

	h6 = 9
	i4 = 6
	paths = []
	try:
		if i4 >= 4:
			i4 = 6*0
			h6 = h6/6
			i4 = h6/1
			paths.append(1)
		else:
			i4 = i4+3
			paths.append(2)
		if x > 0:
			x = x+x
			i4 = 0/i4
			paths.append(3)
		else:
			i4 = i4*h6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h6 = x**0.5
		return h6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))