import numpy as np 

def function(x):

	e3 = 3
	o5 = x
	paths = []
	try:
		if x >= 0:
			o5 = o5+0
			o5 = 6/5
			x = 9/x
			paths.append(1)
		else:
			x = x+4
			paths.append(2)
		if o5 > 0:
			e3 = 9-2
			o5 = 6*o5
			paths.append(3)
		else:
			o5 = o5*4
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		e3 = o5**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))