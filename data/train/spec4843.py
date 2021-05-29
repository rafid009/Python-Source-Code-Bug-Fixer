import numpy as np 

def function(x):

	h9 = 2
	v2 = x
	paths = []
	try:
		if h9 >= 3:
			v2 = v2-2
			h9 = x*6
			v2 = 9+v2
			paths.append(1)
		else:
			v2 = v2*3
			h9 = 1*h9
			paths.append(2)
		if x <= 4:
			h9 = 7+h9
			paths.append(3)
		else:
			v2 = v2+v2
			h9 = 2*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v2 = x**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))