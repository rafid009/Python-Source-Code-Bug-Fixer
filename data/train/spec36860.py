import numpy as np 

def function(x):

	o9 = 0
	e4 = x
	x = 9
	paths = []
	try:
		if o9 <= 7:
			e4 = 5+3
			paths.append(1)
		else:
			x = 0*x
			o9 = x-0
			x = 3*e4
			paths.append(2)
		if e4 > 9:
			o9 = o9-6
			e4 = 3*5
			paths.append(3)
		else:
			e4 = e4-x
			x = o9/x
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		e4 = e4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))