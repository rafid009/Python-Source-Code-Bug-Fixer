import numpy as np 

def function(x):

	o4 = 1
	a7 = 4
	paths = []
	try:
		if o4 > 4:
			x = x*a7
			paths.append(1)
		else:
			a7 = a7-1
			o4 = o4*2
			paths.append(2)
		if x > 9:
			o4 = o4/4
			paths.append(3)
		else:
			o4 = o4*o4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o4 = x**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))