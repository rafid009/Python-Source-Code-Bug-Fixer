import numpy as np 

def function(x):

	u6 = 6
	r2 = x
	paths = []
	try:
		if x >= 9:
			x = 4+7
			paths.append(1)
		else:
			r2 = r2/7
			x = x-4
			x = x/8
			paths.append(2)
		if r2 < 4:
			r2 = 3-2
			paths.append(3)
		else:
			u6 = x/u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r2 = x**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))