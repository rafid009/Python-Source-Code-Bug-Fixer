import numpy as np 

def function(x):

	a7 = x
	a3 = x
	paths = []
	try:
		if a7 > 8:
			a3 = a3+8
			paths.append(1)
		else:
			a3 = 0/6
			x = x*2
			paths.append(2)
		if x <= 0:
			a7 = x-a7
			paths.append(3)
		else:
			a7 = a7+x
			a3 = a3/6
			a7 = 0*a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a3 = x**0.5
		return a3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))