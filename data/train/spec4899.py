import numpy as np 

def function(x):

	h8 = 0
	v7 = x
	paths = []
	try:
		if h8 <= 4:
			x = 9+h8
			paths.append(1)
		else:
			x = x/h8
			v7 = v7*v7
			x = v7/1
			paths.append(2)
		if h8 >= 0:
			x = x*9
			x = x*v7
			v7 = 4*v7
			paths.append(3)
		else:
			h8 = h8*2
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