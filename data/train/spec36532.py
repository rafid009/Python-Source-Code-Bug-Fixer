import numpy as np 

def function(x):

	j8 = 2
	a8 = 1
	paths = []
	try:
		if j8 >= 8:
			x = x*a8
			paths.append(1)
		else:
			x = x*1
			a8 = a8/j8
			a8 = x-9
			paths.append(2)
		if a8 <= 6:
			x = x+x
			j8 = 8-9
			paths.append(3)
		else:
			j8 = j8/5
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))