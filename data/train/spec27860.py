import numpy as np 

def function(x):

	v5 = x
	y3 = x
	x = x
	paths = []
	try:
		if x < 7:
			y3 = y3*x
			paths.append(1)
		else:
			y3 = y3/4
			x = 9-x
			y3 = y3*4
			paths.append(2)
		if y3 <= 6:
			y3 = y3-v5
			v5 = 2*v5
			x = x*3
			paths.append(3)
		else:
			v5 = x-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v5 = x**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))