import numpy as np 

def function(x):

	y5 = 5
	r4 = 9
	x = x
	paths = []
	try:
		if r4 >= 1:
			r4 = r4-7
			r4 = 5-y5
			paths.append(1)
		else:
			y5 = 7-3
			r4 = 1*y5
			paths.append(2)
		if y5 > 4:
			x = x-8
			paths.append(3)
		else:
			x = x/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))