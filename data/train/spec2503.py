import numpy as np 

def function(x):

	x8 = 4
	i7 = 7
	paths = []
	try:
		if i7 < 5:
			x8 = i7*x
			paths.append(1)
		else:
			x8 = x8*x8
			x8 = x8*x
			x = x/i7
			paths.append(2)
		if x8 < 8:
			x8 = x8*9
			x8 = 1/x8
			x = x+i7
			paths.append(3)
		else:
			x = 3+4
			x8 = 6-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x8 = x**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))