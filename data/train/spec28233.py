import numpy as np 

def function(x):

	v2 = x
	y0 = x
	paths = []
	try:
		if x <= 3:
			x = x+0
			v2 = 8+v2
			paths.append(1)
		else:
			v2 = v2-5
			v2 = 8*5
			x = x-4
			paths.append(2)
		if x <= 8:
			x = 0*7
			paths.append(3)
		else:
			v2 = v2*y0
			y0 = y0/5
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		v2 = y0**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))