import numpy as np 

def function(x):

	v3 = x
	h9 = 0
	x = 5
	paths = []
	try:
		if v3 >= 0:
			h9 = h9*5
			v3 = 5/2
			x = x*4
			paths.append(1)
		else:
			x = h9-x
			x = v3*7
			x = 7+v3
			paths.append(2)
		if x >= 2:
			x = x/3
			v3 = v3*x
			paths.append(3)
		else:
			v3 = x*9
			h9 = 7-3
			x = h9*x
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))