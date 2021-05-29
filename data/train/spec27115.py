import numpy as np 

def function(x):

	r9 = 8
	j8 = x
	paths = []
	try:
		if r9 > 6:
			j8 = 6+j8
			r9 = r9*7
			paths.append(1)
		else:
			j8 = 7*j8
			j8 = r9+r9
			paths.append(2)
		if x > 0:
			r9 = 7*r9
			r9 = 7/2
			j8 = 9*5
			paths.append(3)
		else:
			j8 = j8+6
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