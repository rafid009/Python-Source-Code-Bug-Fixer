import numpy as np 

def function(x):

	h6 = 6
	v6 = x
	paths = []
	try:
		if v6 > 4:
			h6 = 5/4
			x = v6-x
			v6 = v6+h6
			paths.append(1)
		else:
			v6 = v6-2
			h6 = 5*h6
			h6 = x+v6
			paths.append(2)
		if x < 9:
			h6 = h6+1
			paths.append(3)
		else:
			v6 = 5+v6
			h6 = h6-x
			h6 = h6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))