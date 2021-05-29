import numpy as np 

def function(x):

	d5 = 5
	k2 = 4
	paths = []
	try:
		if k2 > 2:
			k2 = k2/4
			k2 = 8*k2
			paths.append(1)
		else:
			d5 = k2-9
			x = x+7
			paths.append(2)
		if d5 >= 2:
			x = x*4
			d5 = 7*5
			x = 7*x
			paths.append(3)
		else:
			x = 8-x
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