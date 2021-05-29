import numpy as np 

def function(x):

	h2 = 0
	o2 = 0
	paths = []
	try:
		if h2 >= 5:
			x = 7+x
			paths.append(1)
		else:
			h2 = h2+0
			x = 0-x
			paths.append(2)
		if x <= 5:
			x = 1*h2
			x = 2-6
			paths.append(3)
		else:
			o2 = 5/x
			o2 = o2*6
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