import numpy as np 

def function(x):

	a7 = 5
	k3 = 9
	paths = []
	try:
		if x < 3:
			k3 = 7/5
			k3 = k3+3
			paths.append(1)
		else:
			a7 = a7/6
			x = 9*7
			k3 = 6/7
			paths.append(2)
		if x < 6:
			a7 = 9*a7
			a7 = a7/7
			paths.append(3)
		else:
			x = 9*x
			a7 = 8*3
			k3 = k3*k3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))