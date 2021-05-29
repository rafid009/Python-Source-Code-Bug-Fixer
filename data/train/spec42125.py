import numpy as np 

def function(x):

	n9 = 4
	e9 = x
	paths = []
	try:
		if n9 < 7:
			x = x*2
			e9 = e9-4
			paths.append(1)
		else:
			e9 = e9/n9
			paths.append(2)
		if e9 < 2:
			e9 = 0+e9
			e9 = 5+e9
			n9 = n9*e9
			paths.append(3)
		else:
			n9 = n9+1
			x = x-n9
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