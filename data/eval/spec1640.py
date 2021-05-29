import numpy as np 

def function(x):

	d8 = x
	o1 = 3
	paths = []
	try:
		if d8 >= 6:
			o1 = o1*5
			x = x*6
			x = x/5
			paths.append(1)
		else:
			o1 = o1*5
			paths.append(2)
		if x >= 1:
			o1 = 5-o1
			paths.append(3)
		else:
			o1 = 9-d8
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