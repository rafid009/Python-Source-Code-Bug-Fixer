import numpy as np 

def function(x):

	a1 = 7
	k4 = x
	paths = []
	try:
		if k4 > 9:
			x = 1*0
			a1 = 4*x
			a1 = 2/8
			paths.append(1)
		else:
			k4 = 5+3
			a1 = 0-x
			paths.append(2)
		if a1 >= 8:
			k4 = 6+5
			paths.append(3)
		else:
			a1 = 7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))