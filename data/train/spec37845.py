import numpy as np 

def function(x):

	e0 = x
	o7 = x
	paths = []
	try:
		if o7 <= 6:
			o7 = 0*6
			o7 = o7/x
			paths.append(1)
		else:
			e0 = e0*x
			paths.append(2)
		if x >= 5:
			x = x*4
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		o7 = e0**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))