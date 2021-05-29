import numpy as np 

def function(x):

	o2 = 5
	a3 = x
	paths = []
	try:
		if x < 2:
			o2 = x*9
			o2 = 0*9
			paths.append(1)
		else:
			a3 = 8/a3
			x = 7*x
			x = x*a3
			paths.append(2)
		if o2 < 8:
			x = a3-x
			paths.append(3)
		else:
			x = x+o2
			a3 = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))