import numpy as np 

def function(x):

	h9 = 3
	a4 = x
	paths = []
	try:
		if a4 > 5:
			x = a4*1
			x = 5*1
			h9 = x+h9
			paths.append(1)
		else:
			x = x/6
			paths.append(2)
		if a4 <= 6:
			x = a4*2
			paths.append(3)
		else:
			a4 = h9/a4
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