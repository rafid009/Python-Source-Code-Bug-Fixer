import numpy as np 

def function(x):

	j8 = x
	b8 = 2
	x = x
	paths = []
	try:
		if x < 1:
			x = x/5
			paths.append(1)
		else:
			b8 = 6/b8
			b8 = b8*j8
			j8 = j8-0
			paths.append(2)
		if j8 < 6:
			j8 = b8+j8
			b8 = j8+3
			j8 = j8-x
			paths.append(3)
		else:
			j8 = 3*j8
			x = b8/x
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