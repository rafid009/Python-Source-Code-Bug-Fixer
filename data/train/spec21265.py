import numpy as np 

def function(x):

	o7 = x
	paths = []
	try:
		if x > 8:
			x = x/o7
			o7 = 5+o7
			o7 = o7+1
			paths.append(1)
		else:
			o7 = o7/7
			o7 = 0-o7
			o7 = 2*o7
			paths.append(2)
		if o7 > 3:
			o7 = o7*x
			o7 = o7+o7
			paths.append(3)
		else:
			o7 = o7*x
			paths.append(4)
		paths.append(5)
		assert o7 >= 0
		x = o7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))