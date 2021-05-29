import numpy as np 

def function(x):

	h1 = x
	o2 = 0
	paths = []
	try:
		if x >= 1:
			o2 = o2/3
			paths.append(1)
		else:
			o2 = o2/3
			paths.append(2)
		if x > 8:
			h1 = o2/9
			o2 = o2+o2
			paths.append(3)
		else:
			x = x+o2
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