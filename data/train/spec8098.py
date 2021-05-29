import numpy as np 

def function(x):

	e0 = 5
	o4 = x
	paths = []
	try:
		if x <= 2:
			x = x+6
			paths.append(1)
		else:
			o4 = o4/9
			o4 = 4-4
			o4 = x+o4
			paths.append(2)
		if x >= 9:
			x = o4-x
			e0 = x-3
			paths.append(3)
		else:
			o4 = o4+1
			o4 = o4-x
			e0 = e0+0
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		e0 = o4**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))