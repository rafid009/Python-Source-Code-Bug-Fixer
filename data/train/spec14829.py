import numpy as np 

def function(x):

	a8 = 9
	x4 = x
	x = x
	paths = []
	try:
		if x < 1:
			a8 = x4-a8
			x = x-6
			paths.append(1)
		else:
			x4 = x4/9
			x4 = 2*a8
			paths.append(2)
		if x <= 8:
			x = x-0
			paths.append(3)
		else:
			x = x+x4
			x = x-9
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))