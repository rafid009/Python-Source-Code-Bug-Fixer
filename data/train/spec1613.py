import numpy as np 

def function(x):

	e7 = 1
	o5 = 3
	paths = []
	try:
		if x >= 0:
			o5 = o5*4
			o5 = x-x
			paths.append(1)
		else:
			x = x*0
			o5 = o5*o5
			o5 = o5/e7
			paths.append(2)
		if x <= 4:
			o5 = 3*o5
			o5 = 7/7
			paths.append(3)
		else:
			e7 = 2/e7
			x = 0-x
			e7 = 0/e7
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