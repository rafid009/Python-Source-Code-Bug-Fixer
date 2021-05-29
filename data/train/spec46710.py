import numpy as np 

def function(x):

	e7 = 7
	o9 = 9
	paths = []
	try:
		if o9 >= 0:
			o9 = x-o9
			x = x/x
			e7 = 6+e7
			paths.append(1)
		else:
			o9 = o9+2
			o9 = o9/x
			o9 = 0/o9
			paths.append(2)
		if e7 > 1:
			x = 5-x
			x = o9*6
			x = x*e7
			paths.append(3)
		else:
			o9 = o9-2
			o9 = 3/o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		e7 = o9**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))