import numpy as np 

def function(x):

	o4 = 9
	k6 = 3
	paths = []
	try:
		if k6 > 5:
			x = 3+5
			paths.append(1)
		else:
			x = x*3
			paths.append(2)
		if k6 < 2:
			k6 = k6/3
			k6 = k6*5
			paths.append(3)
		else:
			k6 = o4*k6
			k6 = 7*k6
			o4 = o4*5
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