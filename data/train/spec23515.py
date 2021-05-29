import numpy as np 

def function(x):

	j1 = 9
	x7 = 7
	paths = []
	try:
		if x < 7:
			x7 = 8*x
			x7 = 6-j1
			x = 2+5
			paths.append(1)
		else:
			j1 = j1/j1
			paths.append(2)
		if j1 < 6:
			x = 3-3
			j1 = j1+0
			paths.append(3)
		else:
			x7 = j1/x7
			x = x7/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))