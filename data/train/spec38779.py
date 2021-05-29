import numpy as np 

def function(x):

	a3 = x
	j8 = 9
	x = 9
	paths = []
	try:
		if j8 < 9:
			a3 = 6-a3
			x = x+j8
			x = 4*1
			paths.append(1)
		else:
			x = a3*x
			j8 = j8*j8
			a3 = a3*7
			paths.append(2)
		if x >= 1:
			a3 = 0-a3
			x = a3-x
			a3 = 5-a3
			paths.append(3)
		else:
			a3 = x-2
			j8 = j8/j8
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