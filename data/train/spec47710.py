import numpy as np 

def function(x):

	h8 = x
	a4 = 0
	paths = []
	try:
		if h8 < 0:
			x = x/1
			h8 = h8+h8
			a4 = 7+5
			paths.append(1)
		else:
			h8 = h8*h8
			h8 = 5*3
			x = x-7
			paths.append(2)
		if a4 >= 4:
			a4 = 6*a4
			x = x/4
			x = 2*2
			paths.append(3)
		else:
			x = x*4
			h8 = h8*9
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