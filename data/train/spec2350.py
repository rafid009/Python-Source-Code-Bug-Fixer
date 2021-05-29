import numpy as np 

def function(x):

	h6 = 2
	v2 = x
	paths = []
	try:
		if h6 < 0:
			v2 = 7*v2
			v2 = v2+x
			paths.append(1)
		else:
			h6 = x+h6
			v2 = v2+v2
			x = x-2
			paths.append(2)
		if v2 < 7:
			h6 = 5*v2
			paths.append(3)
		else:
			h6 = 5-h6
			v2 = v2/x
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		x = h6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))