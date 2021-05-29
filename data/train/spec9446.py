import numpy as np 

def function(x):

	a3 = 0
	n5 = 8
	x = x
	paths = []
	try:
		if n5 >= 4:
			a3 = a3+x
			a3 = 2/n5
			a3 = 8*a3
			paths.append(1)
		else:
			x = 6*x
			a3 = a3+x
			a3 = a3*3
			paths.append(2)
		if a3 >= 7:
			n5 = n5*x
			n5 = n5-7
			a3 = x+a3
			paths.append(3)
		else:
			x = 9-x
			x = x+8
			x = 0-8
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