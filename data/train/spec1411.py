import numpy as np 

def function(x):

	u0 = 8
	o6 = 3
	paths = []
	try:
		if x > 5:
			u0 = x-u0
			x = 1-0
			paths.append(1)
		else:
			o6 = o6+u0
			x = x-8
			u0 = u0+2
			paths.append(2)
		if o6 >= 0:
			o6 = 2*u0
			u0 = 4+8
			o6 = o6*1
			paths.append(3)
		else:
			u0 = 4*x
			o6 = o6/o6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		u0 = o6**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))