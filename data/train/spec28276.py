import numpy as np 

def function(x):

	y5 = x
	j1 = x
	paths = []
	try:
		if j1 <= 6:
			x = 1/x
			j1 = x-9
			x = x*4
			paths.append(1)
		else:
			j1 = 5/j1
			x = x/3
			paths.append(2)
		if j1 < 9:
			x = x-7
			paths.append(3)
		else:
			j1 = j1*2
			j1 = 9-j1
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