import numpy as np 

def function(x):

	x2 = 7
	j8 = 4
	x = x
	paths = []
	try:
		if j8 > 9:
			x2 = j8*x
			x = 4/x
			j8 = j8/6
			paths.append(1)
		else:
			x2 = x2+x
			paths.append(2)
		if x2 < 9:
			x = x-6
			paths.append(3)
		else:
			j8 = 4+7
			j8 = 7-j8
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