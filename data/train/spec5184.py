import numpy as np 

def function(x):

	h4 = 7
	v1 = x
	x = x
	paths = []
	try:
		if v1 <= 8:
			v1 = v1*2
			paths.append(1)
		else:
			x = v1+h4
			x = x*4
			paths.append(2)
		if x >= 6:
			h4 = h4+4
			paths.append(3)
		else:
			x = 5-x
			x = x/3
			v1 = v1*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))