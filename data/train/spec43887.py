import numpy as np 

def function(x):

	x1 = 9
	i7 = x
	paths = []
	try:
		if x1 < 0:
			i7 = 6*7
			paths.append(1)
		else:
			x1 = x1+8
			x = x-8
			x1 = 4*x1
			paths.append(2)
		if x1 <= 5:
			i7 = i7+i7
			paths.append(3)
		else:
			i7 = i7*x
			x1 = 9/x1
			i7 = i7+8
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