import numpy as np 

def function(x):

	i4 = x
	o2 = 7
	paths = []
	try:
		if o2 > 3:
			x = x+o2
			x = 7/x
			paths.append(1)
		else:
			o2 = i4+o2
			paths.append(2)
		if o2 >= 3:
			x = x*9
			x = x/8
			x = x/8
			paths.append(3)
		else:
			o2 = 7+o2
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