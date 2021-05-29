import numpy as np 

def function(x):

	u0 = 6
	o6 = x
	paths = []
	try:
		if x >= 8:
			x = x+5
			x = 7-x
			x = x*8
			paths.append(1)
		else:
			x = u0/9
			x = 2/3
			paths.append(2)
		if x < 3:
			o6 = 2*u0
			paths.append(3)
		else:
			o6 = 0*1
			o6 = o6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o6 = x**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))