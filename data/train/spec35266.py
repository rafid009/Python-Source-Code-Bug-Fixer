import numpy as np 

def function(x):

	x9 = x
	j8 = 5
	paths = []
	try:
		if x9 <= 8:
			j8 = j8*4
			x9 = x9+j8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if j8 > 3:
			j8 = 9*j8
			x = 2+x9
			paths.append(3)
		else:
			x9 = 8-x9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j8 = x**0.5
		return j8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))