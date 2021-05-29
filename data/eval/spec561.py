import numpy as np 

def function(x):

	i4 = 7
	a1 = x
	paths = []
	try:
		if a1 >= 2:
			a1 = a1-5
			a1 = a1/i4
			paths.append(1)
		else:
			x = x+0
			x = a1/6
			x = x-a1
			paths.append(2)
		if x > 6:
			a1 = a1-5
			x = x+x
			paths.append(3)
		else:
			x = x/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))