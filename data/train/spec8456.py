import numpy as np 

def function(x):

	e6 = 8
	o2 = 0
	paths = []
	try:
		if o2 > 0:
			o2 = 5+e6
			e6 = o2-e6
			paths.append(1)
		else:
			o2 = o2*o2
			paths.append(2)
		if x < 5:
			x = x-3
			o2 = o2-4
			e6 = e6-e6
			paths.append(3)
		else:
			e6 = e6-0
			o2 = e6-x
			e6 = x+e6
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