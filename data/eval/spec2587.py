import numpy as np 

def function(x):

	b2 = 8
	o2 = 2
	paths = []
	try:
		if b2 > 5:
			o2 = o2-6
			paths.append(1)
		else:
			x = 3/9
			x = o2-3
			paths.append(2)
		if o2 > 6:
			o2 = o2-8
			paths.append(3)
		else:
			x = 2-b2
			b2 = 5-4
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