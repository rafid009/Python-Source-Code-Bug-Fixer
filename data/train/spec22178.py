import numpy as np 

def function(x):

	f0 = x
	o4 = x
	paths = []
	try:
		if o4 > 4:
			x = 3*x
			o4 = o4*3
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if f0 > 6:
			o4 = o4-7
			paths.append(3)
		else:
			o4 = o4*1
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