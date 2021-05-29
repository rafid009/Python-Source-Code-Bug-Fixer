import numpy as np 

def function(x):

	m8 = 1
	o2 = 3
	paths = []
	try:
		if o2 > 2:
			x = x+3
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if o2 <= 3:
			o2 = o2/6
			paths.append(3)
		else:
			o2 = 9*4
			x = x-5
			x = x*6
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