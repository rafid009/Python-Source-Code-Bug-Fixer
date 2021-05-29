import numpy as np 

def function(x):

	a3 = x
	p6 = x
	paths = []
	try:
		if x <= 6:
			x = x/5
			a3 = 3-a3
			paths.append(1)
		else:
			a3 = 1*a3
			p6 = 0+p6
			a3 = 3*p6
			paths.append(2)
		if a3 < 6:
			a3 = 9/8
			a3 = 8*a3
			paths.append(3)
		else:
			a3 = 2-a3
			x = x/3
			x = 8+x
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