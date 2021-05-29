import numpy as np 

def function(x):

	a4 = x
	o4 = x
	paths = []
	try:
		if a4 < 5:
			a4 = 8*a4
			a4 = a4/a4
			paths.append(1)
		else:
			a4 = a4/o4
			paths.append(2)
		if o4 <= 9:
			o4 = 9/o4
			a4 = a4-2
			paths.append(3)
		else:
			o4 = 3*o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))