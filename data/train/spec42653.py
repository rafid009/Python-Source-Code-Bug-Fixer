import numpy as np 

def function(x):

	o4 = 2
	y6 = x
	paths = []
	try:
		if x > 3:
			x = x+y6
			paths.append(1)
		else:
			y6 = 0*y6
			o4 = o4+2
			x = x/7
			paths.append(2)
		if o4 < 8:
			o4 = 5*o4
			y6 = 7-y6
			x = o4-y6
			paths.append(3)
		else:
			y6 = 4*y6
			o4 = y6/y6
			o4 = 0*o4
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))