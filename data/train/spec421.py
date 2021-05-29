import numpy as np 

def function(x):

	i7 = 9
	x6 = x
	paths = []
	try:
		if x6 < 8:
			i7 = 1/i7
			x = x/x6
			x = 1/x
			paths.append(1)
		else:
			x6 = x6*x6
			x6 = 7-x6
			paths.append(2)
		if x >= 9:
			x = x*i7
			x = 0-i7
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))