import numpy as np 

def function(x):

	x1 = x
	d9 = x
	paths = []
	try:
		if d9 >= 9:
			x = x+0
			x = 2*x
			paths.append(1)
		else:
			x1 = x-d9
			paths.append(2)
		if d9 <= 2:
			x1 = x1+1
			paths.append(3)
		else:
			x1 = x1/5
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