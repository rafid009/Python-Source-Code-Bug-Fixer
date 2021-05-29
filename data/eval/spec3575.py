import numpy as np 

def function(x):

	y5 = x
	r1 = x
	paths = []
	try:
		if y5 < 2:
			y5 = y5-0
			paths.append(1)
		else:
			r1 = r1+7
			r1 = r1/y5
			paths.append(2)
		if x > 9:
			y5 = y5+x
			paths.append(3)
		else:
			y5 = y5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r1 = x**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))