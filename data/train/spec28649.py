import numpy as np 

def function(x):

	y5 = 5
	j1 = x
	x = x
	paths = []
	try:
		if j1 < 4:
			y5 = 6+5
			paths.append(1)
		else:
			x = x/1
			j1 = y5/6
			x = 3-1
			paths.append(2)
		if j1 <= 4:
			j1 = 1*j1
			y5 = x-3
			paths.append(3)
		else:
			x = y5/x
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