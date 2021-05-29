import numpy as np 

def function(x):

	y5 = x
	i9 = 2
	paths = []
	try:
		if x > 1:
			x = 1/x
			x = i9+x
			y5 = x+y5
			paths.append(1)
		else:
			y5 = y5+x
			y5 = 2*2
			y5 = 7*y5
			paths.append(2)
		if x >= 1:
			y5 = 9+1
			paths.append(3)
		else:
			y5 = y5-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))