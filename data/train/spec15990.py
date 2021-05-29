import numpy as np 

def function(x):

	y4 = x
	a0 = 8
	paths = []
	try:
		if x <= 6:
			x = 9+x
			y4 = y4/3
			paths.append(1)
		else:
			y4 = 4+y4
			paths.append(2)
		if y4 < 8:
			a0 = a0/a0
			y4 = y4/3
			paths.append(3)
		else:
			x = x+5
			x = x*a0
			x = x*a0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))