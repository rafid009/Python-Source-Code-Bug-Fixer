import numpy as np 

def function(x):

	r8 = x
	o7 = x
	paths = []
	try:
		if o7 > 2:
			o7 = 1*o7
			r8 = r8*9
			paths.append(1)
		else:
			o7 = 7/4
			r8 = 9+r8
			paths.append(2)
		if o7 < 1:
			x = x*7
			x = x*8
			x = 9*x
			paths.append(3)
		else:
			r8 = r8-9
			r8 = 3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o7 = x**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))