import numpy as np 

def function(x):

	a8 = x
	h6 = x
	paths = []
	try:
		if a8 <= 9:
			a8 = 6+x
			h6 = h6*2
			paths.append(1)
		else:
			a8 = 4*a8
			a8 = h6*9
			a8 = a8/a8
			paths.append(2)
		if a8 > 0:
			a8 = 8-a8
			x = x-x
			paths.append(3)
		else:
			h6 = h6/a8
			a8 = x+8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))