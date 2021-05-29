import numpy as np 

def function(x):

	j8 = x
	x2 = 0
	paths = []
	try:
		if x < 4:
			j8 = 1/j8
			j8 = 9/j8
			paths.append(1)
		else:
			x2 = x+x2
			x = 0+x
			j8 = j8*j8
			paths.append(2)
		if j8 < 4:
			j8 = 5-3
			paths.append(3)
		else:
			x2 = x2/2
			x2 = x2-x2
			x2 = x2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x2 = x**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))