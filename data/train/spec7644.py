import numpy as np 

def function(x):

	o2 = 2
	h1 = x
	paths = []
	try:
		if x < 2:
			o2 = h1/9
			paths.append(1)
		else:
			x = 5*7
			paths.append(2)
		if o2 < 4:
			h1 = h1*1
			o2 = 3+o2
			x = x-2
			paths.append(3)
		else:
			x = x-o2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o2 = x**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))