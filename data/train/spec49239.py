import numpy as np 

def function(x):

	i5 = x
	o4 = 1
	paths = []
	try:
		if o4 > 8:
			o4 = 0/o4
			x = x/x
			x = x+3
			paths.append(1)
		else:
			o4 = 9/6
			o4 = o4-3
			o4 = o4*8
			paths.append(2)
		if o4 > 6:
			x = 1/x
			x = x*i5
			x = x*0
			paths.append(3)
		else:
			x = 0-x
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